# BAGEL Model - Comparison Notes

> [!TIP]
> **📊 [Open the Interactive Results Dashboard](./index.html)**: charts, filterable tables, and logs.

Ran **ByteDance-Seed/BAGEL-7B-MoT** through the BabyVision benchmark to see how it stacks up against Gemma 4, mostly out of curiosity about how a different vision-language architecture handles the same tasks.

---

## The numbers

* **BAGEL:** 4.12% (`0.0412 ± 0.0000`)
* **Gemma 4 baseline:** 12.97% (`0.1297 ± 0.0099`, 1024-token budget - see [final_report.md](./results/final_report.md))

4.12% looks bad, but it's mostly an artifact, not a sign BAGEL is worse at visual reasoning - see below.

| Category | BAGEL (bfloat16, CoT) | Gemma 4 (baseline) |
| :--- | :---: | :---: |
| Fine-grained Discrimination | 4.91% | 11.04% |
| Spatial Perception | 2.20% | 15.75% |
| Visual Pattern Recognition | 5.88% | 15.03% |
| Visual Tracking | 3.61% | 12.45% |

Subtypes where BAGEL actually finished its answer: 2D Pattern Completion 15.00%, 3D Pattern Completion 11.11%, Find the Shadow 8.70%, Pattern and Color Completion 10.00%, Overlay Patterns 5.88%, Rotation Patterns 20.00%, Count Clusters 5.56%, Connect the Lines/Maze/Recognize Characters 4.3-5.2%. Everything else scored 0% because of token truncation (see below), not because the model got it wrong.

---

## Why the score is so low: token truncation, not bad reasoning

BAGEL has a very verbose internal "thinking" step before it answers, and the eval script capped that at `max_think_token_n=1024`. In **303 of 388 tasks (78%)**, BAGEL used up all 1024 tokens thinking and never got to write `\boxed{Answer}` - so it scored 0% on those by default, regardless of whether it was on the right track.

On the 85 tasks where it *did* finish in time, it scored **18.8% (16/85)** - over 4x the 4.12% headline number, and closer to Gemma's ballpark. This is the same failure mode documented at length elsewhere in this project (see [final_report.md](./results/final_report.md#did-the-fix-actually-help)): capping generation too tight doesn't make a model dumber, it just stops it from finishing.

The clearest proof of that is what happened with Qwen. At a 512-token cap Qwen had an 81.4% no-answer rate and scored 2.84% - it looked dramatically worse than every Gemma variant. Bumping it to 1024 tokens dropped the no-answer rate to 1.8% and its score jumped to 13.32%, roughly tying my best Gemma run. Nothing about the model changed - it just finally had room to finish. BAGEL's truncation rate here (78%) is in that same range as Qwen's original 81.4%, so if the same relationship holds, its real score is likely being undersold by a similarly large margin.

**If I had more compute/time, this is the first thing I'd fix**: bump `max_think_token_n` well past 1024 and re-run. I didn't get to it mainly because of the wall-clock cost - BAGEL already needed the checkpoint-and-chain workaround below just to finish a single pass at the current (too-tight) budget, and raising the cap would only make each pass slower.

(Also: BAGEL was run greedy (`do_sample=False`), so all 3 passes were identical - hence `± 0.0000`.)

---

## Getting it to actually finish running

388 tasks × 3 passes at BAGEL's pace took ~15.5 hours on an A100, but the cluster partition caps jobs at 4 hours. Worked around it by:
1. Checkpointing raw outputs to disk every 5 tasks, so a job could resume where it left off.
2. Chaining dependent Slurm jobs so each one picked up from the last checkpoint:
   - [bagel_eval_16877352](./logs/evaluation/bagel_eval_16877352.out) (passes 1-2, timed out mid-pass-3)
   - [bagel_eval_16877397](./logs/evaluation/bagel_eval_16877397.out) (resumed pass 3, ran judging, finished)

---

## Raw data

* [score_summary.txt](./babyvision_eval/runs/bagel/score_summary.txt)
* Pass results: [1](./babyvision_eval/runs/bagel/model_results_run_1.json) / [2](./babyvision_eval/runs/bagel/model_results_run_2.json) / [3](./babyvision_eval/runs/bagel/model_results_run_3.json)
* [Evaluation logs](./logs/evaluation/) / [Setup logs](./logs/setup/) / [Sbatch scripts](./sbatch_scripts/)
