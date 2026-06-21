#!/bin/bash
#SBATCH --partition=L4-12h
#SBATCH --gres=gpu:1
#SBATCH --mem=32G
#SBATCH --time=8:00:00
#SBATCH --job-name=babyvision_hf_eval
#SBATCH --output=slurm_hf_%j.out
#SBATCH --error=slurm_hf_%j.err

echo "=== Starting Slurm Job ==="
echo "Node: $SLURMD_NODENAME"
echo "Date: $(date)"

# Run local Hugging Face evaluation
cd babyvision_eval
../.venv/bin/python3 -u evaluate_local_hf.py \
    --model-id "Qwen/Qwen2.5-VL-7B-Instruct" \
    --judge-model-id "Qwen/Qwen2.5-7B-Instruct" \
    --test-json-path "../data/babyvision_data/meta_data.jsonl" \
    --output-dir "./results_local_hf" \
    --num-passes 3

echo "Computing final score summary..."
../.venv/bin/python3 compute_score.py results_local_hf/model_results_run_*.json > results_local_hf/score_summary.txt

echo "=== Evaluation Results ==="
cat results_local_hf/score_summary.txt
echo "=========================="

echo "=== Slurm Job Completed ==="
