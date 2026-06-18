#!/usr/bin/env python3
"""
BabyVision Auto-Evaluation Script (Local HF GPU version)
Evaluates generated images from any model against ground truth using local Qwen2.5-VL model on GPU.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from tqdm import tqdm
from PIL import Image
import torch
from transformers import AutoModelForImageTextToText, AutoProcessor
from qwen_vl_utils import process_vision_info

# Setup paths
SCRIPT_DIR = Path(__file__).parent
BASE_DIR = SCRIPT_DIR.parent
GENERATED_DIR = BASE_DIR / "generated"
RESULTS_DIR = BASE_DIR / "results"

from evaluate import build_evaluation_prompt, find_generated_image

def get_eval_inputs(model_id, processor, input_path, gt_path, gen_path, prompt):
    if "qwen" in model_id.lower():
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Image 1 (Input):"},
                    {"type": "image", "image": input_path},
                    {"type": "text", "text": "\nImage 2 (Ground Truth):"},
                    {"type": "image", "image": gt_path},
                    {"type": "text", "text": "\nImage 3 (Generated):"},
                    {"type": "image", "image": gen_path},
                    {"type": "text", "text": "\n" + prompt},
                ],
            }
        ]
        text = processor.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        from qwen_vl_utils import process_vision_info
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
        # Standard Hugging Face vision model (Gemma 4, etc.)
        messages = [
            {
                "role": "system",
                "content": [{"type": "text", "text": "You are a helpful vision-language assistant. You can see the provided images and must answer questions about them accurately and concisely."}]
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Image 1 (Input):"},
                    {"type": "image"},
                    {"type": "text", "text": "\nImage 2 (Ground Truth):"},
                    {"type": "image"},
                    {"type": "text", "text": "\nImage 3 (Generated):"},
                    {"type": "image"},
                    {"type": "text", "text": "\n" + prompt},
                ],
            }
        ]
        text = processor.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        images = [
            Image.open(input_path).convert("RGB"),
            Image.open(gt_path).convert("RGB"),
            Image.open(gen_path).convert("RGB"),
        ]
        inputs = processor(
            text=[text],
            images=images,
            return_tensors="pt"
        )
        return inputs

def main():
    parser = argparse.ArgumentParser(description="Evaluate generated images locally on GPU using Hugging Face")
    parser.add_argument("--model-name", type=str, required=True, help="Model name to evaluate")
    parser.add_argument("--round", type=str, default="all", help="Round name (e.g. round1) or 'all'")
    parser.add_argument("--tasks-file", type=str, default="../data/babyvision_gen_data/meta_data.jsonl", help="Path to tasks JSONL file")
    parser.add_argument("--eval-model-id", type=str, default="Qwen/Qwen2.5-VL-7B-Instruct", help="LLM model ID for evaluation")
    parser.add_argument("--data-root", type=str, default="../data/babyvision_gen_data", help="Data root folder containing images/ and answerImages/")

    args = parser.parse_args()

    # Load tasks
    tasks = []
    with open(args.tasks_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                tasks.append(json.loads(line))
    print(f"[INFO] Loaded {len(tasks)} tasks.")

    # Determine rounds to evaluate
    model_dir = GENERATED_DIR / args.model_name
    if not model_dir.exists():
        print(f"[ERROR] Model directory not found: {model_dir}")
        sys.exit(1)

    if args.round == "all":
        rounds = [d.name for d in model_dir.iterdir() if d.is_dir() and d.name.startswith("round")]
    else:
        rounds = [args.round]

    if not rounds:
        print(f"[ERROR] No rounds found to evaluate in {model_dir}")
        sys.exit(1)

    print(f"[INFO] Evaluating model '{args.model_name}' for rounds: {rounds}")

    # Load evaluation model on GPU
    print(f"Loading local evaluation model: {args.eval_model_id}...")
    
    model = AutoModelForImageTextToText.from_pretrained(
        args.eval_model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True
    )
    
    if "qwen" in args.eval_model_id.lower():
        # Configure max_pixels to avoid huge VRAM consumption with 3 images
        min_pixels = 256 * 28 * 28
        max_pixels = 512 * 28 * 28
        processor = AutoProcessor.from_pretrained(
            args.eval_model_id,
            min_pixels=min_pixels,
            max_pixels=max_pixels,
            trust_remote_code=True
        )
    else:
        processor = AutoProcessor.from_pretrained(
            args.eval_model_id,
            trust_remote_code=True
        )
    print("Evaluation model loaded successfully.")

    for round_name in rounds:
        round_results_dir = RESULTS_DIR / args.model_name / round_name
        round_results_dir.makedirs(exist_ok=True) if hasattr(round_results_dir, "makedirs") else os.makedirs(round_results_dir, exist_ok=True)
        eval_output_path = round_results_dir / "eval.jsonl"

        # Load completed to resume
        completed = {}
        if eval_output_path.exists():
            with open(eval_output_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        item = json.loads(line)
                        completed[item["taskId"]] = item

        print(f"\n--- Evaluating {round_name} ---")
        output_results = []
        
        for task in tqdm(tasks, desc=round_name):
            task_id = task["taskId"]
            
            # Resume if already completed
            if task_id in completed:
                output_results.append(completed[task_id])
                continue

            input_path = os.path.join(args.data_root, task["image"])
            gt_path = os.path.join(args.data_root, task["answerImage"])
            gen_path = find_generated_image(task, args.model_name, round_name)

            if not gen_path or not os.path.exists(gen_path):
                # Count as false if generated image is missing
                output_results.append({
                    "taskId": task_id,
                    "type": task.get("type", ""),
                    "subtype": task.get("subtype", ""),
                    "autoEval": False,
                    "error": "Generated image missing",
                    "response": "False"
                })
                continue

            prompt = build_evaluation_prompt(task)
            
            try:
                inputs = get_eval_inputs(args.eval_model_id, processor, input_path, gt_path, gen_path, prompt)
                inputs = inputs.to("cuda")
                
                with torch.inference_mode():
                    generated_ids = model.generate(**inputs, max_new_tokens=10)
                
                generated_ids_trimmed = [
                    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
                ]
                response_text = processor.batch_decode(
                    generated_ids_trimmed, skip_special_tokens=True
                )[0].strip()
                
                # Check response
                auto_eval = "true" in response_text.lower()
                error_msg = None
            except Exception as e:
                response_text = ""
                auto_eval = False
                error_msg = str(e)
                print(f"\nError evaluating task ID {task_id}: {e}")

            output_results.append({
                "taskId": task_id,
                "type": task.get("type", ""),
                "subtype": task.get("subtype", ""),
                "autoEval": auto_eval,
                "error": error_msg,
                "response": response_text
            })

            # Intermediate save to support resume
            with open(eval_output_path, "w", encoding="utf-8") as f:
                for item in output_results:
                    f.write(json.dumps(item, ensure_ascii=False) + "\n")
                    
        print(f"[INFO] Completed round {round_name} evaluation. Saved to {eval_output_path}")

    print("\n=== Evaluation Complete ===")

if __name__ == "__main__":
    main()
