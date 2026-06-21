#!/bin/bash
#SBATCH --partition=L4-12h
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=2:00:00
#SBATCH --job-name=install_flash_attn_v3
#SBATCH --output=install_flash_attn_v3_%j.out
#SBATCH --error=install_flash_attn_v3_%j.err

echo "=== Starting flash-attn Installation v3 ==="
echo "Node: $SLURMD_NODENAME"
echo "Date: $(date)"
echo "CPUs allocated: $SLURM_CPUS_PER_TASK"

# Export CUDA environment variables
export CUDA_HOME=/usr/local/cuda
export PATH=/usr/local/cuda/bin:$PATH

# Optimize compilation speed
export FLASH_ATTN_CUDA_ARCHS="80;89"
export TORCH_CUDA_ARCH_LIST="8.0;8.9"
export MAX_JOBS=8

echo "Using nvcc:"
which nvcc
nvcc --version

# Run pip install flash-attn with verbose option
/home/dsi/sinayyo/.conda/envs/babyvision_py310/bin/pip install flash-attn --no-build-isolation -v

echo "=== Installation Completed ==="
