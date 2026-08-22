# Why these logs are here

Everything in this directory is a superseded, cancelled, or otherwise non-final SLURM job log, kept for the historical record but not part of the current results. File names keep their original job IDs (never renamed for cosmetic reasons - see the top-level `CLAUDE.md`), except where a handful of June logs were misfiled under `logs/evaluation/` with misleading names; those were moved here and given a clearer name that still preserves the original job ID.

- `bagel_eval_archived_*`, `gemma_generation_test_archived_*`, `gemma_system_prompt_rl_eval_archived_*`, `gemma_system_prompt_rl_training_archived_*` - earlier attempts/crashes superseded by the runs referenced in `results/final_report.md`.
- `gemma_rl_training_attempt_archived_16876847`, `gemma_rl_training_attempt_v2_archived_16876848` - early GRPO training attempts from June 19, only a handful of steps long. Originally misfiled under `logs/evaluation/` with "eval" in the name despite being training logs; superseded by the full training runs (`16875257`, `16877068`).
- `slurm_gemma_rl_correctness_weight1_maxtok512_eval_23604081`, `slurm_gemma_rl_correctness_weight2_maxtok512_eval_23604082`, `slurm_system_prompt_rl_maxtok512_eval_23604083` - the three LoRA-adapter eval jobs that silently scored a flat 0.00% due to the PEFT `device_map` bug (see `CLAUDE.md` finding #2). Superseded by the re-runs after the fix (`23657919`, `23657920`, `23657921`).
- `interrupted_runs/` - jobs that were cancelled or crashed mid-run before completing.
