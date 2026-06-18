# BabyVision Experiment Final Report: Baseline vs. RL (GRPO) Fine-Tuning

This final report compiles and documents all experimental runs, reinforcement learning training setups, and evaluations performed on the **BabyVision** visual reasoning dataset using the `google/gemma-4-E4B-it` vision-language model.

---

## 🗺️ Project Runs Overview

Below is the chronological history of all Slurm job runs executed during this project:

| Run Stage | Job ID | Description | Output Logs | Status |
| :--- | :---: | :--- | :---: | :---: |
| **Baseline Eval** | `16875224` | Evaluated the unmodified `google/gemma-4-E4B-it` model on 388 visual reasoning tasks. | [Out](file:///home/dsi/sinayyo/BabyVision/results/logs/baseline_evaluation_16875224.out) / [Err](file:///home/dsi/sinayyo/BabyVision/results/logs/baseline_evaluation_16875224.err) | **Success** |
| **RL Training** | `16875234` | GRPO training trial. Aborted early/interrupted. | [Out](file:///home/dsi/sinayyo/BabyVision/results/logs/interrupted_runs/rl_training_failed_16875234.out) / [Err](file:///home/dsi/sinayyo/BabyVision/results/logs/interrupted_runs/rl_training_failed_16875234.err) | *Interrupted* |
| **RL Training** | `16875246` | GRPO training trial. Target module configuration fixes. | [Out](file:///home/dsi/sinayyo/BabyVision/results/logs/interrupted_runs/rl_training_failed_16875246.out) / [Err](file:///home/dsi/sinayyo/BabyVision/results/logs/interrupted_runs/rl_training_failed_16875246.err) | *Interrupted* |
| **RL Training** | `16875248` | GRPO training trial. Adjusted adapter modules for Gemma 4 sub-layers. | [Out](file:///home/dsi/sinayyo/BabyVision/results/logs/interrupted_runs/rl_training_failed_16875248.out) / [Err](file:///home/dsi/sinayyo/BabyVision/results/logs/interrupted_runs/rl_training_failed_16875248.err) | *Interrupted* |
| **RL Training** | `16875257` | Final successful GRPO training run. LoRA weights saved. | [Out](file:///home/dsi/sinayyo/BabyVision/results/logs/rl_training_16875257.out) / [Err](file:///home/dsi/sinayyo/BabyVision/results/logs/rl_training_16875257.err) | **Success** |
| **RL Evaluation** | `16876673` | Evaluated the RL fine-tuned model (LoRA adapter) on 388 tasks. | [Out](file:///home/dsi/sinayyo/BabyVision/results/logs/rl_evaluation_16876673.out) / [Err](file:///home/dsi/sinayyo/BabyVision/results/logs/rl_evaluation_16876673.err) | **Success** |

---

## 📈 Performance Summary & Comparison

The evaluation consisted of **3 independent inference passes** per task. The model answers were graded using a local `Qwen/Qwen2.5-7B-Instruct` judge model.

* **Baseline Model Accuracy:** **`0.1108 ± 0.0117`** (11.08%) — [Detailed Baseline Results](file:///home/dsi/sinayyo/BabyVision/results/baseline_detailed_results.md)
* **RL Fine-Tuned Model Accuracy:** **`0.0954 ± 0.0105`** (9.54%) — [Detailed RL Results](file:///home/dsi/sinayyo/BabyVision/results/rl_detailed_results.md)
* **Absolute Change:** **`-1.54%`** 

### Category Accuracy Metrics:
| Category | Baseline Accuracy | RL Fine-Tuned (GRPO) | Difference |
| :--- | :---: | :---: | :---: |
| 🧩 **Fine-grained Discrimination** | `0.1084 ± 0.0190` | `0.0838 ± 0.0126` | `-0.0246` (-2.46%) |
| 📍 **Spatial Perception** | `0.1392 ± 0.0137` | `0.1355 ± 0.0226` | `-0.0037` (-0.37%) |
| 🌀 **Visual Pattern Recognition** | `0.0980 ± 0.0000` | `0.0654 ± 0.0333` | `-0.0326` (-3.26%) |
| 👁️ **Visual Tracking** | `0.0924 ± 0.0316` | `0.0924 ± 0.0057` | `0.0000` (Neutral) |

---

## 🔍 Detailed Subtype Findings

### 🟢 What Improved?
The reinforcement learning fine-tuning successfully improved performance on **logical constraints, textual structures, and rule-based tasks**:
1. **Paper Folding** (Spatial Perception): **`19.44% ± 3.93%`** vs. `8.33% ± 0.00%` (**`+11.11%`**)
   * *Findings:* The model learned to formulate cleaner step-by-step reasoning logic before making spatial fold counts.
2. **Find the same** (Fine-grained Discrimination): **`3.92% ± 2.77%`** vs. `0.00% ± 0.00%` (**`+3.92%`**)
3. **Mirroring Patterns** (Visual Pattern Recognition): **`10.00% ± 0.00%`** vs. `6.67% ± 4.71%` (**`+3.33%`**)
4. **Recognize numbers and letters** (Visual Tracking): **`10.14% ± 2.05%`** vs. `7.25% ± 2.05%` (**`+2.89%`**)

### 🔴 What Did Not Improve (Regressed)?
Regressions occurred mainly in tasks heavily dependent on **fine-grained visual details and spatial-image alignment**:
1. **2D Pattern Completion:** **`28.33% ± 6.24%`** vs. `43.33% ± 2.36%` (**`-15.00%`**)
2. **Rotation Patterns:** **`6.67% ± 4.71%`** vs. `20.00% ± 8.16%` (**`-13.33%`**)
3. **Count Clusters:** **`3.70% ± 2.62%`** vs. `12.96% ± 6.93%` (**`-9.26%`**)
4. **Overlay Patterns:** **`5.88% ± 4.80%`** vs. `9.80% ± 2.77%` (**`-3.92%`**)

---

## 🧠 Diagnostic Analysis

### 1. Visual-Text Representation Drift
In GRPOTrainer, LoRA weights were only targeted at the **causal language model sub-layers** (`q_proj.linear`, `v_proj.linear`, etc.). The vision encoder remained frozen. 
As the language layers optimized for textual formatting rewards, their internal latent projections drifted away from the frozen visual encoder's representations. This resulted in the model writing beautifully structured reasoning sequences (`\boxed{}`) but occasionally losing grounding on exact visual counts or pixel-level relationships.

### 2. Format Reward Bias on Small Datasets
The training set was limited to **310 tasks** (80% of BabyVision). Because the correctness reward (`correctness_reward = 1.0` or `0.0`) was sparse on complex spatial puzzles, the training optimizer heavily prioritized the easy-to-learn format reward (`format_reward = 0.1` for outputting `\boxed{}`). This biased the policy toward generating correct formatting at the expense of rigorous visual correctness checking.

---

## 🛠️ Recommendations for Next Steps

To build on these results and fix the visual grounding regression:
1. **Multimodal PEFT Targets:** In future runs, extend the LoRA target modules to include projection layers inside the visual encoder. This allows the model to adjust its visual features during training.
2. **Increase Correctness Reward Weight:** Scale up the correctness reward (e.g., setting it to `2.0` or `5.0` relative to a `0.1` format reward) to force the policy optimizer to value task correctness much more than simple format compliance.
3. **Augment visual dataset:** Pre-train or co-train on a larger, synthetic dataset with rich visual Chain-of-Thought reasoning.
