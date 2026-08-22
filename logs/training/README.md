# Why these logs are here

RL/GRPO training runs. `v1`/`v2` here name the correctness-reward-weight variant, not a version number - see `CLAUDE.md`'s naming-conventions note. This is unrelated to the unconnected `v2`-`v5` sequence in `../setup/`, which numbers flash-attn install retry attempts.

- `gemma_rl_v1_training_16875257`: training run for Configuration B (`rl_train_gemma4.py`, correctness_weight=1.0, language-model-only LoRA targets).
- `gemma_rl_v2_training_16877068` (+ `gemma_rl_v2_training_resume_16877168`): training run for Configuration C (`rl_train_gemma4_correctness_weight2.py`, correctness_weight=2.0, multimodal LoRA targets), resumed after hitting a partition time limit.
- `gemma_system_prompt_rl_training_16877070`: training run for Configuration D (`rl_train_system_prompt.py`).
