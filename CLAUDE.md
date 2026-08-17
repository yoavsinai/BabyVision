# BabyVision — Project State

This file tracks project state, conventions, and open threads across sessions. Update it at the end of each session that changes structure, finds something non-obvious, or leaves work in flight.

## What this project is

Evaluating and RL-fine-tuning `google/gemma-4-E4B-it` (and comparing against `Qwen/Qwen2.5-VL-7B-Instruct`) on the BabyVision visual reasoning benchmark (`data/babyvision_data/meta_data.jsonl`, 388 tasks). Answers are extracted via `\boxed{...}` and graded by an LLM judge (`Qwen/Qwen2.5-7B-Instruct`).

## Directory layout (as of 2026-08-17 reorg)

```
babyvision_eval/
  evaluate_local_hf.py, evaluate_bagel.py, evaluate_system_prompt.py, evaluate_model.py
  rl_train_gemma4.py                       # RL training, correctness_weight=1.0 (original)
  rl_train_gemma4_correctness_weight2.py   # RL training, correctness_weight=2.0 + multimodal LoRA targets
  rl_train_system_prompt.py                # RL training a system-prompt-generating policy
  compute_score.py, utils.py
  runs/            # evaluation outputs (raw + scored results per model variant)
    baseline/                          # Gemma base, 256-token cap (buggy, see below)
    baseline_maxtok512/                # Gemma base, 512-token cap (fixed) — IN PROGRESS
    rl_correctness_weight1/            # 256-token cap
    rl_correctness_weight1_maxtok512/  # IN PROGRESS
    rl_correctness_weight2/            # 256-token cap
    rl_correctness_weight2_maxtok512/  # IN PROGRESS
    system_prompt_rl/                  # 256-token cap
    system_prompt_rl_maxtok512/        # IN PROGRESS
    qwen_baseline/                     # Qwen2.5-VL-7B base, 512 tokens, 2.84% acc — promoted from _deprecated
    bagel/
  checkpoints/     # gitignored LoRA output dirs (multi-GB)
    rl_correctness_weight1/, rl_correctness_weight2/, system_prompt_rl/
  _deprecated/     # stale/orphaned runs kept for history, not part of the official comparison
    early_orphan_run/, scratch_tests/

sbatch_scripts/
  training/        # run_gemma_rl.sbatch, run_gemma_rl_correctness_weight2.sbatch, run_system_prompt_rl.sbatch
  evaluation/       # one script per runs/ variant above, plus run_hf_eval.sbatch (Qwen), run_bagel_eval.sbatch
  other/           # run_local_eval.sbatch (Ollama), run_local_gen_eval.sbatch (image-gen eval, unrelated track)

logs/
  training/, evaluation/, setup/, archive/   # historical SLURM job stdout/err, named by real job ID — never rename these, they're the audit trail

results/           # top-level copies of detailed_results.md + final_report.md + charts, referenced by index.html dashboard
```

## Naming conventions

- Directories/files are named for **what changed**, not a version number. E.g. `rl_correctness_weight2` (not `rl_v2`) because the actual change was the correctness reward weight going from 1.0 → 2.0. `_maxtok512` suffix means "re-evaluated with the token-budget fix applied."
- Do not introduce bare `v1`/`v2` version suffixes — always name the parameter/change that differs.
- `logs/` historical SLURM output files keep their original names (including any old `v2` naming) since they're tied to real job IDs — cosmetic renames there would falsify the record.

## Key finding: the 256-vs-512 token cap bug (found 2026-08-17)

`evaluate_local_hf.py` had `max_tokens = 256 if "gemma" in model_id.lower() else 512` — Gemma was evaluated with **half** the generation budget of every other model (including Qwen), causing ~25% of Gemma's answers to be truncated before reaching the closing `\boxed{...}` (verified: unterminated `\boxed{` in raw outputs). `evaluate_system_prompt.py` had the same 256-token cap on its answer-generation step (not model-conditional there, but still too tight).

**Fixed**: both scripts now use `max_new_tokens=512` unconditionally. All old 256-token `runs/*` results are being re-evaluated at 512 tokens in parallel dirs suffixed `_maxtok512`.

Note: this bug only affected **evaluation**, not RL **training** — `rl_train_gemma4*.py` use `max_completion_length=256` (128 for system-prompt) uniformly for all training rollouts; that's a deliberate training-efficiency budget, not an asymmetry bug. Not yet checked how often training rollouts hit that cap — worth investigating if training quality is ever in question.

## Known confound to keep in mind

Comparing **RL-trained Gemma** against **base/untrained Qwen** is apples-to-oranges (one model got extra training). The only fair "which base model is better" comparison is base Gemma vs. base Qwen, same token budget — that's `runs/baseline_maxtok512/` vs `runs/qwen_baseline/` once the former lands. RL-tuned Gemma results should be presented as "Gemma + our RL" and not implicitly compared to untrained Qwen.

## Session log

### 2026-08-17
- Diagnosed and fixed the 256/512 token cap bug (`evaluate_local_hf.py:152`, `evaluate_system_prompt.py`).
- Reorganized `babyvision_eval/` (`runs/`, `checkpoints/`, `_deprecated/`) and `sbatch_scripts/` (`training/`, `evaluation/`, `other/`); updated all internal path references, `index.html`/`results_dashboard.html` dashboard links, and `results/*.md`.
- Renamed `rl_v2` → `rl_correctness_weight2` throughout (scripts, checkpoints, results, docs) to name the actual parameter change instead of a version number.
- Promoted archived Qwen base results (`_deprecated/scratch_tests/results_local_hf`) to `runs/qwen_baseline/` — full 388-task run, 3 passes, already at 512 tokens. Result: **2.84% ± 0.21%** accuracy.
- Submitted 4 SLURM jobs (23604080–23604083) re-evaluating all Gemma variants (baseline, correctness_weight1, correctness_weight2, system_prompt_rl) at 512 tokens. **Status: pending/running, results not yet in.**
- Next planned step once those land: compile an updated `final_report.md` comparing all Gemma variants + Qwen base on equal footing (512 tokens), then decide whether to also RL-train a Qwen variant for a true trained-vs-trained comparison (would require nontrivial adaptation of `rl_train_gemma4_correctness_weight2.py` — different LoRA target modules, chat template, etc. for Qwen2.5-VL).
- Nothing committed to git yet this session — working tree has the reorg + bugfix uncommitted.
