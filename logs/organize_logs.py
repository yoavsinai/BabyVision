import os
import shutil

def main():
    root_dir = '/home/dsi/sinayyo/BabyVision'
    os.chdir(root_dir)
    
    # Create target directories
    os.makedirs('logs/training', exist_ok=True)
    os.makedirs('logs/evaluation', exist_ok=True)
    os.makedirs('logs/archive', exist_ok=True)
    os.makedirs('logs/archive/interrupted_runs', exist_ok=True)

    # 1. Map of specific active logs to move and rename to descriptive names
    active_moves = {
        # Gemma V1
        'results/logs/baseline_evaluation_16875224.out': 'logs/evaluation/gemma_baseline_eval_16875224.out',
        'results/logs/baseline_evaluation_16875224.err': 'logs/evaluation/gemma_baseline_eval_16875224.err',
        'results/logs/rl_training_16875257.out': 'logs/training/gemma_rl_v1_training_16875257.out',
        'results/logs/rl_training_16875257.err': 'logs/training/gemma_rl_v1_training_16875257.err',
        'results/logs/rl_evaluation_16876673.out': 'logs/evaluation/gemma_rl_v1_eval_16876673.out',
        'results/logs/rl_evaluation_16876673.err': 'logs/evaluation/gemma_rl_v1_eval_16876673.err',

        # Gemma V2
        'results/logs/slurm_gemma_rl_v2_16877068.out': 'logs/training/gemma_rl_v2_training_16877068.out',
        'results/logs/slurm_gemma_rl_v2_16877068.err': 'logs/training/gemma_rl_v2_training_16877068.err',
        'results/logs/slurm_gemma_rl_v2_16877168.out': 'logs/training/gemma_rl_v2_training_resume_16877168.out',
        'results/logs/slurm_gemma_rl_v2_16877168.err': 'logs/training/gemma_rl_v2_training_resume_16877168.err',
        'results/logs/slurm_gemma_rl_v2_eval_16877072.out': 'logs/evaluation/gemma_rl_v2_eval_16877072.out',
        'results/logs/slurm_gemma_rl_v2_eval_16877072.err': 'logs/evaluation/gemma_rl_v2_eval_16877072.err',
        'results/logs/slurm_gemma_rl_v2_eval_16877169.out': 'logs/evaluation/gemma_rl_v2_eval_resume_16877169.out',
        'results/logs/slurm_gemma_rl_v2_eval_16877169.err': 'logs/evaluation/gemma_rl_v2_eval_resume_16877169.err',

        # Gemma System Prompt RL
        'results/logs/archive/slurm_system_prompt_rl_16877070.out': 'logs/training/gemma_system_prompt_rl_training_16877070.out',
        'results/logs/archive/slurm_system_prompt_rl_16877070.err': 'logs/training/gemma_system_prompt_rl_training_16877070.err',
        'results/logs/archive/slurm_system_prompt_eval_16877197.out': 'logs/evaluation/gemma_system_prompt_rl_eval_16877197.out',
        'results/logs/archive/slurm_system_prompt_eval_16877197.err': 'logs/evaluation/gemma_system_prompt_rl_eval_16877197.err',
    }

    # Perform active moves
    for src, dst in active_moves.items():
        if os.path.exists(src):
            print(f"Moving & Renaming: {src} -> {dst}")
            shutil.move(src, dst)

    # 2. Move remaining archived files from results/logs/archive/ to logs/archive/
    archive_src = 'results/logs/archive'
    if os.path.exists(archive_src):
        for item in os.listdir(archive_src):
            src_path = os.path.join(archive_src, item)
            if os.path.isfile(src_path):
                # Clean name if possible
                new_name = item
                if item.startswith('slurm_system_prompt_rl_'):
                    new_name = f"gemma_system_prompt_rl_training_archived_{item.split('_')[-1]}"
                elif item.startswith('slurm_system_prompt_eval_'):
                    new_name = f"gemma_system_prompt_rl_eval_archived_{item.split('_')[-1]}"
                elif item.startswith('slurm_gen_'):
                    new_name = f"gemma_generation_test_archived_{item.split('_')[-1]}"
                
                dst_path = os.path.join('logs/archive', new_name)
                print(f"Archiving: {src_path} -> {dst_path}")
                shutil.move(src_path, dst_path)

    # 3. Move interrupted files from results/logs/interrupted_runs/ to logs/archive/interrupted_runs/
    interrupted_src = 'results/logs/interrupted_runs'
    if os.path.exists(interrupted_src):
        for item in os.listdir(interrupted_src):
            src_path = os.path.join(interrupted_src, item)
            if os.path.isfile(src_path):
                dst_path = os.path.join('logs/archive/interrupted_runs', item)
                print(f"Archiving Interrupted: {src_path} -> {dst_path}")
                shutil.move(src_path, dst_path)

    # 4. Clean up results/logs directory if it is empty
    if os.path.exists('results/logs'):
        # Recursively remove results/logs
        try:
            shutil.rmtree('results/logs')
            print("Successfully deleted old results/logs directory.")
        except Exception as e:
            print(f"Error deleting results/logs directory: {e}")

    print("Log organization completed successfully!")

if __name__ == '__main__':
    main()
