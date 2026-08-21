# BAGEL Model - Comparison Notes (deprecated)

> [!WARNING]
> **Deprecated.** This ran BAGEL through the text-answering understanding track, but the BabyVision paper's actual suggestion for BAGEL was the image-generation track (`babyvision_gen_eval/`) - see [README.md](./README.md) in this folder for why. Kept for the record, not part of the current results.

> [!TIP]
> **📊 [Interactive Results Dashboard](../../../_deprecated/index.html)** (archived, not part of the submission - see `results/final_report.md` instead): charts, filterable tables, and logs.

Ran **ByteDance-Seed/BAGEL-7B-MoT** through the BabyVision benchmark to see how it stacks up against Gemma 4, mostly out of curiosity about how a different vision-language architecture handles the same tasks.

---

## The numbers

* **BAGEL:** 4.12% (`0.0412 ± 0.0000`)
* **Gemma 4 baseline:** 12.97% (`0.1297 ± 0.0099`, 1024-token budget - see [final_report.md](../../../results/final_report.md))

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

On the 85 tasks where it *did* finish in time, it scored **18.8% (16/85)** - over 4x the 4.12% headline number, and closer to Gemma's ballpark. This is the same failure mode documented at length elsewhere in this project (see [final_report.md](../../../results/final_report.md#did-the-fix-actually-help)): capping generation too tight doesn't make a model dumber, it just stops it from finishing.

The clearest proof of that is what happened with Qwen. At a 512-token cap Qwen had an 81.4% no-answer rate and scored 2.84% - it looked dramatically worse than every Gemma variant. Bumping it to 1024 tokens dropped the no-answer rate to 1.8% and its score jumped to 13.32%, roughly tying my best Gemma run. Nothing about the model changed - it just finally had room to finish. BAGEL's truncation rate here (78%) is in that same range as Qwen's original 81.4%, so if the same relationship holds, its real score is likely being undersold by a similarly large margin.

**If I had more compute/time, this is the first thing I'd fix**: bump `max_think_token_n` well past 1024 and re-run. I didn't get to it mainly because of the wall-clock cost - BAGEL already needed the checkpoint-and-chain workaround below just to finish a single pass at the current (too-tight) budget, and raising the cap would only make each pass slower.

(Also: BAGEL was run greedy (`do_sample=False`), so all 3 passes were identical - hence `± 0.0000`.)

---

## Getting it to actually finish running

388 tasks × 3 passes at BAGEL's pace took ~2 hours once it was actually working, but getting there took several failed attempts first - crashes from a `transformers`/BAGEL code version mismatch, a CUDA out-of-memory error, and a `libcudart.so.12` driver mismatch on one node. None of those logs are informative beyond "it crashed," so I'm not listing each one.

Checkpointing raw outputs to disk every 5 tasks (so a job could resume where a previous one left off) is what eventually let it finish, across two jobs that made real progress:

| Job | Elapsed | Result | Logs |
| :--- | :---: | :--- | :---: |
| `16877328` | 49m50s | Got into pass 1 generation and built up a chunk of the checkpoint progress before being manually stopped | [Out](../../../logs/evaluation/bagel_eval_16877328.out) / [Err](../../../logs/evaluation/bagel_eval_16877328.err) |
| `16877352` | 1h59m52s | **The one that finished.** Resumed passes 1-2 from checkpoints (already complete, including the progress from `16877328`), pass 3 resumed from 235/388, generated the rest, then ran the full judging phase - this produced the final 4.12% score | [Out](../../../logs/evaluation/bagel_eval_16877352.out) / [Err](../../../logs/evaluation/bagel_eval_16877352.err) |

Both jobs finished well inside their 4-hour partition limit (`A100-4h`), so the checkpointing wasn't really needed to dodge a wall-clock cap here - `16877328` shows a Slurm state of `CANCELLED+` (manually stopped) rather than `TIMEOUT`, and there's no crash or error in its logs at the point it stopped. Most likely it was killed mid-debugging rather than by the scheduler. The checkpointing was genuinely useful, just for a different reason than I first assumed: it meant a manual restart (or one of the earlier environment-crash attempts) didn't throw away progress, not that a 4-hour cap was actually being hit.

(Corrected 2026-08-21: I'd previously written that `16877352` timed out mid-pass-3 and a later job finished the judging, and that the whole process was driven by a 4-hour wall-clock cap - checking the actual logs shows `16877352` completed everything itself in one run, and neither job it depended on actually hit that cap.)

---

## Raw data

* [score_summary.txt](./runs_bagel/score_summary.txt)
* Pass results: [1](./runs_bagel/model_results_run_1.json) / [2](./runs_bagel/model_results_run_2.json) / [3](./runs_bagel/model_results_run_3.json)
* Raw (pre-judge) results: [1](./runs_bagel/raw_results_run_1.json) / [2](./runs_bagel/raw_results_run_2.json) / [3](./runs_bagel/raw_results_run_3.json)
* [Setup logs](../../../logs/setup/) / [Sbatch script](./run_bagel_eval.sbatch)
