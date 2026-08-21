# Why this is here

An earlier session tried the generation track locally with `timbrooks/instruct-pix2pix` (`inference_local_hf.py`, driven by `run_local_gen_eval.sbatch`). It's never mentioned anywhere in `results/final_report.md` - the results here (`generated_instruct-pix2pix/`, `results_instruct-pix2pix/`) never made it into any reported finding, so archived rather than presenting them as if they were part of the story.

The generation track this project actually uses is BAGEL (`babyvision_gen_eval/scripts/inference_bagel.py`), which runs the same benchmark through BAGEL's native image-editing mode instead.
