#!/bin/bash
#SBATCH --partition=L4-12h
#SBATCH --gres=gpu:1
#SBATCH --mem=32G
#SBATCH --time=8:00:00
#SBATCH --job-name=babyvision_gemma_eval
#SBATCH --output=slurm_gemma_%j.out
#SBATCH --error=slurm_gemma_%j.err

echo "=== Starting Slurm Job ==="
echo "Node: $SLURMD_NODENAME"
echo "Date: $(date)"

# Run local Hugging Face evaluation for Gemma 4
cd babyvision_eval
/home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/python3 -u evaluate_local_hf.py \
    --model-id "google/gemma-4-E4B-it" \
    --judge-model-id "Qwen/Qwen2.5-7B-Instruct" \
    --test-json-path "../data/babyvision_data/meta_data.jsonl" \
    --output-dir "./results_local_gemma_4" \
    --num-passes 3

echo "Computing final score summary..."
/home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/python3 compute_score.py results_local_gemma_4/model_results_run_*.json > results_local_gemma_4/score_summary.txt

echo "=== Evaluation Results ==="
cat results_local_gemma_4/score_summary.txt
echo "=========================="

echo "=== Slurm Job Completed ==="
