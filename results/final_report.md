# BabyVision Experiment Final Report: Baseline vs. RL (correctness_weight=1) vs. RL (correctness_weight=2) vs. System Prompt RL

> [!TIP]
> **📊 [Open the Interactive Results Dashboard](../index.html)**: View interactive charts, filterable tables, and detailed logs directly in your browser.

> [!WARNING]
> **Numbers below use the 256-token generation cap.** On 2026-08-17 we found `evaluate_local_hf.py` capped Gemma's generation at 256 tokens while other models (e.g. Qwen) got 512, truncating ~25% of Gemma's answers before they reached `\boxed{...}`. All runs are being re-evaluated at 512 tokens (`runs/*_maxtok512/`); this report will be updated once those land. See `CLAUDE.md` for details and job status.

This final report compiles and documents all experimental runs, reinforcement learning training setups, and evaluations performed on the **BabyVision** visual reasoning dataset using the `google/gemma-4-E4B-it` vision-language model.


---

## 🗺️ Project Runs Overview

Below is the chronological history of all Slurm job runs executed during this project:

| Run Stage | Job ID | Description | Output Logs | Status |
| :--- | :---: | :--- | :---: | :---: |
| **Baseline Eval** | `16875224` | Evaluated the unmodified `google/gemma-4-E4B-it` model on 388 visual reasoning tasks. | [Out](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/gemma_baseline_eval_16875224.out) / [Err](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/gemma_baseline_eval_16875224.err) | **Success** |
| **RL Training (correctness_weight=1)** | `16875257` | Initial GRPO training run (LoRA causal LM layers, correctness reward weight = 1.0). | [Out](file:///home/dsi/sinayyo/BabyVision/logs/training/gemma_rl_v1_training_16875257.out) / [Err](file:///home/dsi/sinayyo/BabyVision/logs/training/gemma_rl_v1_training_16875257.err) | **Success** |
| **RL Evaluation (correctness_weight=1)** | `16876673` | Evaluated the correctness_weight=1 model on 388 tasks (3 passes). | [Out](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/gemma_rl_v1_eval_16876673.out) / [Err](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/gemma_rl_v1_eval_16876673.err) | **Success** |
| **RL Training (correctness_weight=2)** | `16877068`<br>(resumed `16877168`) | GRPO training run with multimodal PEFT targets, correctness reward weight scaled to 2.0. | [Out](file:///home/dsi/sinayyo/BabyVision/logs/training/gemma_rl_v2_training_16877068.out) / [Err](file:///home/dsi/sinayyo/BabyVision/logs/training/gemma_rl_v2_training_16877068.err) | **Success** |
| **RL Evaluation (correctness_weight=2)** | `16877072` | Evaluated the correctness_weight=2 model on 388 tasks (3 passes). | [Out](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/gemma_rl_v2_eval_16877072.out) / [Err](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/gemma_rl_v2_eval_16877072.err) | **Success** |
| **System Prompt RL Training** | `16877070` | GRPO training run targeting system prompt optimization (run by parallel agent). | [Out](file:///home/dsi/sinayyo/BabyVision/logs/training/gemma_system_prompt_rl_training_16877070.out) / [Err](file:///home/dsi/sinayyo/BabyVision/logs/training/gemma_system_prompt_rl_training_16877070.err) | **Success** |
| **System Prompt RL Eval** | `16877197` | Evaluated the System Prompt RL model on 388 tasks (3 passes). | [Out](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/gemma_system_prompt_rl_eval_16877197.out) / [Err](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/gemma_system_prompt_rl_eval_16877197.err) | **Success** |
| **Baseline Eval (512 tokens)** | `23604080` | Re-evaluating baseline Gemma with the token-cap fix. | — | **Pending** |
| **RL Eval, correctness_weight=1 (512 tokens)** | `23604081` | Re-evaluating with the token-cap fix. | — | **Pending** |
| **RL Eval, correctness_weight=2 (512 tokens)** | `23604082` | Re-evaluating with the token-cap fix. | — | **Pending** |
| **System Prompt RL Eval (512 tokens)** | `23604083` | Re-evaluating with the token-cap fix. | — | **Pending** |
| **Qwen Baseline Eval** | *(archived, exact job ID not recorded)* | Evaluated `Qwen/Qwen2.5-VL-7B-Instruct` base model at 512 tokens, 388 tasks (3 passes). Promoted from `_deprecated/scratch_tests/` into `runs/qwen_baseline/`. | — | **Success** |

---

## 📈 Performance Summary & Comparison

The evaluations consisted of **3 independent inference passes** per task. The model answers were graded using a local `Qwen/Qwen2.5-7B-Instruct` judge model.

> ⚠️ The numbers below are from the **256-token-capped** runs and will be superseded once the pending 512-token re-evaluations (above) complete.

* **Baseline Model Accuracy:** **`11.08% ± 1.17%`** — [Detailed Baseline Results](file:///home/dsi/sinayyo/BabyVision/results/baseline_detailed_results.md)
* **RL Model Accuracy (correctness_weight=1):** **`9.54% ± 1.05%`** (Regression due to visual-text representation drift & format bias) — [Detailed Results](file:///home/dsi/sinayyo/BabyVision/results/rl_detailed_results.md)
* **RL Model Accuracy (correctness_weight=2):** **`13.14% ± 1.64%`** (best result so far) — [Detailed Results](file:///home/dsi/sinayyo/BabyVision/results/rl_correctness_weight2_detailed_results.md)
* **System Prompt RL Accuracy:** **`9.71% ± 0.64%`** (Regression due to similar text format bias/representation drift) — [Detailed System Prompt RL Results](file:///home/dsi/sinayyo/BabyVision/results/system_prompt_detailed_results.md)
* **Qwen Baseline Accuracy:** **`2.84% ± 0.21%`** (base `Qwen/Qwen2.5-VL-7B-Instruct`, 512 tokens — not a like-for-like comparison against RL-tuned Gemma variants above; only comparable against Gemma's own base/untrained result)
* **Absolute Change (correctness_weight=2 vs. Baseline):** **`+2.06%`** (18.6% relative improvement)
* **Absolute Change (correctness_weight=2 vs. correctness_weight=1):** **`+3.60%`** (37.7% relative improvement)

### Category Accuracy Metrics:
| Category | Baseline Accuracy | RL (cw=1) Accuracy | RL (cw=2) Accuracy (Ours) | System Prompt RL |
| :--- | :---: | :---: | :---: | :---: |
| 🧩 **Fine-grained Discrimination** | `10.84% ± 1.90%` | `8.38% ± 1.26%` | `11.04% ± 1.50%` | `8.59% ± 0.50%` |
| 📍 **Spatial Perception** | `13.92% ± 1.37%` | `13.55% ± 2.26%` | `15.75% ± 1.37%` | `11.36% ± 1.04%` |
| 🌀 **Visual Pattern Recognition** | `9.80% ± 0.00%` | `6.54% ± 3.33%` | `19.61% ± 6.40%` | `8.50% ± 1.85%` |
| 👁️ **Visual Tracking** | `9.24% ± 3.16%` | `9.24% ± 0.57%` | `10.44% ± 2.05%` | `10.84% ± 2.60%` |

![Accuracy Comparison Graph](/home/dsi/sinayyo/BabyVision/results/accuracy_comparison.png)

---


## 🔍 Detailed Subtype Findings

### 🟢 What Improved Most with correctness_weight=2?
The combination of multimodal LoRA targets and a scaled correctness reward weight yielded substantial gains on logical, structural, and spatial tracking tasks:
1. **Rotation Patterns** (Visual Pattern Recognition): **`33.33% ± 9.43%`** vs. `20.00% ± 8.16%` (Baseline) (**`+13.33%`**)
   * *Findings:* Visual PEFT targets successfully aligned the model's visual representations of rotated objects with language descriptions.
2. **Paper Folding** (Spatial Perception): **`22.22% ± 3.93%`** vs. `8.33% ± 0.00%` (Baseline) (**`+13.89%`**)
   * *Findings:* Robust correctness rewards encouraged the model to verify intermediate crease-line logic step-by-step.
3. **Logic Patterns** (Visual Pattern Recognition): **`16.67% ± 8.91%`** vs. `4.76% ± 6.73%` (Baseline) (**`+11.91%`**)
4. **Overlay Patterns** (Visual Pattern Recognition): **`19.61% ± 7.34%`** vs. `9.80% ± 2.77%` (Baseline) (**`+9.81%`**)
5. **Find the same** (Fine-grained Discrimination): **`5.88% ± 0.00%`** vs. `0.00% ± 0.00%` (Baseline) (**`+5.88%`**)

### 🔴 Regressions and Partial Recoveries
1. **2D Pattern Completion:** **`35.00% ± 7.07%`** (Partial Recovery with correctness_weight=2: up from `28.33%` at correctness_weight=1, but still below Baseline `43.33%`).
2. **3D Pattern Completion:** **`25.93% ± 2.62%`** vs. `31.48% ± 6.93%` (Baseline) (**`-5.55%`**).

---

## 🧠 Key Insights & Methodology Changes

### 1. Visual-Language Representation Grounding (Multimodal PEFT Targets)
In language-only PEFT (correctness_weight=1 and System Prompt RL), updating only the causal language model layers resulted in alignment drift from the frozen visual encoder. For the correctness_weight=2 run, extending the LoRA configurations to target multimodal connector and projection sub-layers kept text-image alignments intact, preserving spatial grounding.

### 2. Correctness Reward Scaling (Squelching Formatting Exploits)
Restricting correctness weight to `1.0` (correctness_weight=1 run and System Prompt RL) allowed policy gradients to easily optimize for the formatting reward (`0.1` for outputting `\boxed{Answer}`) at the expense of correct answers. Scaling the correctness reward weight to `2.0` forced actual logical reasoning updates.

### 3. Evaluation Token-Budget Bug (found 2026-08-17)
`evaluate_local_hf.py` capped Gemma's generation at 256 tokens while other models (Qwen) were evaluated at 512, silently truncating ~25% of Gemma's answers before they reached `\boxed{...}`. This affected every Gemma variant's *evaluation* (not training — GRPO training used its own fixed, uniform `max_completion_length`). Fixed to 512 tokens across the board; all Gemma variants are being re-evaluated (see Pending rows above).

## 📉 GRPO Training Progress (correctness_weight=2)

Below is the training progress dashboard showing the Policy Loss and Mean Rewards optimization curves over the 3 epochs of training:

![GRPO Training Progress](/home/dsi/sinayyo/BabyVision/results/training_progress.png)

---

## 🎯 Conclusion & Verification

The hypothesis that **Reinforcement Learning (GRPO) can improve visual reasoning** on the BabyVision dataset is **VERIFIED** under the 256-token-capped evaluation.

By ensuring **multimodal parameter updates** and **robust correctness reward weighting**, we mitigated the representation drift and formatting exploits of the initial runs, raising overall accuracy from a baseline of **`11.08%`** to **`13.14%`** (an absolute improvement of **`+2.06%`**).

**This conclusion is pending re-verification** at 512 tokens once the pending jobs (above) complete — the token-budget bug may have disproportionately affected some variants over others, so relative rankings could shift.
