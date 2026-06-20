#!/bin/bash
#SBATCH --partition=L4-12h
#SBATCH --gres=gpu:1
#SBATCH --mem=32G
#SBATCH --time=8:00:00
#SBATCH --job-name=babyvision_gemma_rl_v2_eval
#SBATCH --output=slurm_gemma_rl_v2_eval_%j.out
#SBATCH --error=slurm_gemma_rl_v2_eval_%j.err

echo "=== Starting Slurm Job ==="
echo "Node: $SLURMD_NODENAME"
echo "Date: $(date)"

# Run local Hugging Face evaluation for fine-tuned Gemma 4
cd babyvision_eval
/home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/python3 -u evaluate_local_hf.py \
    --model-id "google/gemma-4-E4B-it" \
    --peft-adapter-path "./gemma4_rl_output_v2/final_lora" \
    --judge-model-id "Qwen/Qwen2.5-7B-Instruct" \
    --test-json-path "../data/babyvision_data/meta_data.jsonl" \
    --output-dir "./results_local_gemma_4_rl_v2" \
    --num-passes 3

echo "Computing final score summary..."
/home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/python3 compute_score.py results_local_gemma_4_rl_v2/model_results_run_*.json > results_local_gemma_4_rl_v2/score_summary.txt

echo "=== Evaluation Results ==="
cat results_local_gemma_4_rl_v2/score_summary.txt
echo "=========================="

echo "=== Slurm Job Completed ==="
