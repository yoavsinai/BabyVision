#!/bin/bash
#SBATCH --partition=L4-4h
#SBATCH --gres=gpu:1
#SBATCH --mem=32G
#SBATCH --time=4:00:00
#SBATCH --job-name=babyvision_eval
#SBATCH --output=slurm_eval_%j.out
#SBATCH --error=slurm_eval_%j.err

echo "=== Starting Slurm Job ==="
echo "Node: $SLURMD_NODENAME"
echo "Date: $(date)"

# Clean up any existing ollama server running on this host
pkill ollama || true
sleep 2

# Start local Ollama server
export OLLAMA_HOST=127.0.0.1:11434
export OLLAMA_MODELS=/home/dsi/sinayyo/.ollama/models

echo "Starting local Ollama server..."
./local_ollama/bin/ollama serve > local_ollama/ollama_serve_gpu.log 2>&1 &
SERVE_PID=$!

# Wait for Ollama server to start and load
sleep 8

# List loaded models
echo "Listing local Ollama models:"
./local_ollama/bin/ollama list

echo "Running MLLM evaluation on local GPU..."
cd babyvision_eval

# Run the python evaluation script on the full benchmark
../.venv/bin/python3 evaluate_model.py \
    --model-api-key "mock-key" \
    --model-base-url "http://127.0.0.1:11434/v1" \
    --model-name "llama3.2-vision" \
    --judge-api-key "mock-key" \
    --judge-base-url "http://127.0.0.1:11434/v1" \
    --judge-model-name "llama3.2" \
    --test-json-path "../data/babyvision_data/meta_data.jsonl" \
    --output-dir "./results_local" \
    --num-processes 4 \
    --num-passes 3

echo "Computing final score summary..."
../.venv/bin/python3 compute_score.py results_local/model_results_run_*.json > results_local/score_summary.txt

echo "=== Evaluation Results ==="
cat results_local/score_summary.txt
echo "=========================="

# Stop the Ollama server
kill $SERVE_PID
echo "=== Slurm Job Completed ==="
