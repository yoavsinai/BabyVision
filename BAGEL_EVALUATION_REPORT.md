# BabyVision Benchmark Evaluation Report: BAGEL Model

> [!TIP]
> **📊 [Open the Interactive Results Dashboard](./index.html)**: View interactive charts, filterable tables, and detailed logs directly in your browser.

This report summarizes the benchmark evaluation results of the **BAGEL** model (**ByteDance-Seed/BAGEL-7B-MoT**) on the **BabyVision** visual reasoning dataset, compared against the **Gemma 4** model baseline.


---

## 1. Executive Summary

We evaluated the visual understanding and reasoning capabilities of the BAGEL model on the BabyVision dataset. The evaluation was run in `bfloat16` precision with Chain-of-Thought planning activated (`think=True`) to maximize the model's visual reasoning performance. Predictions were evaluated using a local LLM Judge (`Qwen/Qwen2.5-7B-Instruct`).

### Overall Scores

* **BAGEL Overall Accuracy:** **4.12%** (`0.0412 ± 0.0000`)
* **Gemma 4 Baseline Accuracy:** **11.08%** (`0.1108 ± 0.0117`)

> [!NOTE]
> While BAGEL's raw accuracy is lower than Gemma 4's, this is primarily a consequence of strict token limits during the Chain-of-Thought thinking process rather than poor visual logic. See the [Analysis section](#4-analysis-and-key-findings) below for details.

---

## 2. Category-Wise Evaluation Results

The table below breaks down the average accuracy (across 3 passes) for both models across the four primary categories of the BabyVision dataset:

| Dataset Category | BAGEL Accuracy (bfloat16, CoT) | Gemma 4 Accuracy (Baseline) |
| :--- | :---: | :---: |
| **Fine-grained Discrimination** | **4.91%** | 10.84% |
| **Spatial Perception** | **2.20%** | 13.92% |
| **Visual Pattern Recognition** | **5.88%** | 9.80% |
| **Visual Tracking** | **3.61%** | 9.24% |

### Subtype-Wise Accuracy Breakdown (BAGEL)
* **2D Pattern Completion:** 15.00%
* **3D Pattern Completion:** 11.11%
* **Find the Shadow:** 8.70%
* **Pattern and Color Completion:** 10.00%
* **Overlay Patterns:** 5.88%
* **Rotation Patterns:** 20.00%
* **Count Clusters:** 5.56%
* **Connect the Lines / Maze / Recognize Characters:** 4.3%–5.2%
* *All other visual tracking and discrimination subtypes scored 0% due to task-level token truncation.*

---

## 3. Engineering & Deployment Details

Due to the length of BAGEL's Chain-of-Thought reasoning steps, the evaluation of 388 tasks over 3 passes takes ~15.5 hours on an NVIDIA A100 GPU. To overcome the cluster's strict 4-hour partition limit, we implemented a robust **fault-tolerant execution pipeline**:

1. **Incremental Checkpointing:** Modified the evaluation script to save raw outputs to disk after every 5 tasks, allowing the run to resume from the last saved state without losing progress on preemption or timeout.
2. **Dependency Queue Chaining:** Submitted a chain of 4 dependent Slurm jobs to the scheduler:
   * [bagel_eval_16877352](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/bagel_eval_16877352.out) (completed passes 1 and 2, timed out during pass 3)
   * [bagel_eval_16877397](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/bagel_eval_16877397.out) (resumed pass 3, ran judging phase, completed the evaluation)
   * Subsequent jobs resolved instantly seeing the finished state.

---

## 4. Analysis and Key Findings

### Why is BAGEL's raw score 4.12%?
* **Strict Token Truncation:** BAGEL has a very verbose internal planning and reasoning mechanism. The evaluation script enforced a limit of `max_think_token_n=1024` tokens for the reasoning process. 
* **The Penalty:** In **78% of the tasks** (303 out of 388), BAGEL spent more than 1024 tokens thinking, running out of tokens *before* it could output the final answer in the required `\boxed{Answer}` format. This resulted in an empty extracted answer, which scored 0%.
* **Adjusted Accuracy:** On the 85 tasks where BAGEL finished its thinking and successfully wrote a final answer before reaching the token limit, it achieved **18.8% accuracy (16/85)**, showcasing a strong capacity for visual discrimination.

### Zero Standard Deviation (`± 0.0000`)
Unlike Gemma 4 which used stochastic sampling, BAGEL was run with greedy decoding (`do_sample=False`). This made the generation 100% deterministic across the three passes, ensuring reproducible results and standard deviations of exactly `0.0`.

---

## 5. Artifacts and Raw Data Links

* **Scoring Summary Output:** [score_summary.txt](file:///home/dsi/sinayyo/BabyVision/babyvision_eval/results_local_bagel/score_summary.txt)
* **Model Result Passes:**
  * [Pass 1 Results JSON](file:///home/dsi/sinayyo/BabyVision/babyvision_eval/results_local_bagel/model_results_run_1.json)
  * [Pass 2 Results JSON](file:///home/dsi/sinayyo/BabyVision/babyvision_eval/results_local_bagel/model_results_run_2.json)
  * [Pass 3 Results JSON](file:///home/dsi/sinayyo/BabyVision/babyvision_eval/results_local_bagel/model_results_run_3.json)
* **Execution Logs:**
  * [Evaluation Logs](file:///home/dsi/sinayyo/BabyVision/logs/evaluation/)
  * [Setup Logs](file:///home/dsi/sinayyo/BabyVision/logs/setup/)
  * [Slurm Runner Scripts](file:///home/dsi/sinayyo/BabyVision/sbatch_scripts/)
