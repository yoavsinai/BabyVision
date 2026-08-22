# Why these logs are here

Evaluation runs. As in `../training/`, `v1`/`v2` in `gemma_rl_v1_eval_*`/`gemma_rl_v2_eval_*` names the correctness-reward-weight variant being evaluated, not a version number - see `CLAUDE.md`'s naming-conventions note.

- `gemma_baseline_eval_16875224`: Configuration A (untrained Gemma), original 256-token run.
- `gemma_rl_v1_eval_16876673`: Configuration B (correctness_weight=1.0) eval, original 256-token run.
- `gemma_rl_v2_eval_16877072`: Configuration C (correctness_weight=2.0) eval, original 256-token run.
- `gemma_system_prompt_rl_eval_16877197`: Configuration D eval, original 256-token run.
- `bagel_eval_16877328`, `bagel_eval_16877352`: BAGEL evaluated on the (later deprecated) text-answering understanding track - see `babyvision_eval/_deprecated/bagel_understanding_track/README.md`.
- `slurm_gemma_*`, `slurm_gemma_rl_correctness_weight{1,2}_maxtok{512,1024}_eval_*`, `slurm_system_prompt_rl_maxtok{512,1024}_eval_*`, `slurm_hf_maxtok{512,1024}_*`: the post-reorg 512- and 1024-token re-evaluations referenced by job ID in `results/final_report.md`'s Appendix A. These use the full descriptive names (`correctness_weight1`/`correctness_weight2`) rather than `v1`/`v2`.
- `slurm_bagel_gen_find_different_23820802`: the targeted BAGEL generation-track test on the "Find the different" subtype.

Superseded/failed runs (early duplicate training attempts mislabeled as "eval", a cancelled eval-resume job, and the three jobs that silently scored 0.00% due to the PEFT `device_map` bug) have been moved to `../archive/` - see `../archive/README.md`.
