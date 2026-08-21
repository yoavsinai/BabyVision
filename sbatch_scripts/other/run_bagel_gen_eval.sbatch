#!/bin/bash
#SBATCH --partition=A100-4h
#SBATCH --gres=gpu:1
#SBATCH --mem=64G
#SBATCH --time=04:00:00
#SBATCH --job-name=babyvision_bagel_gen_eval
#SBATCH --output=slurm_bagel_gen_%j.out
#SBATCH --error=slurm_bagel_gen_%j.err

echo "=== Starting Slurm Job ==="
echo "Node: $SLURMD_NODENAME"
echo "Date: $(date)"

export CUDA_HOME=/usr/local/cuda
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/home/dsi/sinayyo/BabyVision/local_ollama/lib/ollama/cuda_v12:/usr/local/cuda/lib64:/home/dsi/sinayyo/.conda/envs/babyvision_py310/lib:$LD_LIBRARY_PATH

cd babyvision_gen_eval

# Step 1: BAGEL native image-editing inference (3 rounds)
echo "Starting BAGEL image-editing inference..."
/home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/python3 -u scripts/inference_bagel.py \
    --data-root ../data/babyvision_gen_data \
    --jsonl ../data/babyvision_gen_data/meta_data.jsonl \
    --output ./generated/bagel \
    --rounds 3

# Step 2: Judge generated images against ground truth (local Qwen2.5-VL, no API key needed)
echo "Starting local evaluation using Qwen2.5-VL..."
/home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/python3 -u scripts/evaluate_local_hf.py \
    --model-name "bagel" \
    --round "all" \
    --tasks-file ../data/babyvision_gen_data/meta_data.jsonl \
    --eval-model-id "Qwen/Qwen2.5-VL-7B-Instruct" \
    --data-root ../data/babyvision_gen_data

# Step 3: Summarize results
echo "Summarizing results..."
/home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/python3 scripts/summarize_results.py \
    --tasks-file ../data/babyvision_gen_data/meta_data.jsonl

echo "=== Generation Evaluation Results ==="
cat results/summary.txt

echo "=== Slurm Job Completed ==="
