#!/usr/bin/env python3
"""
BabyVision Evaluation Script for System Prompt Optimization (Meta-RL)
Generates custom system prompts using the fine-tuned adapter, runs the base VLM, and judges the outputs.
"""

import os
import gc
import json
import re
import argparse
from tqdm import tqdm
from PIL import Image
import torch
from transformers import AutoModelForImageTextToText, AutoProcessor, AutoModelForCausalLM, AutoTokenizer

from utils import LLM_JUDGE_PROMPT, format_choices, extract_boxed_answer

def extract_boxed_system_prompt(text):
    idx = text.rfind(r"\boxed{")
    if idx == -1:
        return ""
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

def main():
    parser = argparse.ArgumentParser(description="Evaluate System Prompt RL Model on BabyVision")
    parser.add_argument("--model-id", type=str, default="google/gemma-4-E4B-it", help="Hugging Face model ID")
    parser.add_argument("--judge-model-id", type=str, default="Qwen/Qwen2.5-7B-Instruct", help="Hugging Face model ID for judge")
    parser.add_argument("--test-json-path", type=str, default="../data/babyvision_data/meta_data.jsonl", help="Path to test JSONL file")
    parser.add_argument("--output-dir", type=str, default="./results_system_prompt_rl", help="Output directory")
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

    # Prepare task structures
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

        tasks.append({
            "Id": item['taskId'],
            "raw_question": question,
            "image_path": image_path,
            "answer": answer,
            "Type": item['type'],
            "Subtype": item['subtype'],
        })

    # ==========================================
    # Phase 1: Model Generations (Two-Step Inference)
    # ==========================================
    print(f"\n--- Phase 1: Starting Two-Step Meta-RL Inference using {args.model_id} ---")
    print("Loading vision model and processor...")
    
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
    
    processor = AutoProcessor.from_pretrained(args.model_id, trust_remote_code=True)
    print("Model and processor loaded successfully.")

    default_sp = "You are a helpful vision-language assistant. You can see the provided image and must answer questions about it accurately and concisely."
    all_passes_results = []

    for pass_idx in range(args.num_passes):
        print(f"\nRunning pass {pass_idx + 1}/{args.num_passes}...")
        pass_results = []

        for task in tqdm(tasks, desc=f"Pass {pass_idx + 1}"):
            try:
                # Load image
                image = Image.open(task["image_path"]).convert("RGB")
                
                # Step 1: Query Policy Model to generate System Prompt
                prompt_messages = [
                    {
                        "role": "system",
                        "content": [{"type": "text", "text": "You are a helpful AI assistant prompt engineer. Your task is to generate a custom system prompt (instruction) for a vision-language assistant to help it solve the visual task correctly. Explain your reasoning and then output your final system prompt inside \\boxed{System Prompt}."}]
                    },
                    {
                        "role": "user",
                        "content": [
                            {"type": "image"},
                            {"type": "text", "text": f"Task Question:\n{task['raw_question']}\n\nAnalyze the image and question, and write a custom system prompt that will guide a vision-language assistant to answer the question correctly. Explain your reasoning in 1-2 sentences, and output the system prompt inside \\boxed{{System Prompt}}."}
                        ]
                    }
                ]
                policy_text = processor.apply_chat_template(prompt_messages, tokenize=False, add_generation_prompt=True)
                policy_inputs = processor(images=image, text=policy_text, return_tensors="pt").to(model.device)
                
                with torch.no_grad():
                    # Adapter is active for generating prompt
                    policy_gen = model.generate(**policy_inputs, max_new_tokens=128)
                
                policy_gen_trimmed = policy_gen[0][len(policy_inputs.input_ids[0]):]
                policy_output = processor.decode(policy_gen_trimmed, skip_special_tokens=True).strip()
                
                generated_sp = extract_boxed_system_prompt(policy_output)
                if not generated_sp or generated_sp.strip() == "":
                    generated_sp = default_sp
                
                # Step 2: Query Base Model (adapter disabled) with generated System Prompt
                eval_messages = [
                    {
                        "role": "system",
                        "content": [{"type": "text", "text": generated_sp}]
                    },
                    {
                        "role": "user",
                        "content": [
                            {"type": "image"},
                            {"type": "text", "text": task["raw_question"] + "\nAnswer the question as concisely as possible. Explain your reasoning in at most 2 sentences, and output your final answer inside \\boxed{Answer} at the end."}
                        ]
                    }
                ]
                eval_text = processor.apply_chat_template(eval_messages, tokenize=False, add_generation_prompt=True)
                eval_inputs = processor(images=image, text=eval_text, return_tensors="pt").to(model.device)
                
                with torch.no_grad():
                    # Disable LoRA adapter to query frozen base VLM
                    if args.peft_adapter_path:
                        with model.disable_adapter():
                            eval_gen = model.generate(**eval_inputs, max_new_tokens=256)
                    else:
                        eval_gen = model.generate(**eval_inputs, max_new_tokens=256)
                
                eval_gen_trimmed = eval_gen[0][len(eval_inputs.input_ids[0]):]
                model_output_result = processor.decode(eval_gen_trimmed, skip_special_tokens=True).strip()
                extracted_answer = extract_boxed_answer(model_output_result)
                
            except Exception as e:
                print(f"\nError running two-step inference on task ID {task['Id']}: {e}")
                policy_output = ""
                generated_sp = default_sp
                model_output_result = ""
                extracted_answer = ""

            pass_results.append({
                "Id": task['Id'],
                "Question": task['raw_question'],
                "GeneratedSystemPrompt": generated_sp,
                "PolicyExplanation": policy_output,
                "ModelReasoning": "",
                "ModelResult": model_output_result,
                "GroundTruth": task['answer'],
                "ExtractedAnswer": extracted_answer,
                "LLMJudgeResult": False,
                "Type": task['Type'],
                "Subtype": task['Subtype'],
            })
        
        all_passes_results.append(pass_results)
        
        # Save raw predictions
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
