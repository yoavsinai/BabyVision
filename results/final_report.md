# BabyVision Experiments — Project Notes

> [!TIP]
> **📊 [Open the Interactive Results Dashboard](../index.html)**: charts, filterable tables, and logs.

## What this is

For my seminar, I've been experimenting on top of the [BabyVision benchmark](https://arxiv.org/pdf/2601.06521) — a visual reasoning benchmark of 388 puzzle-style tasks (things like finding the odd-one-out, solving mazes, folding paper, completing patterns). The original paper shows RL fine-tuning can improve a model's visual reasoning on this benchmark; my contribution is applying that same RL recipe to a model the paper didn't cover — **`google/gemma-4-E4B-it`** — and seeing whether the same approach helps there too.

I used `Qwen/Qwen2.5-7B-Instruct` as an LLM judge that grades whether the model's answer matches the ground truth. I also ran a couple of side comparisons: against a stock `Qwen/Qwen2.5-VL-7B-Instruct` (no training), and against ByteDance's `BAGEL-7B-MoT` (see [BAGEL_EVALUATION_REPORT.md](file:///home/dsi/sinayyo/BabyVision/BAGEL_EVALUATION_REPORT.md)).

This is a small-sample setup (388 tasks, 3 passes each) — good enough to get signal on what helps, not a rigorous claim about the state of the art.

## The story so far

**1. Baseline.** Ran stock Gemma with no training: **11.08% accuracy**.

**2. First RL attempt (GRPO, correctness reward weight = 1.0).** Only put LoRA adapters on the language-model layers. Accuracy went *down* to 9.54%. My read: with only the language layers being updated, the model's text output started drifting away from what the frozen vision encoder was actually seeing — plus the reward function made it too easy to get credit just for outputting the right `\boxed{...}` format without necessarily being correct.

**3. Second RL attempt (correctness reward weight = 2.0, multimodal LoRA).** Two changes: (a) extended the LoRA adapters to also cover the multimodal connector/projection layers, not just the language layers, and (b) doubled the weight on the correctness reward so formatting alone was no longer enough to score well. This got to **13.14% accuracy** — the best result so far, and a real improvement over baseline.

**4. Side experiment: system-prompt RL.** Instead of training the model to answer directly, I tried training it to *generate a system prompt* for itself, hoping it would learn to give itself better instructions. This underperformed baseline (9.71%) — same failure mode as attempt #2 (language-only PEFT).

**5. Caught a bug.** My teacher pointed out that Gemma scoring worse than Qwen in some comparisons looked suspicious — and it was. I found that the evaluation script (`evaluate_local_hf.py`) was capping Gemma's generation at 256 tokens while every other model got 512. Since Gemma tends to reason for a while before giving its final `\boxed{answer}`, this was silently truncating roughly a quarter of its answers before it ever reached the answer. I fixed the cap and I'm currently re-running all the evaluations above at 512 tokens to see how much this changes the picture.

## Results (⚠️ current numbers use the old 256-token cap — being re-run)

| Model | Accuracy |
| :--- | :---: |
| Baseline Gemma | 11.08% ± 1.17% |
| Gemma + RL (weight=1, language-only LoRA) | 9.54% ± 1.05% — regressed |
| Gemma + RL (weight=2, multimodal LoRA) | **13.14% ± 1.64%** — best so far |
| Gemma + system-prompt RL | 9.71% ± 0.64% — regressed |
| Qwen baseline (untrained) | 2.84% ± 0.21% — see note below |

**On the Qwen number:** it's not a fair comparison to the RL-tuned Gemma models above, since Qwen never went through any training — one model got extra help and the other didn't. The only comparison that's actually meaningful for "which base model is stronger" is base Gemma vs. base Qwen, same token budget, which is what I'm setting up next.

### By category

| Category | Baseline | RL (w=1) | RL (w=2) | System-prompt RL |
| :--- | :---: | :---: | :---: | :---: |
| Fine-grained Discrimination | 10.84% | 8.38% | 11.04% | 8.59% |
| Spatial Perception | 13.92% | 13.55% | 15.75% | 11.36% |
| Visual Pattern Recognition | 9.80% | 6.54% | 19.61% | 8.50% |
| Visual Tracking | 9.24% | 9.24% | 10.44% | 10.84% |

![Accuracy Comparison Graph](/home/dsi/sinayyo/BabyVision/results/accuracy_comparison.png)

The best run's biggest gain was in Visual Pattern Recognition (6.5% → 19.6%); its biggest regression was 3D Pattern Completion (31.5% baseline → 25.9%), which I haven't dug into yet.

## What I'm doing next

1. Re-running every variant above at 512 tokens (4 jobs currently in the queue) to get clean numbers that aren't distorted by the truncation bug.
2. Once that lands, doing an honest base-vs-base comparison against Qwen (same token budget, no training on either side) to answer the original "is Gemma actually worse than Qwen" question properly.
3. Considering RL-training a Qwen variant too, so I can compare trained-vs-trained rather than trained-Gemma-vs-untrained-Qwen — this needs real adaptation work (Qwen's LoRA target modules and chat template differ from Gemma's), so only worth it if there's still a meaningful gap after the token-cap fix.
4. Double-checking whether the RL *training* rollouts (separate 256-token completion cap during GRPO, not the eval bug above) were also getting truncated — if so, the reward signal itself may have been noisy.

---
<details>
<summary>Job IDs and raw logs (for reproducibility)</summary>

| Run | Job ID | Logs |
| :--- | :---: | :---: |
| Baseline eval | `16875224` | [Out](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/gemma_baseline_eval_16875224.out) / [Err](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/gemma_baseline_eval_16875224.err) |
| RL training, w=1 | `16875257` | [Out](file:///home/dsi/sinayyo/BabyVision/logs/training/gemma_rl_v1_training_16875257.out) / [Err](file:///home/dsi/sinayyo/BabyVision/logs/training/gemma_rl_v1_training_16875257.err) |
| RL eval, w=1 | `16876673` | [Out](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/gemma_rl_v1_eval_16876673.out) / [Err](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/gemma_rl_v1_eval_16876673.err) |
| RL training, w=2 | `16877068` (resumed `16877168`) | [Out](file:///home/dsi/sinayyo/BabyVision/logs/training/gemma_rl_v2_training_16877068.out) / [Err](file:///home/dsi/sinayyo/BabyVision/logs/training/gemma_rl_v2_training_16877068.err) |
| RL eval, w=2 | `16877072` | [Out](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/gemma_rl_v2_eval_16877072.out) / [Err](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/gemma_rl_v2_eval_16877072.err) |
| System-prompt RL training | `16877070` | [Out](file:///home/dsi/sinayyo/BabyVision/logs/training/gemma_system_prompt_rl_training_16877070.out) / [Err](file:///home/dsi/sinayyo/BabyVision/logs/training/gemma_system_prompt_rl_training_16877070.err) |
| System-prompt RL eval | `16877197` | [Out](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/gemma_system_prompt_rl_eval_16877197.out) / [Err](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/gemma_system_prompt_rl_eval_16877197.err) |
| Baseline eval, 512 tokens | `23604080` | pending |
| RL eval, w=1, 512 tokens | `23604081` | pending |
| RL eval, w=2, 512 tokens | `23604082` | pending |
| System-prompt RL eval, 512 tokens | `23604083` | pending |
| Qwen baseline eval | *(archived, no job ID kept)* | — |

</details>
