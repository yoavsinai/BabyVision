#!/usr/bin/env python3
"""
RL Training Script for Gemma 4 on BabyVision Visual Reasoning tasks.
Uses TRL's GRPOTrainer with Verifiable Rewards (correctness & format).
"""

import os
import re
import json
import torch
import argparse
from PIL import Image
from pathlib import Path
from datasets import Dataset
from peft import LoraConfig
from transformers import AutoModelForImageTextToText, AutoProcessor
from trl import GRPOTrainer, GRPOConfig

def format_choices(options):
    formatted = []
    for idx, opt in enumerate(options):
        letter = chr(65 + idx)
        formatted.append(f"{letter}. {opt}")
    return "\n".join(formatted)

def get_completion_content(comp):
    if isinstance(comp, list) and len(comp) > 0 and isinstance(comp[0], dict):
        return comp[0].get("content", "")
    elif isinstance(comp, dict):
        return comp.get("content", "")
    elif isinstance(comp, str):
        return comp
    return ""

def extract_boxed_answer(text):
    # Find boxed answer
    matches = re.findall(r"\\boxed\{([^{}]+)\}", text)
    if matches:
        return matches[-1].strip().lower()
    return ""

# Reward functions
def correctness_reward(prompts, completions, answer, **kwargs):
    rewards = []
    for comp, ans in zip(completions, answer):
        content = get_completion_content(comp)
        extracted = extract_boxed_answer(content)
        target = str(ans).strip().lower()
        if extracted == target:
            rewards.append(1.0)
        else:
            rewards.append(0.0)
    return rewards

def format_reward(prompts, completions, **kwargs):
    rewards = []
    for comp in completions:
        content = get_completion_content(comp)
        # Check if the completion contains a boxed answer
        if "\\boxed{" in content and content.endswith("}"):
            rewards.append(0.1)
        elif "\\boxed{" in content:
            rewards.append(0.05)
        else:
            rewards.append(0.0)
    return rewards

def main():
    parser = argparse.ArgumentParser(description="RL training of Gemma 4 on BabyVision prompts")
    parser.add_argument("--model-id", type=str, default="google/gemma-4-E4B-it", help="Model ID to train")
    parser.add_argument("--data-path", type=str, default="../data/babyvision_data/meta_data.jsonl", help="Dataset file")
    parser.add_argument("--output-dir", type=str, default="./gemma4_rl_output", help="Output directory")
    parser.add_argument("--epochs", type=int, default=3, help="Number of training epochs")
    parser.add_argument("--learning-rate", type=float, default=1e-5, help="Learning rate")
    
    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    
    print("Loading dataset...")
    # Load and parse BabyVision tasks
    test_json_dir = os.path.dirname(args.data_path)
    raw_data = []
    with open(args.data_path, "r") as f:
        for line in f:
            if line.strip():
                raw_data.append(json.loads(line.strip()))
                
    formatted_samples = []
    for item in raw_data:
        image_path = os.path.join(test_json_dir, item['image'])
        if not os.path.exists(image_path):
            continue
            
        if item['ansType'] == "blank":
            question = item['question']
            answer = item['blankAns']
        else:
            question = item['question'] + "\nChoices:\n" + format_choices(item['options'])
            answer = chr(65 + int(item['choiceAns']))
            
        # Gemma system and user prompt formatting
        question_prompt = question + "\nAnswer the question as concisely as possible. Explain your reasoning in at most 2 sentences, and output your final answer inside \\boxed{Answer} at the end."
        
        prompt_messages = [
            {
                "role": "system",
                "content": [{"type": "text", "text": "You are a helpful vision-language assistant. You can see the provided image and must answer questions about it accurately and concisely."}]
            },
            {
                "role": "user",
                "content": [
                    {"type": "image"},
                    {"type": "text", "text": question_prompt}
                ]
            }
        ]
        
        try:
            pil_image = Image.open(image_path).convert("RGB")
            formatted_samples.append({
                "prompt": prompt_messages,
                "images": [pil_image],
                "answer": answer
            })
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")
            
    print(f"Loaded and formatted {len(formatted_samples)} tasks.")
    
    # Split dataset into train (80%) and val (20%)
    train_size = int(0.8 * len(formatted_samples))
    train_samples = formatted_samples[:train_size]
    val_samples = formatted_samples[train_size:]
    
    train_dataset = Dataset.from_list(train_samples)
    val_dataset = Dataset.from_list(val_samples)
    print(f"Train dataset size: {len(train_dataset)}")
    print(f"Val dataset size: {len(val_dataset)}")
    
    print("Loading model and processor...")
    processor = AutoProcessor.from_pretrained(args.model_id, trust_remote_code=True)
    model = AutoModelForImageTextToText.from_pretrained(
        args.model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True
    )
    model.config.use_cache = False
    
    # PEFT (LoRA) Config
    peft_config = LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules=["q_proj.linear", "k_proj.linear", "v_proj.linear", "o_proj.linear", "gate_proj.linear", "up_proj.linear", "down_proj.linear"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )
    
    # GRPO training configuration
    training_args = GRPOConfig(
        output_dir=args.output_dir,
        learning_rate=args.learning_rate,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=8,
        num_generations=4, # Group size
        max_completion_length=256,
        bf16=True,
        gradient_checkpointing=True,
        num_train_epochs=args.epochs,
        logging_steps=1,
        save_strategy="steps",
        save_steps=25,
        eval_strategy="no",
        report_to="none"
    )
    
    print("Initializing GRPOTrainer...")
    trainer = GRPOTrainer(
        model=model,
        processing_class=processor,
        reward_funcs=[correctness_reward, format_reward],
        args=training_args,
        train_dataset=train_dataset,
        peft_config=peft_config
    )
    
    print("Starting RL/GRPO training...")
    trainer.train()
    
    print("Saving final LoRA adapter...")
    trainer.save_model(os.path.join(args.output_dir, "final_lora"))
    print("RL training completed successfully.")

if __name__ == "__main__":
    main()
