#!/bin/bash
#SBATCH --partition=L4-12h
#SBATCH --gres=gpu:1
#SBATCH --mem=32G
#SBATCH --time=12:00:00
#SBATCH --job-name=babyvision_hf_eval_maxtok1024
#SBATCH --output=slurm_hf_maxtok1024_%j.out
#SBATCH --error=slurm_hf_maxtok1024_%j.err

echo "=== Starting Slurm Job ==="
echo "Node: $SLURMD_NODENAME"
echo "Date: $(date)"

# Run local Hugging Face evaluation
cd babyvision_eval
../.venv/bin/python3 -u evaluate_local_hf.py \
    --model-id "Qwen/Qwen2.5-VL-7B-Instruct" \
    --judge-model-id "Qwen/Qwen2.5-7B-Instruct" \
    --test-json-path "../data/babyvision_data/meta_data.jsonl" \
    --output-dir "./runs/qwen_baseline_maxtok1024" \
    --num-passes 3

echo "Computing final score summary..."
../.venv/bin/python3 compute_score.py runs/qwen_baseline_maxtok1024/model_results_run_*.json > runs/qwen_baseline_maxtok1024/score_summary.txt

echo "=== Evaluation Results ==="
cat runs/qwen_baseline_maxtok1024/score_summary.txt
echo "=========================="

echo "=== Slurm Job Completed ==="
