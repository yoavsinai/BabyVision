#!/usr/bin/env python3
"""
BabyVision BAGEL Model Evaluation Script
Loads BAGEL using its custom architecture and runs evaluation on the benchmark.
"""

import os
import gc
import sys
import json
import argparse
from tqdm import tqdm
from PIL import Image
import torch

# Patch transformers ROPE_INIT_FUNCTIONS for default rope type in newer transformers version
from transformers.modeling_rope_utils import ROPE_INIT_FUNCTIONS
def compute_default_rope_parameters(config, device=None, seq_len=None, **kwargs):
    if hasattr(config, 'standardize_rope_params'):
        config.standardize_rope_params()
    base = config.rope_parameters.get("rope_theta", getattr(config, "rope_theta", 1000000.0)) if hasattr(config, "rope_parameters") else getattr(config, "rope_theta", 1000000.0)
    head_dim = getattr(config, "head_dim", None) or config.hidden_size // config.num_attention_heads
    partial_rotary_factor = getattr(config, "partial_rotary_factor", 1.0)
    dim = int(head_dim * partial_rotary_factor)
    inv_freq = 1.0 / (
        base ** (torch.arange(0, dim, 2, dtype=torch.int64).to(device=device, dtype=torch.float) / dim)
    )
    return inv_freq, 1.0

ROPE_INIT_FUNCTIONS["default"] = compute_default_rope_parameters

# Add BAGEL to path
bagel_path = "/home/dsi/sinayyo/BabyVision/BAGEL"
if bagel_path not in sys.path:
    sys.path.append(bagel_path)

from accelerate import infer_auto_device_map, load_checkpoint_and_dispatch, init_empty_weights
from data.data_utils import add_special_tokens, pil_img2rgb
from data.transforms import ImageTransform
from inferencer import InterleaveInferencer
from modeling.autoencoder import load_ae
from modeling.bagel import (
    BagelConfig, Bagel, Qwen2Config, Qwen2ForCausalLM,
    SiglipVisionConfig, SiglipVisionModel
)
from modeling.qwen2 import Qwen2Tokenizer

from transformers import AutoModelForCausalLM, AutoTokenizer
from utils import LLM_JUDGE_PROMPT, format_choices, extract_boxed_answer

def main():
    parser = argparse.ArgumentParser(description="Evaluate BAGEL model locally on GPU")
    parser.add_argument("--model-path", type=str, default="/home/dsi/sinayyo/.cache/huggingface/hub/models--ByteDance-Seed--BAGEL-7B-MoT/snapshots/5019f57d168e5816e8f3f701b17cc816bb7cf24b", help="Path to BAGEL checkpoint")
    parser.add_argument("--judge-model-id", type=str, default="Qwen/Qwen2.5-7B-Instruct", help="Hugging Face model ID for the judge")
    parser.add_argument("--test-json-path", type=str, default="../data/babyvision_data/meta_data.jsonl", help="Path to test JSONL file")
    parser.add_argument("--output-dir", type=str, default="./results_local_bagel", help="Output directory")
    parser.add_argument("--num-passes", type=int, default=3, help="Number of evaluation passes")
    parser.add_argument("--skip-judge", action="store_true", help="Skip running the judge phase")

    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    # 1. Load test data
    meta_data = []
    with open(args.test_json_path, "r") as f:
        for line in f:
            if line.strip():
                meta_data.append(json.loads(line.strip()))
    print(f"Loaded {len(meta_data)} tasks from {args.test_json_path}")

    # Prepare list of items to process
    tasks = []
    test_json_dir = os.path.dirname(args.test_json_path)
    for item in meta_data:
        image_path = os.path.join(test_json_dir, item['image'])
        if item['ansType'] == "blank":
            question = item['question']
            answer = item['blankAns']
        else:
            question = item['question'] + "\nChoices:\n" + format_choices(item['options'])
            answer = chr(65 + int(item['choiceAns']))

        question = question + "\nThink about the question and give your final answer in \\boxed{Answer} format."
        tasks.append({
            "Id": item['taskId'],
            "question": question,
            "image_path": image_path,
            "answer": answer,
            "Type": item['type'],
            "Subtype": item['subtype'],
        })

    # ==========================================
    # Phase 1: Run MLLM Inference
    # ==========================================
    print(f"\n--- Phase 1: Starting Vision Inference using BAGEL ---")
    
    # Load BAGEL components
    llm_config = Qwen2Config.from_json_file(os.path.join(args.model_path, "llm_config.json"))
    llm_config.pad_token_id = getattr(llm_config, 'pad_token_id', None) or getattr(llm_config, 'eos_token_id', 151645)
    llm_config.qk_norm = True
    llm_config.tie_word_embeddings = False
    llm_config.layer_module = "Qwen2MoTDecoderLayer"
    
    vit_config = SiglipVisionConfig.from_json_file(os.path.join(args.model_path, "vit_config.json"))
    vit_config.rope = False
    vit_config.num_hidden_layers -= 1
    
    print("Loading VAE model...")
    vae_model, vae_config = load_ae(local_path=os.path.join(args.model_path, "ae.safetensors"))
    
    config = BagelConfig(
        visual_gen=True,
        visual_und=True,
        llm_config=llm_config, 
        vit_config=vit_config,
        vae_config=vae_config,
        vit_max_num_patch_per_side=70,
        connector_act='gelu_pytorch_tanh',
        latent_patch_size=2,
        max_latent_size=64,
    )
    
    print("Initializing model architecture...")
    with init_empty_weights():
        language_model = Qwen2ForCausalLM(llm_config)
        vit_model      = SiglipVisionModel(vit_config)
        model          = Bagel(language_model, vit_model, config)
        model.vit_model.vision_model.embeddings.convert_conv2d_to_linear(vit_config, meta=True)
    
    tokenizer = Qwen2Tokenizer.from_pretrained(args.model_path)
    tokenizer, new_token_ids, _ = add_special_tokens(tokenizer)
    
    vae_transform = ImageTransform(1024, 512, 16)
    vit_transform = ImageTransform(980, 224, 14)
    
    print("Determining device map...")
    device_map = infer_auto_device_map(
        model,
        max_memory={i: "80GiB" for i in range(torch.cuda.device_count())} if torch.cuda.is_available() else {0: "80GiB"},
        no_split_module_classes=["Bagel", "Qwen2MoTDecoderLayer"],
    )
    
    same_device_modules = [
        'language_model.model.embed_tokens',
        'time_embedder',
        'latent_pos_embed',
        'vae2llm',
        'llm2vae',
        'connector',
        'vit_pos_embed'
    ]
    
    first_device = device_map.get(same_device_modules[0], "cuda:0" if torch.cuda.is_available() else "cpu")
    for k in same_device_modules:
        if k in device_map:
            device_map[k] = first_device
        else:
            device_map[k] = "cuda:0" if torch.cuda.is_available() else "cpu"
            
    print("Loading weights...")
    model = load_checkpoint_and_dispatch(
        model,
        checkpoint=os.path.join(args.model_path, "ema.safetensors"),
        device_map=device_map,
        offload_buffers=True,
        dtype=torch.bfloat16,
        force_hooks=True,
    ).eval()
    
    print("Initializing Inferencer...")
    inferencer = InterleaveInferencer(
        model=model,
        vae_model=vae_model,
        tokenizer=tokenizer,
        vae_transform=vae_transform,
        vit_transform=vit_transform,
        new_token_ids=new_token_ids,
    )
    print("Model loaded successfully.")

    all_passes_results = []

    for pass_idx in range(args.num_passes):
        print(f"\nRunning pass {pass_idx + 1}/{args.num_passes}...")
        raw_output_path = os.path.join(args.output_dir, f"raw_results_run_{pass_idx + 1}.json")
        
        # Load existing raw results to resume if file exists
        existing_results = {}
        if os.path.exists(raw_output_path):
            try:
                with open(raw_output_path, "r") as f:
                    loaded_data = json.load(f)
                    for item in loaded_data:
                        if item.get("ModelResult") != "":
                            existing_results[item["Id"]] = item
                print(f"Found {len(existing_results)} existing raw results. Resuming...")
            except Exception as e:
                print(f"Error loading existing raw results: {e}")

        pass_results = []

        for task in tqdm(tasks, desc=f"Pass {pass_idx + 1}"):
            if task["Id"] in existing_results:
                pass_results.append(existing_results[task["Id"]])
                continue

            try:
                image = Image.open(task["image_path"])
                
                result = inferencer(
                    image=image,
                    text=task["question"],
                    think=True,
                    understanding_output=True,
                    do_sample=False,
                    max_think_token_n=1024,
                )
                model_output_result = result["text"]
                extracted_answer = extract_boxed_answer(model_output_result)
            except Exception as e:
                print(f"\nError running model inference on task ID {task['Id']}: {e}")
                model_output_result = ""
                extracted_answer = ""

            pass_results.append({
                "Id": task['Id'],
                "Question": task['question'],
                "ModelReasoning": "",
                "ModelResult": model_output_result,
                "GroundTruth": task['answer'],
                "ExtractedAnswer": extracted_answer,
                "LLMJudgeResult": False,  # Will be filled in Phase 2
                "Type": task['Type'],
                "Subtype": task['Subtype'],
            })
            
            # Save raw predictions intermediate files incrementally every 5 tasks
            if len(pass_results) % 5 == 0 or len(pass_results) == len(tasks):
                with open(raw_output_path, "w") as f:
                    json.dump(pass_results, f, indent=2)
        
        # Save raw predictions at the end of the pass
        with open(raw_output_path, "w") as f:
            json.dump(pass_results, f, indent=2)
        print(f"Saved raw inference results to {raw_output_path}")
        
        all_passes_results.append(pass_results)

    # Unload vision model to free VRAM
    print("\nUnloading vision model to free VRAM for the judge model...")
    del model
    del inferencer
    gc.collect()
    torch.cuda.empty_cache()
    print("VRAM cleared.")

    if args.skip_judge:
        print("Skipping judge phase as requested.")
        return

    # ==========================================
    # Phase 2: Run LLM Judge
    # ==========================================
    print(f"\n--- Phase 2: Starting LLM Judge using {args.judge_model_id} ---")
    print("Loading judge model and tokenizer...")
    judge_model = AutoModelForCausalLM.from_pretrained(
        args.judge_model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True
    )
    judge_tokenizer = AutoTokenizer.from_pretrained(args.judge_model_id, trust_remote_code=True)
    print("Judge model loaded successfully.")

    for pass_idx, pass_results in enumerate(all_passes_results):
        print(f"\nJudging pass {pass_idx + 1}/{args.num_passes}...")
        output_path = os.path.join(args.output_dir, f"model_results_run_{pass_idx + 1}.json")
        
        # Load existing judged results to resume
        existing_judged = {}
        if os.path.exists(output_path):
            try:
                with open(output_path, "r") as f:
                    loaded_data = json.load(f)
                    for item in loaded_data:
                        if "LLMJudgeResult" in item:
                            existing_judged[item["Id"]] = item["LLMJudgeResult"]
                print(f"Found {len(existing_judged)} existing judged results. Resuming...")
            except Exception as e:
                print(f"Error loading existing judged results: {e}")

        for idx, result in enumerate(tqdm(pass_results, desc=f"Judging Pass {pass_idx + 1}")):
            if result["Id"] in existing_judged:
                result["LLMJudgeResult"] = existing_judged[result["Id"]]
                continue

            if not result["ExtractedAnswer"]:
                result["LLMJudgeResult"] = False
                if (idx + 1) % 5 == 0 or (idx + 1) == len(pass_results):
                    with open(output_path, "w") as f:
                        json.dump(pass_results, f, indent=2)
                continue

            try:
                judge_prompt = LLM_JUDGE_PROMPT.format(
                    question=result["Question"],
                    groundtruth=result["GroundTruth"],
                    modeloutput=result["ExtractedAnswer"]
                )
                messages = [{"role": "user", "content": judge_prompt}]
                text = judge_tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
                inputs = judge_tokenizer([text], return_tensors="pt").to("cuda")
                
                with torch.no_grad():
                    generated_ids = judge_model.generate(**inputs, max_new_tokens=10)
                
                generated_ids_trimmed = [
                    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
                ]
                judge_response = judge_tokenizer.batch_decode(
                    generated_ids_trimmed, skip_special_tokens=True
                )[0].strip().lower()

                if 'true' in judge_response:
                    result["LLMJudgeResult"] = True
                else:
                    result["LLMJudgeResult"] = False
            except Exception as e:
                print(f"\nError running judge model on task ID {result['Id']}: {e}")
                result["LLMJudgeResult"] = False

            if (idx + 1) % 5 == 0 or (idx + 1) == len(pass_results):
                with open(output_path, "w") as f:
                    json.dump(pass_results, f, indent=2)

        # Save final complete files
        with open(output_path, "w") as f:
            json.dump(pass_results, f, indent=2)
        print(f"Saved completed evaluation results to {output_path}")

    print("\n=== All Evaluation Passes Complete ===")

if __name__ == "__main__":
    main()
