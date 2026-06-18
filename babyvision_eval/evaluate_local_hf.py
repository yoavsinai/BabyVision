#!/usr/bin/env python3
"""
BabyVision Local Hugging Face Evaluation Script
Runs vision-language model inference and judges answers locally on GPU.
"""

import os
import gc
import json
import regex
import argparse
from tqdm import tqdm
from PIL import Image
import torch
from transformers import AutoModelForImageTextToText, AutoProcessor, AutoModelForCausalLM, AutoTokenizer

from utils import LLM_JUDGE_PROMPT, format_choices, extract_boxed_answer

def get_inputs(model_id, processor, image_path, question):
    image = Image.open(image_path).convert("RGB")
    
    if "qwen" in model_id.lower():
        from qwen_vl_utils import process_vision_info
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": image_path},
                    {"type": "text", "text": question},
                ],
            }
        ]
        text = processor.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        image_inputs, video_inputs = process_vision_info(messages)
        inputs = processor(
            text=[text],
            images=image_inputs,
            videos=video_inputs,
            padding=True,
            return_tensors="pt",
        )
        return inputs
    else:
        # Standard Hugging Face vision model interface (Gemma 4, etc.)
        messages = [
            {
                "role": "system",
                "content": [{"type": "text", "text": "You are a helpful vision-language assistant. You can see the provided image and must answer questions about it accurately and concisely."}]
            },
            {
                "role": "user",
                "content": [
                    {"type": "image"},
                    {"type": "text", "text": question},
                ],
            }
        ]
        text = processor.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = processor(
            images=image,
            text=text,
            return_tensors="pt"
        )
        return inputs

def main():
    parser = argparse.ArgumentParser(description="Evaluate MLLM locally on GPU using Hugging Face")
    parser.add_argument("--model-id", type=str, default="Qwen/Qwen2.5-VL-7B-Instruct", help="Hugging Face model ID to evaluate")
    parser.add_argument("--judge-model-id", type=str, default="Qwen/Qwen2.5-7B-Instruct", help="Hugging Face model ID for the judge")
    parser.add_argument("--test-json-path", type=str, default="../data/babyvision_data/meta_data.jsonl", help="Path to test JSONL file")
    parser.add_argument("--output-dir", type=str, default="./results_local_hf", help="Output directory")
    parser.add_argument("--num-passes", type=int, default=3, help="Number of evaluation passes")
    parser.add_argument("--skip-judge", action="store_true", help="Skip running the judge phase")
    parser.add_argument("--peft-adapter-path", type=str, default=None, help="Path to PEFT/LoRA adapter weights")

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

        if "gemma" in args.model_id.lower():
            question = question + "\nAnswer the question as concisely as possible. Explain your reasoning in at most 2 sentences, and output your final answer inside \\boxed{Answer} at the end."
        else:
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
    print(f"\n--- Phase 1: Starting Vision Inference using {args.model_id} ---")
    print("Loading vision model and processor...")
    
    # Load model and processor
    model = AutoModelForImageTextToText.from_pretrained(
        args.model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True
    )
    if args.peft_adapter_path:
        from peft import PeftModel
        print(f"Loading Peft LoRA adapter from {args.peft_adapter_path}...")
        model = PeftModel.from_pretrained(model, args.peft_adapter_path)
    if "qwen" in args.model_id.lower():
        min_pixels = 256 * 28 * 28
        max_pixels = 512 * 28 * 28
        processor = AutoProcessor.from_pretrained(args.model_id, min_pixels=min_pixels, max_pixels=max_pixels, trust_remote_code=True)
    else:
        processor = AutoProcessor.from_pretrained(args.model_id, trust_remote_code=True)
    print("Model loaded successfully.")

    all_passes_results = []

    for pass_idx in range(args.num_passes):
        print(f"\nRunning pass {pass_idx + 1}/{args.num_passes}...")
        pass_results = []

        for task in tqdm(tasks, desc=f"Pass {pass_idx + 1}"):
            try:
                inputs = get_inputs(args.model_id, processor, task["image_path"], task["question"])
                inputs = inputs.to("cuda")
                
                max_tokens = 256 if "gemma" in args.model_id.lower() else 512
                with torch.no_grad():
                    generated_ids = model.generate(**inputs, max_new_tokens=max_tokens)
                
                generated_ids_trimmed = [
                    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
                ]
                model_output_result = processor.batch_decode(
                    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
                )[0]
                
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
        
        all_passes_results.append(pass_results)
        
        # Save raw predictions intermediate files
        raw_output_path = os.path.join(args.output_dir, f"raw_results_run_{pass_idx + 1}.json")
        with open(raw_output_path, "w") as f:
            json.dump(pass_results, f, indent=2)
        print(f"Saved raw inference results to {raw_output_path}")

    # Unload vision model to free VRAM
    print("\nUnloading vision model to free VRAM for the judge model...")
    del model
    del processor
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
        
        for idx, result in enumerate(tqdm(pass_results, desc=f"Judging Pass {pass_idx + 1}")):
            if not result["ExtractedAnswer"]:
                result["LLMJudgeResult"] = False
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

        # Save final complete files
        output_path = os.path.join(args.output_dir, f"model_results_run_{pass_idx + 1}.json")
        with open(output_path, "w") as f:
            json.dump(pass_results, f, indent=2)
        print(f"Saved completed evaluation results to {output_path}")

    print("\n=== All Evaluation Passes Complete ===")

if __name__ == "__main__":
    main()
