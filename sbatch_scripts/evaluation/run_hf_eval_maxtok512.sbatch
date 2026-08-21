#!/bin/bash
#SBATCH --partition=L4-12h
#SBATCH --gres=gpu:1
#SBATCH --mem=32G
#SBATCH --time=8:00:00
#SBATCH --job-name=babyvision_hf_eval_maxtok512
#SBATCH --output=slurm_hf_maxtok512_%j.out
#SBATCH --error=slurm_hf_maxtok512_%j.err

echo "=== Starting Slurm Job ==="
echo "Node: $SLURMD_NODENAME"
echo "Date: $(date)"

# Reproduces the original (archived, log-less) Qwen 512-token baseline run,
# this time with a proper job ID and logs, so the "before" side of the
# token-budget hypothesis has a full audit trail.
cd babyvision_eval
../.venv/bin/python3 -u evaluate_local_hf.py \
    --model-id "Qwen/Qwen2.5-VL-7B-Instruct" \
    --judge-model-id "Qwen/Qwen2.5-7B-Instruct" \
    --test-json-path "../data/babyvision_data/meta_data.jsonl" \
    --output-dir "./runs/qwen_baseline_maxtok512_reproduced" \
    --max-tokens 512 \
    --num-passes 3

echo "Computing final score summary..."
../.venv/bin/python3 compute_score.py runs/qwen_baseline_maxtok512_reproduced/model_results_run_*.json > runs/qwen_baseline_maxtok512_reproduced/score_summary.txt

echo "=== Evaluation Results ==="
cat runs/qwen_baseline_maxtok512_reproduced/score_summary.txt
echo "=========================="

echo "=== Slurm Job Completed ==="
