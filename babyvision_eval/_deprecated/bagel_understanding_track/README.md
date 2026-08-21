# Why this is deprecated

I originally ran ByteDance's BAGEL-7B-MoT through the same understanding-only track as Gemma and Qwen (`understanding_output=True` - text answer only, no image generation), out of curiosity about how a different architecture handled the same tasks.

Re-reading the BabyVision paper more carefully: it doesn't suggest running BAGEL on the standard MLLM understanding track at all. It mentions BAGEL specifically in the context of `BabyVision-Gen` - unified models that natively integrate understanding and generation could "think in visual space" (sketching trajectories, marking regions) instead of being forced to verbalize an answer. That's a fundamentally different, more interesting question than "how does BAGEL do as a text-answering MLLM," and it belongs in `babyvision_gen_eval/`, not here.

So this comparison, while the numbers in it are real and the token-truncation finding is still a legitimate example of the same eval-budget bug documented in `results/final_report.md`, was run on the wrong benchmark for what it was actually trying to test. Kept here for the record rather than deleted, but it's not part of the main results anymore.

If BAGEL gets tested properly in the future, it should be through `babyvision_gen_eval/` using its native image-editing mode (`understanding_output=False, think=True`), scored against `answerImages/` the same way other generation models are.
