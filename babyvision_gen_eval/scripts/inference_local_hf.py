#!/usr/bin/env python3
"""
BabyVision Image Generation Local HF Inference Script
Generates annotated images locally on GPU using timbrooks/instruct-pix2pix.
"""

import os
import json
import argparse
from PIL import Image
from tqdm import tqdm
import torch
from diffusers import StableDiffusionInstructPix2PixPipeline

def main():
    parser = argparse.ArgumentParser(description="BabyVision Image Generation Local HF Inference")
    parser.add_argument("--data-root", type=str, required=True, help="Data root folder containing images/")
    parser.add_argument("--jsonl", type=str, required=True, help="Input JSONL file path")
    parser.add_argument("--output", type=str, required=True, help="Output folder for generated images")
    parser.add_argument("--rounds", type=int, default=3, help="Number of generation rounds")
    parser.add_argument("--model-id", type=str, default="timbrooks/instruct-pix2pix", help="InstructPix2Pix model ID")
    parser.add_argument("--steps", type=int, default=30, help="Number of inference steps")
    parser.add_argument("--image-guidance-scale", type=float, default=1.5, help="Image guidance scale")
    parser.add_argument("--guidance-scale", type=float, default=7.5, help="Text guidance scale")
    
    args = parser.parse_args()
    
    # Load pipeline
    print(f"Loading local InstructPix2Pix pipeline: {args.model_id}...")
    pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(
        args.model_id,
        torch_dtype=torch.float16,
        safety_checker=None
    ).to("cuda")
    print("Model loaded successfully.")
    
    # Load tasks
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
            
            # Skip if already exists
            if os.path.exists(save_path):
                task_copy = task.copy()
                task_copy["generated_image"] = os.path.relpath(save_path, round_dir)
                output_results.append(task_copy)
                continue
                
            try:
                # Load and prepare image
                img = Image.open(image_path).convert("RGB")
                # Resize to 512x512 for speed and stability
                img = img.resize((512, 512))
                
                # Run pipeline
                with torch.inference_mode():
                    edited_image = pipe(
                        prompt,
                        image=img,
                        num_inference_steps=args.steps,
                        image_guidance_scale=args.image_guidance_scale,
                        guidance_scale=args.guidance_scale
                    ).images[0]
                
                edited_image.save(save_path)
                
                task_copy = task.copy()
                task_copy["generated_image"] = os.path.relpath(save_path, round_dir)
                output_results.append(task_copy)
            except Exception as e:
                print(f"\nError on task ID {task_id}: {e}")
                task_copy = task.copy()
                task_copy["generated_image"] = None
                output_results.append(task_copy)
                
        # Save round results.jsonl
        results_jsonl_path = os.path.join(round_dir, "results.jsonl")
        with open(results_jsonl_path, "w", encoding="utf-8") as f:
            for item in output_results:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
        print(f"Saved results to {results_jsonl_path}")

if __name__ == "__main__":
    main()
