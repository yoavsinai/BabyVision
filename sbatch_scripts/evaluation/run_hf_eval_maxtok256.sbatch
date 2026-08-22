#!/bin/bash
#SBATCH --partition=L4-12h
#SBATCH --gres=gpu:1
#SBATCH --mem=32G
#SBATCH --time=8:00:00
#SBATCH --job-name=babyvision_hf_eval_maxtok256
#SBATCH --output=qwen_baseline_maxtok256_eval_%j.out
#SBATCH --error=qwen_baseline_maxtok256_eval_%j.err

echo "=== Starting Slurm Job ==="
echo "Node: $SLURMD_NODENAME"
echo "Date: $(date)"

# Qwen was never subject to the Gemma-specific 256-token cap bug, so this
# run isn't reproducing a defect - it's an added data point to check whether
# Qwen's no-answer-rate-vs-accuracy pattern across token budgets matches the
# Gemma variants at the tightest budget tested elsewhere in this project.
cd babyvision_eval
../.venv/bin/python3 -u evaluate_local_hf.py \
    --model-id "Qwen/Qwen2.5-VL-7B-Instruct" \
    --judge-model-id "Qwen/Qwen2.5-7B-Instruct" \
    --test-json-path "../data/babyvision_data/meta_data.jsonl" \
    --output-dir "./runs/qwen_baseline_maxtok256" \
    --max-tokens 256 \
    --num-passes 3

echo "Computing final score summary..."
../.venv/bin/python3 compute_score.py runs/qwen_baseline_maxtok256/model_results_run_*.json > runs/qwen_baseline_maxtok256/score_summary.txt

echo "Computing no-answer rate..."
../.venv/bin/python3 compute_no_answer_rate.py runs/qwen_baseline_maxtok256/model_results_run_*.json

echo "=== Evaluation Results ==="
cat runs/qwen_baseline_maxtok256/score_summary.txt
echo "=========================="

echo "=== Slurm Job Completed ==="
