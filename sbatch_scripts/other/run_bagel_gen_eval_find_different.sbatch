#!/bin/bash
#SBATCH --partition=A100-4h
#SBATCH --gres=gpu:1
#SBATCH --mem=64G
#SBATCH --time=01:30:00
#SBATCH --job-name=babyvision_bagel_gen_find_different
#SBATCH --output=slurm_bagel_gen_find_different_%j.out
#SBATCH --error=slurm_bagel_gen_find_different_%j.err

echo "=== Starting Slurm Job ==="
echo "Node: $SLURMD_NODENAME"
echo "Date: $(date)"

export CUDA_HOME=/usr/local/cuda
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/home/dsi/sinayyo/BabyVision/local_ollama/lib/ollama/cuda_v12:/usr/local/cuda/lib64:/home/dsi/sinayyo/.conda/envs/babyvision_py310/lib:$LD_LIBRARY_PATH

cd babyvision_gen_eval

# Targeted sample run: the 16 "Find the different" tasks - the subtype every
# prior model (Gemma baseline, both RL variants, system-prompt RL, Qwen) scored
# exactly 0% on in the understanding track. Picked deliberately, not the first
# N rows, to get signal on the case previous models struggled with most.
echo "Starting BAGEL image-editing inference (16-task Find-the-different sample, 1 round)..."
/home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/python3 -u scripts/inference_bagel.py \
    --data-root ../data/babyvision_gen_data \
    --jsonl ../data/babyvision_gen_data/meta_data_find_different.jsonl \
    --output ./generated/bagel_find_different \
    --rounds 1

echo "Starting local evaluation using Qwen2.5-VL..."
/home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/python3 -u scripts/evaluate_local_hf.py \
    --model-name "bagel_find_different" \
    --round "all" \
    --tasks-file ../data/babyvision_gen_data/meta_data_find_different.jsonl \
    --eval-model-id "Qwen/Qwen2.5-VL-7B-Instruct" \
    --data-root ../data/babyvision_gen_data

echo "Summarizing results..."
/home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/python3 scripts/summarize_results.py \
    --tasks-file ../data/babyvision_gen_data/meta_data_find_different.jsonl

echo "=== Generation Evaluation Results ==="
cat results/summary.txt

echo "=== Slurm Job Completed ==="
