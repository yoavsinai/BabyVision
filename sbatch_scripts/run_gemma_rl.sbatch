#!/bin/bash
#SBATCH --partition=L4-12h
#SBATCH --gres=gpu:1
#SBATCH --mem=32G
#SBATCH --time=6:00:00
#SBATCH --job-name=gemma_rl_train
#SBATCH --output=slurm_gemma_rl_%j.out
#SBATCH --error=slurm_gemma_rl_%j.err

echo "=== Starting Gemma 4 RL Training Job ==="
echo "Node: $SLURMD_NODENAME"
echo "Date: $(date)"

cd babyvision_eval

# Run RL training using our Python environment
/home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/python3 -u rl_train_gemma4.py \
    --model-id "google/gemma-4-E4B-it" \
    --data-path "../data/babyvision_data/meta_data.jsonl" \
    --output-dir "./gemma4_rl_output" \
    --epochs 3 \
    --learning-rate 1e-5

echo "=== Slurm Job Completed ==="
