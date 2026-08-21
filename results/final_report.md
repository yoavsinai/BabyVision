# BabyVision Experiments - Project Notes

> [!TIP]
> **📊 [Open the Interactive Results Dashboard](../index.html)**: charts, filterable tables, and logs.

## What this is

For my seminar, I've been experimenting on top of the [BabyVision benchmark](https://arxiv.org/pdf/2601.06521) - a visual reasoning benchmark of 388 puzzle-style tasks (things like finding the odd-one-out, solving mazes, folding paper, completing patterns). The original paper shows RL fine-tuning can improve a model's visual reasoning on this benchmark; my contribution is applying that same RL recipe to a model the paper didn't cover - **`google/gemma-4-E4B-it`** - and seeing whether the same approach helps there too.

I used `Qwen/Qwen2.5-7B-Instruct` as an LLM judge that grades whether the model's answer matches the ground truth. I also ran a couple of side comparisons: against a stock `Qwen/Qwen2.5-VL-7B-Instruct` (no training), and against ByteDance's `BAGEL-7B-MoT` (see [BAGEL_EVALUATION_REPORT.md](../BAGEL_EVALUATION_REPORT.md)).

This is a small-sample setup (388 tasks, 3 passes each) - good enough to get signal on what helps, not a rigorous claim about the state of the art.

## The story so far

**1. Baseline.** Ran stock Gemma with no training.

**2. First RL attempt (GRPO, correctness reward weight = 1.0).** Only put LoRA adapters on the language-model layers.

**3. Second RL attempt (correctness reward weight = 2.0, multimodal LoRA).** Two changes: (a) extended the LoRA adapters to also cover the multimodal connector/projection layers, not just the language layers, and (b) doubled the weight on the correctness reward so formatting alone was no longer enough to score well.

**4. Side experiment: system-prompt RL.** Instead of training the model to answer directly, I tried training it to *generate a system prompt* for itself, hoping it would learn to give itself better instructions.

**5. Caught a bug.** My supervisor told me the RL results looked odd, which sent me digging. Turned out the evaluation script (`evaluate_local_hf.py`) was capping Gemma's generation at 256 tokens while every other model got 512, silently truncating a chunk of its answers before they ever reached `\boxed{...}`. Fixed by making the cap 512 for everyone and re-ran every variant - every variant improved (see "Did the fix actually help?" below).

**6. Checked if 512 was actually enough - it wasn't, especially for Qwen.** I measured how often each model's answer was still getting cut off with no extractable answer at all, even at 512 tokens. Every model still had some truncation (10-22% for the Gemma variants), but **Qwen was at 81.4%** - it was barely ever finishing an answer. That meant the "Gemma clearly beats Qwen" comparison I'd been drawing was itself broken by the same bug, just worse. So I bumped everyone to 1024 tokens and re-ran again.

**Result: Qwen was never actually bad, it just never got to finish talking.** At 1024 tokens Qwen's no-answer rate dropped to 1.8% and its accuracy jumped from 2.84% to **13.32%** - roughly tied with my best Gemma RL run. The entire "Gemma beats Qwen" finding from earlier in this project was an artifact of an unfair token budget, not a real difference between the models. See the [dashboard](../index.html) and the table below for the full before/after picture.

## Results (1024 tokens - current best numbers)

| Model | Accuracy | No-answer rate |
| :--- | :---: | :---: |
| Baseline Gemma | 12.97% ± 0.99% | 6.4% |
| Gemma + RL (weight=1, language-only LoRA) | 11.34% ± 0.56% | 6.7% |
| Gemma + RL (weight=2, multimodal LoRA) | **13.75% ± 0.49%** - best | 0.5% |
| Gemma + system-prompt RL | 13.66% ± 0.56% | 8.0% |
| Qwen baseline (untrained) | 13.32% ± 0.44% | 1.8% |

A few things worth calling out:
- **RL (weight=2) and Qwen baseline are now essentially tied for best**, with system-prompt RL right behind. The gap between "best" and "worst" here (11.34% to 13.75%) is much smaller than it looked at 256 or even 512 tokens - a lot of what looked like meaningful differences between these runs was actually different sensitivity to token starvation, not different visual reasoning ability.
- **RL (weight=1) actually looks slightly worse at 1024 than at 512** (12.20% → 11.34%). I don't have a strong explanation for this - could be genuine noise given the small eval set (388 tasks, 3 passes), could be something about how that particular checkpoint behaves with more room to reason. Not chasing this further given the sample size, but flagging it rather than hiding it.
- **RL (weight=2) still has by far the lowest no-answer rate (0.5%)** of any variant, at every token budget I tried. That's consistent with the higher correctness-reward training actually teaching it to give a complete, concise answer rather than ramble - a real, repeatable effect, unlike some of the small accuracy differences above.
- **The Gemma-vs-Qwen comparison is now fair** (same 1024-token budget, neither trained): Gemma 12.97% vs. Qwen 13.32% - close enough that I wouldn't claim either is clearly better on this benchmark.

### By category

| Category | Baseline | RL (w=1) | RL (w=2) | System-prompt RL | Qwen |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Fine-grained Discrimination | 11.04% | 10.43% | 12.88% | 11.86% | 9.20% |
| Spatial Perception | 15.75% | 15.02% | 18.32% | 18.32% | 16.48% |
| Visual Pattern Recognition | 15.03% | 10.46% | 12.42% | 15.03% | **24.18%** |
| Visual Tracking | 12.45% | 9.64% | 11.24% | 11.24% | 11.24% |

![Accuracy Comparison Graph](./accuracy_comparison.png)

Qwen's Visual Pattern Recognition score (24.18%) stands out as the strongest single result in the whole comparison - worth a closer look if I revisit this.

The best Gemma run's (weight=2) biggest gain over baseline was 3D Pattern Completion (33.33% → 46.30%); its biggest regression was 3D Cube Unfold (5.56% → 0.00%).

Raw per-task data (what each model actually answered on every task, all 3 passes) is in `model_results_run_*.json` under each run's folder, e.g. [`babyvision_eval/runs/rl_correctness_weight2_maxtok1024/`](../babyvision_eval/runs/rl_correctness_weight2_maxtok1024/).

## Did the fix actually help?

Yes, clearly, at every step. Tracking accuracy and no-answer rate (proxy for truncation) across all three token budgets I tried:

| Model | Acc (256 tok) | Acc (512 tok) | Acc (1024 tok) | No-answer (256) | No-answer (512) | No-answer (1024) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Baseline Gemma | 11.08% | 12.03% | 12.97% | 24.7% | 14.9% | 6.4% |
| RL (weight=1) | 9.54% | 12.20% | 11.34% | 26.3% | 17.8% | 6.7% |
| RL (weight=2) | 13.14% | 13.66% | 13.75% | 1.8% | 1.0% | 0.5% |
| System-prompt RL | 9.71% | 10.48% | 13.66% | 36.9% | 21.6% | 8.0% |
| Qwen baseline | - | 2.84% | **13.32%** | - | 81.4% | 1.8% |

The pattern is consistent: raising the token budget lowers the no-answer rate, and accuracy tracks it almost every time. Qwen is the extreme case and the clearest proof this is a real, causal effect and not noise - going from 81.4% to 1.8% no-answer rate took its score from "looks much worse than every Gemma variant" to "roughly tied with the best one." The model wasn't getting smarter between 512 and 1024 tokens, it was just finally being given enough room to finish an answer it already knew.

**Same story likely applies to BAGEL.** I didn't get to re-run it with more headroom (see [BAGEL_EVALUATION_REPORT.md](../BAGEL_EVALUATION_REPORT.md)), but the pattern is identical: BAGEL's `max_think_token_n=1024` cap meant 78% of its answers were cut off mid-thought, and its accuracy on just the 22% that did finish was 18.8% - over 4x its reported 4.12% overall score. That's an even worse truncation rate than Qwen's original 81.4%, so if the same relationship holds, BAGEL's real score is likely being undersold by a lot more than its headline number suggests. If I had more GPU time (a single BAGEL pass already took ~15.5 hours against a 4-hour partition limit, worked around with checkpointing), raising that cap would be the first thing I'd try.

## What I'm doing next

1. Considering RL-training a Qwen variant too - now that the base-vs-base comparison is fair and close, it'd be interesting to see if the same RL recipe helps Qwen as much as it helped Gemma. Needs real adaptation work (Qwen's LoRA target modules and chat template differ from Gemma's).
2. Double-checking whether the RL *training* rollouts (separate 256-token completion cap during GRPO, not the eval bug above) were also getting truncated - if so, the reward signal itself may have been noisy.
3. Digging into the 3D Cube Unfold regression and Qwen's strong Visual Pattern Recognition result, if there's time.
4. If I get more compute, re-running BAGEL with a much higher `max_think_token_n` - the truncation evidence above suggests its real score could be substantially higher than 4.12%.

---
<details>
<summary>Job IDs and raw logs (for reproducibility)</summary>

| Run | Job ID | Logs |
| :--- | :---: | :---: |
| Baseline eval (256 tok, original) | `16875224` | [Out](../logs/evaluation/gemma_baseline_eval_16875224.out) / [Err](../logs/evaluation/gemma_baseline_eval_16875224.err) |
| RL training, w=1 | `16875257` | [Out](../logs/training/gemma_rl_v1_training_16875257.out) / [Err](../logs/training/gemma_rl_v1_training_16875257.err) |
| RL eval, w=1 (256 tok, original) | `16876673` | [Out](../logs/evaluation/gemma_rl_v1_eval_16876673.out) / [Err](../logs/evaluation/gemma_rl_v1_eval_16876673.err) |
| RL training, w=2 | `16877068` (resumed `16877168`) | [Out](../logs/training/gemma_rl_v2_training_16877068.out) / [Err](../logs/training/gemma_rl_v2_training_16877068.err) |
| RL eval, w=2 (256 tok, original) | `16877072` | [Out](../logs/evaluation/gemma_rl_v2_eval_16877072.out) / [Err](../logs/evaluation/gemma_rl_v2_eval_16877072.err) |
| System-prompt RL training | `16877070` | [Out](../logs/training/gemma_system_prompt_rl_training_16877070.out) / [Err](../logs/training/gemma_system_prompt_rl_training_16877070.err) |
| System-prompt RL eval (256 tok, original) | `16877197` | [Out](../logs/evaluation/gemma_system_prompt_rl_eval_16877197.out) / [Err](../logs/evaluation/gemma_system_prompt_rl_eval_16877197.err) |
| Baseline eval, 512 tokens | `23604080` | [Out](../logs/evaluation/slurm_gemma_23604080.out) / [Err](../logs/evaluation/slurm_gemma_23604080.err) |
| RL eval, w=1, 512 tokens | `23657919` | [Out](../logs/evaluation/slurm_gemma_rl_correctness_weight1_maxtok512_eval_23657919.out) / [Err](../logs/evaluation/slurm_gemma_rl_correctness_weight1_maxtok512_eval_23657919.err) |
| RL eval, w=2, 512 tokens | `23657920` | [Out](../logs/evaluation/slurm_gemma_rl_correctness_weight2_maxtok512_eval_23657920.out) / [Err](../logs/evaluation/slurm_gemma_rl_correctness_weight2_maxtok512_eval_23657920.err) |
| System-prompt RL eval, 512 tokens | `23657921` | [Out](../logs/evaluation/slurm_system_prompt_rl_maxtok512_eval_23657921.out) / [Err](../logs/evaluation/slurm_system_prompt_rl_maxtok512_eval_23657921.err) |
| Qwen baseline eval, 512 tokens | *(archived, no job ID kept)* | - |
| Baseline eval, 1024 tokens | `23671051` | [Out](../logs/evaluation/slurm_gemma_23671051.out) / [Err](../logs/evaluation/slurm_gemma_23671051.err) |
| RL eval, w=1, 1024 tokens | `23671052` | [Out](../logs/evaluation/slurm_gemma_rl_correctness_weight1_maxtok1024_eval_23671052.out) / [Err](../logs/evaluation/slurm_gemma_rl_correctness_weight1_maxtok1024_eval_23671052.err) |
| RL eval, w=2, 1024 tokens | `23671053` | [Out](../logs/evaluation/slurm_gemma_rl_correctness_weight2_maxtok1024_eval_23671053.out) / [Err](../logs/evaluation/slurm_gemma_rl_correctness_weight2_maxtok1024_eval_23671053.err) |
| System-prompt RL eval, 1024 tokens | `23671054` | [Out](../logs/evaluation/slurm_system_prompt_rl_maxtok1024_eval_23671054.out) / [Err](../logs/evaluation/slurm_system_prompt_rl_maxtok1024_eval_23671054.err) |
| Qwen baseline eval, 1024 tokens | `23671055` | [Out](../logs/evaluation/slurm_hf_maxtok1024_23671055.out) / [Err](../logs/evaluation/slurm_hf_maxtok1024_23671055.err) |

</details>
