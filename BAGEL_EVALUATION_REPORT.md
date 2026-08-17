# BAGEL Model - Comparison Notes

> [!TIP]
> **📊 [Open the Interactive Results Dashboard](./index.html)**: charts, filterable tables, and logs.

Ran **ByteDance-Seed/BAGEL-7B-MoT** through the BabyVision benchmark to see how it stacks up against Gemma 4, mostly out of curiosity about how a different vision-language architecture handles the same tasks.

---

## The numbers

* **BAGEL:** 4.12% (`0.0412 ± 0.0000`)
* **Gemma 4 baseline:** 11.08% (`0.1108 ± 0.0117`)

4.12% looks bad, but it's mostly an artifact, not a sign BAGEL is worse at visual reasoning - see below.

| Category | BAGEL (bfloat16, CoT) | Gemma 4 (baseline) |
| :--- | :---: | :---: |
| Fine-grained Discrimination | 4.91% | 10.84% |
| Spatial Perception | 2.20% | 13.92% |
| Visual Pattern Recognition | 5.88% | 9.80% |
| Visual Tracking | 3.61% | 9.24% |

Subtypes where BAGEL actually finished its answer: 2D Pattern Completion 15.00%, 3D Pattern Completion 11.11%, Find the Shadow 8.70%, Pattern and Color Completion 10.00%, Overlay Patterns 5.88%, Rotation Patterns 20.00%, Count Clusters 5.56%, Connect the Lines/Maze/Recognize Characters 4.3-5.2%. Everything else scored 0% because of token truncation (see below), not because the model got it wrong.

---

## Why the score is so low: token truncation, not bad reasoning

BAGEL has a very verbose internal "thinking" step before it answers, and the eval script capped that at `max_think_token_n=1024`. In **303 of 388 tasks (78%)**, BAGEL used up all 1024 tokens thinking and never got to write `\boxed{Answer}` - so it scored 0% on those by default, regardless of whether it was on the right track.

On the 85 tasks where it *did* finish in time, it scored **18.8% (16/85)** - closer to Gemma's ballpark, and suggests the low headline number is mostly a token-budget problem, similar in spirit to the Gemma 256-vs-512 bug elsewhere in this project. Worth trying with a higher `max_think_token_n` if I come back to this.

(Also: BAGEL was run greedy (`do_sample=False`), so all 3 passes were identical - hence `± 0.0000`.)

---

## Getting it to actually finish running

388 tasks × 3 passes at BAGEL's pace took ~15.5 hours on an A100, but the cluster partition caps jobs at 4 hours. Worked around it by:
1. Checkpointing raw outputs to disk every 5 tasks, so a job could resume where it left off.
2. Chaining dependent Slurm jobs so each one picked up from the last checkpoint:
   - [bagel_eval_16877352](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/bagel_eval_16877352.out) (passes 1-2, timed out mid-pass-3)
   - [bagel_eval_16877397](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/bagel_eval_16877397.out) (resumed pass 3, ran judging, finished)

---

## Raw data

* [score_summary.txt](file:///home/dsi/sinayyo/BabyVision/babyvision_eval/runs/bagel/score_summary.txt)
* Pass results: [1](file:///home/dsi/sinayyo/BabyVision/babyvision_eval/runs/bagel/model_results_run_1.json) / [2](file:///home/dsi/sinayyo/BabyVision/babyvision_eval/runs/bagel/model_results_run_2.json) / [3](file:///home/dsi/sinayyo/BabyVision/babyvision_eval/runs/bagel/model_results_run_3.json)
* [Evaluation logs](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/) / [Setup logs](file:///home/dsi/sinayyo/BabyVision/logs/setup/) / [Sbatch scripts](file:///home/dsi/sinayyo/BabyVision/sbatch_scripts/)
