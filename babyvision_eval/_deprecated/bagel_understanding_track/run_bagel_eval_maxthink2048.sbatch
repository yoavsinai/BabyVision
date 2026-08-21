#!/bin/bash
#SBATCH --partition=A100-4h
#SBATCH --gres=gpu:1
#SBATCH --mem=64G
#SBATCH --time=04:00:00
#SBATCH --job-name=babyvision_bagel_eval_maxthink2048
#SBATCH --output=slurm_bagel_maxthink2048_%j.out
#SBATCH --error=slurm_bagel_maxthink2048_%j.err

echo "=== Starting Slurm Job ==="
echo "Node: $SLURMD_NODENAME"
echo "Date: $(date)"

export CUDA_HOME=/usr/local/cuda
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/home/dsi/sinayyo/BabyVision/local_ollama/lib/ollama/cuda_v12:/usr/local/cuda/lib64:/home/dsi/sinayyo/.conda/envs/babyvision_py310/lib:$LD_LIBRARY_PATH

# Doubling BAGEL's thinking-token budget (1024 -> 2048), same doubling pattern
# used for the Gemma/Qwen token-cap fix, to test whether BAGEL's 78% truncation
# rate (see results/bagel_comparison.md) is similarly undercutting its score.
cd babyvision_eval
/home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/python3 -u evaluate_bagel.py \
    --model-path "/home/dsi/sinayyo/.cache/huggingface/hub/models--ByteDance-Seed--BAGEL-7B-MoT/snapshots/5019f57d168e5816e8f3f701b17cc816bb7cf24b" \
    --judge-model-id "Qwen/Qwen2.5-7B-Instruct" \
    --test-json-path "../data/babyvision_data/meta_data.jsonl" \
    --output-dir "./runs/bagel_maxthink2048" \
    --max-think-tokens 2048 \
    --num-passes 3

echo "Computing final score summary..."
/home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/python3 compute_score.py runs/bagel_maxthink2048/model_results_run_*.json > runs/bagel_maxthink2048/score_summary.txt

echo "=== Evaluation Results ==="
cat runs/bagel_maxthink2048/score_summary.txt
echo "=========================="

echo "=== Slurm Job Completed ==="
