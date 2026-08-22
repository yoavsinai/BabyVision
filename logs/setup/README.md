# Why these logs are here

Environment/dependency setup logs, not evaluation or training runs.

- `install_flash_attn_16877274` through `16877291` (no suffix) and `install_flash_attn_v2_16877315` through `install_flash_attn_v5_16877322`: sequential retry attempts at installing the `flash-attn` package, unrelated to the RL "v1/v2" correctness-weight naming used elsewhere in `logs/`. Each attempt failed for a different reason (build error, SLURM time-limit cancellation, compile errors) until `install_flash_attn_v5_16877322` succeeded (`Successfully installed ... flash-attn-2.8.3.post1`). Only the `v5` run matters; the rest are kept for the record of what didn't work.
- `bagel_test_*`, `cuda_check_*`: one-off environment checks, no bearing on any reported result.
