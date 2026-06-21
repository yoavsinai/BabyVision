#!/usr/bin/env python3
"""
RL Training Script for optimizing System Prompts on BabyVision Visual Reasoning tasks.
Trains Gemma 4 to output custom system prompts for a frozen VLM to solve each task.
Uses TRL's GRPOTrainer with Verifiable Rewards (correctness of VLM answer & prompt formatting).
"""

import os
import re
import json
import torch
import argparse
from PIL import Image
from pathlib import Path
from datasets import Dataset
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForImageTextToText, AutoProcessor
from trl import GRPOTrainer, GRPOConfig

# Global correctness weight and model/processor references for the reward function
CORRECTNESS_WEIGHT = 2.0
eval_model = None
eval_processor = None

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

def extract_boxed_system_prompt(text):
    # Find the last occurrence of \boxed{
    idx = text.rfind(r"\boxed{")
    if idx == -1:
        return ""
    # Start scanning from idx + 7
    start_idx = idx + 7
    brace_count = 1
    end_idx = start_idx
    while end_idx < len(text) and brace_count > 0:
        if text[end_idx] == '{':
            brace_count += 1
        elif text[end_idx] == '}':
            brace_count -= 1
        end_idx += 1
    if brace_count == 0:
        return text[start_idx:end_idx-1].strip()
    return ""

# Reward functions
def system_prompt_correctness_reward(prompts, completions, answer, images, question, **kwargs):
    global eval_model, eval_processor, CORRECTNESS_WEIGHT
    rewards = []
    
    for comp, ans, imgs, q in zip(completions, answer, images, question):
        content = get_completion_content(comp)
        extracted_sp = extract_boxed_system_prompt(content)
        
        if not extracted_sp or extracted_sp.strip() == "":
            rewards.append(0.0)
            continue
            
        # Format the evaluation messages for the frozen VLM using the generated system prompt
        eval_messages = [
            {
                "role": "system",
                "content": [{"type": "text", "text": extracted_sp}]
            },
            {
                "role": "user",
                "content": [
                    {"type": "image"},
                    {"type": "text", "text": q + "\nAnswer the question as concisely as possible. Explain your reasoning in at most 2 sentences, and output your final answer inside \\boxed{Answer} at the end."}
                ]
            }
        ]
        
        try:
            eval_text = eval_processor.apply_chat_template(eval_messages, tokenize=False, add_generation_prompt=True)
            pil_image = imgs[0] if isinstance(imgs, list) else imgs
            
            inputs = eval_processor(images=pil_image, text=eval_text, return_tensors="pt").to(eval_model.device)
            
            with torch.no_grad():
                # Disable LoRA adapters to evaluate using the frozen base model
                with eval_model.disable_adapter():
                    generated_ids = eval_model.generate(
                        **inputs,
                        max_new_tokens=64,
                        use_cache=True,
                        pad_token_id=eval_processor.tokenizer.pad_token_id,
                        eos_token_id=eval_processor.tokenizer.eos_token_id
                    )
            
            generated_ids_trimmed = [
                out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
            ]
            vlm_output = eval_processor.batch_decode(
                generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
            )[0]
            
            extracted_ans = extract_boxed_answer(vlm_output)
            target = str(ans).strip().lower()
            
            if extracted_ans == target:
                rewards.append(CORRECTNESS_WEIGHT)
            else:
                rewards.append(0.0)
                
        except Exception as e:
            print(f"Error evaluating system prompt correctness: {e}")
            rewards.append(0.0)
            
    return rewards

def system_prompt_format_reward(prompts, completions, **kwargs):
    rewards = []
    for comp in completions:
        content = get_completion_content(comp)
        # Check if the completion contains a boxed system prompt
        idx = content.rfind(r"\boxed{")
        if idx != -1:
            brace_count = 1
            end_idx = idx + 7
            while end_idx < len(content) and brace_count > 0:
                if content[end_idx] == '{':
                    brace_count += 1
                elif content[end_idx] == '}':
                    brace_count -= 1
                end_idx += 1
            
            if brace_count == 0:
                # Higher reward if the box ends cleanly at the completion end
                if end_idx == len(content) or content[end_idx:].strip() == "":
                    rewards.append(0.1)
                else:
                    rewards.append(0.05)
            else:
                rewards.append(0.0)
        else:
            rewards.append(0.0)
    return rewards

def main():
    global eval_model, eval_processor, CORRECTNESS_WEIGHT
    
    parser = argparse.ArgumentParser(description="RL training on BabyVision prompts (System Prompt optimization)")
    parser.add_argument("--model-id", type=str, default="google/gemma-4-E4B-it", help="Model ID to train")
    parser.add_argument("--data-path", type=str, default="../data/babyvision_data/meta_data.jsonl", help="Dataset file")
    parser.add_argument("--output-dir", type=str, default="./gemma4_system_prompt_rl_output", help="Output directory")
    parser.add_argument("--epochs", type=int, default=2, help="Number of training epochs")
    parser.add_argument("--learning-rate", type=float, default=1e-5, help="Learning rate")
    parser.add_argument("--correctness-weight", type=float, default=2.0, help="Weight multiplier for correctness reward")
    
    args = parser.parse_args()
    CORRECTNESS_WEIGHT = args.correctness_weight
    os.makedirs(args.output_dir, exist_ok=True)
    
    print(f"=== Gemma 4 System Prompt RL Training ===")
    print(f"Output directory: {args.output_dir}")
    print(f"Correctness reward weight: {CORRECTNESS_WEIGHT}")
    print(f"Format reward weights: 0.1 (strict) / 0.05 (partial)")
    
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
            
        # Policy model system and user prompt formatting to generate system prompt
        prompt_messages = [
            {
                "role": "system",
                "content": [{"type": "text", "text": "You are a helpful AI assistant prompt engineer. Your task is to generate a custom system prompt (instruction) for a vision-language assistant to help it solve the visual task correctly. You must output the system prompt inside \\boxed{System Prompt} directly, with no other explanation or reasoning."}]
            },
            {
                "role": "user",
                "content": [
                    {"type": "image"},
                    {"type": "text", "text": f"Task Question:\n{question}\n\nAnalyze the image and question, and write a custom system prompt that will guide a vision-language assistant to answer the question correctly. Output your system prompt inside \\boxed{{System Prompt}} directly without any other text or explanation."}
                ]
            }
        ]
        
        try:
            pil_image = Image.open(image_path).convert("RGB")
            formatted_samples.append({
                "prompt": prompt_messages,
                "images": [pil_image],
                "answer": answer,
                "question": question
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
    
    # PEFT (LoRA) Config - Multimodal target (both language & vision tower)
    target_modules = ".*(language_model.*self_attn\\.(q_proj|k_proj|v_proj|o_proj)|language_model.*mlp\\.(gate_proj|up_proj|down_proj)|vision_tower.*self_attn\\.(q_proj|k_proj|v_proj|o_proj)\\.linear|vision_tower.*mlp\\.(gate_proj|up_proj|down_proj)\\.linear)$"
    peft_config = LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules=target_modules,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )
    
    # Wrap model with PEFT LoRA
    model = get_peft_model(model, peft_config)
    
    # Set references for reward function evaluation
    eval_model = model
    eval_processor = processor
    
    # GRPO training configuration
    training_args = GRPOConfig(
        output_dir=args.output_dir,
        learning_rate=args.learning_rate,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=8,
        num_generations=4,
        generation_batch_size=4,
        max_completion_length=128,
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
        reward_funcs=[system_prompt_correctness_reward, system_prompt_format_reward],
        args=training_args,
        train_dataset=train_dataset
    )
    
    print("Starting RL/GRPO training (System Prompt optimization)...")
    trainer.train()
    
    print("Saving final LoRA adapter...")
    trainer.save_model(os.path.join(args.output_dir, "final_lora"))
    print("RL training completed successfully.")

if __name__ == "__main__":
    main()
