#!/bin/bash
#SBATCH --partition=L4-4h
#SBATCH --gres=gpu:1
#SBATCH --mem=32G
#SBATCH --time=2:00:00
#SBATCH --job-name=babyvision_gen_eval
#SBATCH --output=slurm_gen_%j.out
#SBATCH --error=slurm_gen_%j.err

echo "=== Starting Slurm Job ==="
echo "Node: $SLURMD_NODENAME"
echo "Date: $(date)"

cd babyvision_gen_eval

# Step 1: Run Local Image Generation Inference (3 rounds)
# echo "Starting local image generation inference using InstructPix2Pix..."
# /home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/python3 -u scripts/inference_local_hf.py \
#     --data-root ../data/babyvision_gen_data \
#     --jsonl ../data/babyvision_gen_data/meta_data.jsonl \
#     --output ./generated/instruct-pix2pix \
#     --rounds 3 \
#     --model-id "timbrooks/instruct-pix2pix"

# Step 2: Run Local Image Evaluation (compare generated vs ground truth)
echo "Starting local evaluation using Gemma 4..."
/home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/python3 -u scripts/evaluate_local_hf.py \
    --model-name "instruct-pix2pix" \
    --round "all" \
    --tasks-file ../data/babyvision_gen_data/meta_data.jsonl \
    --eval-model-id "google/gemma-4-E4B-it" \
    --data-root ../data/babyvision_gen_data

# Step 3: Summarize Results
echo "Summarizing results..."
/home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/python3 scripts/summarize_results.py \
    --tasks-file ../data/babyvision_gen_data/meta_data.jsonl

echo "=== Generation Evaluation Results ==="
cat results/summary.txt
echo "=========================="

echo "=== Slurm Job Completed ==="
