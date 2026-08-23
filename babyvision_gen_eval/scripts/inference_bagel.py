#!/usr/bin/env python3
"""
BabyVision Generation Track - BAGEL Inference Script

Runs ByteDance-Seed/BAGEL-7B-MoT in its native image-editing mode
(understanding_output=False, think=True) to generate annotated answer
images for BabyVision-Gen tasks, instead of BAGEL's text-answering mode
used on the earlier, deprecated understanding-track evaluation.

Output layout matches every other generation model in this repo:
    generated/{model_name}/round{N}/images/{uuid}_task{taskId}.png
    generated/{model_name}/round{N}/results.jsonl
so the existing babyvision_gen_eval/scripts/evaluate_local_hf.py judge
works unmodified.
"""

import os
import sys
import gc
import json
import argparse
from pathlib import Path
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
BAGEL_PATH = "/home/dsi/sinayyo/BabyVision/BAGEL"
if BAGEL_PATH not in sys.path:
    sys.path.append(BAGEL_PATH)

from accelerate import infer_auto_device_map, load_checkpoint_and_dispatch, init_empty_weights
from data.data_utils import add_special_tokens
from data.transforms import ImageTransform
from inferencer import InterleaveInferencer
from modeling.autoencoder import load_ae
from modeling.bagel import (
    BagelConfig, Bagel, Qwen2Config, Qwen2ForCausalLM,
    SiglipVisionConfig, SiglipVisionModel
)
from modeling.qwen2 import Qwen2Tokenizer


def load_bagel_inferencer(model_path: str) -> InterleaveInferencer:
    llm_config = Qwen2Config.from_json_file(os.path.join(model_path, "llm_config.json"))
    llm_config.pad_token_id = getattr(llm_config, 'pad_token_id', None) or getattr(llm_config, 'eos_token_id', 151645)
    llm_config.qk_norm = True
    llm_config.tie_word_embeddings = False
    llm_config.layer_module = "Qwen2MoTDecoderLayer"

    vit_config = SiglipVisionConfig.from_json_file(os.path.join(model_path, "vit_config.json"))
    vit_config.rope = False
    vit_config.num_hidden_layers -= 1

    print("Loading VAE model...")
    vae_model, vae_config = load_ae(local_path=os.path.join(model_path, "ae.safetensors"))

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
        vit_model = SiglipVisionModel(vit_config)
        model = Bagel(language_model, vit_model, config)
        model.vit_model.vision_model.embeddings.convert_conv2d_to_linear(vit_config, meta=True)

    tokenizer = Qwen2Tokenizer.from_pretrained(model_path)
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
        'vit_pos_embed',
    ]
    first_device = device_map.get(same_device_modules[0], "cuda:0" if torch.cuda.is_available() else "cpu")
    for k in same_device_modules:
        device_map[k] = device_map.get(k, first_device) if k in device_map else (
            "cuda:0" if torch.cuda.is_available() else "cpu"
        )

    print("Loading weights...")
    model = load_checkpoint_and_dispatch(
        model,
        checkpoint=os.path.join(model_path, "ema.safetensors"),
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
    return inferencer


def main():
    parser = argparse.ArgumentParser(description="BabyVision-Gen BAGEL inference (native image-editing mode)")
    parser.add_argument("--model-path", type=str,
                        default="/home/dsi/sinayyo/.cache/huggingface/hub/models--ByteDance-Seed--BAGEL-7B-MoT/snapshots/5019f57d168e5816e8f3f701b17cc816bb7cf24b",
                        help="Path to BAGEL checkpoint")
    parser.add_argument("--data-root", type=str, required=True, help="Data root folder containing images/")
    parser.add_argument("--jsonl", type=str, required=True, help="Input JSONL file path")
    parser.add_argument("--output", type=str, required=True, help="Output folder for generated images")
    parser.add_argument("--rounds", type=int, default=3, help="Number of generation rounds")
    parser.add_argument("--max-think-tokens", type=int, default=1024, help="Max tokens for BAGEL's pre-generation thinking step")
    parser.add_argument("--cfg-text-scale", type=float, default=4.0, help="Text CFG scale")
    parser.add_argument("--cfg-img-scale", type=float, default=2.0, help="Image CFG scale")
    args = parser.parse_args()

    inferencer = load_bagel_inferencer(args.model_path)

    tasks = []
    with open(args.jsonl, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                tasks.append(json.loads(line))
    print(f"Loaded {len(tasks)} tasks.")

    for round_idx in range(1, args.rounds + 1):
        round_dir = os.path.join(args.output, f"round{round_idx}")
        images_dir = os.path.join(round_dir, "images")
        os.makedirs(images_dir, exist_ok=True)
        print(f"\n--- Starting Round {round_idx}/{args.rounds} ---")

        output_results = []

        for task in tqdm(tasks, desc=f"Round {round_idx}"):
            task_id = task["taskId"]
            image_rel = task["image"]
            prompt = task["generationPrompt"]

            image_path = os.path.join(args.data_root, image_rel)
            name = os.path.splitext(os.path.basename(image_rel))[0]
            save_path = os.path.join(images_dir, f"{name}_task{task_id}.png")

            if os.path.exists(save_path):
                task_copy = task.copy()
                task_copy["generated_image"] = os.path.relpath(save_path, round_dir)
                output_results.append(task_copy)
                continue

            try:
                img = Image.open(image_path).convert("RGB")

                result = inferencer(
                    image=img,
                    text=prompt,
                    think=True,
                    understanding_output=False,
                    do_sample=False,
                    max_think_token_n=args.max_think_tokens,
                    cfg_text_scale=args.cfg_text_scale,
                    cfg_img_scale=args.cfg_img_scale,
                )
                edited_image = result["image"]
                if edited_image is None:
                    raise RuntimeError("BAGEL returned no image (result['image'] is None)")
                edited_image.save(save_path)

                task_copy = task.copy()
                task_copy["generated_image"] = os.path.relpath(save_path, round_dir)
                task_copy["bagel_thinking_text"] = result.get("text")
                output_results.append(task_copy)
            except Exception as e:
                print(f"\nError on task ID {task_id}: {e}")
                task_copy = task.copy()
                task_copy["generated_image"] = None
                output_results.append(task_copy)

        results_jsonl_path = os.path.join(round_dir, "results.jsonl")
        with open(results_jsonl_path, "w", encoding="utf-8") as f:
            for item in output_results:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
        print(f"Saved results to {results_jsonl_path}")

    del inferencer
    gc.collect()
    torch.cuda.empty_cache()


if __name__ == "__main__":
    main()
