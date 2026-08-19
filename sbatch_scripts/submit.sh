#!/bin/bash
# Wrapper around sbatch that adds email notifications on job end/fail,
# reading the address from SLURM_NOTIFY_EMAIL in .env so it isn't
# hardcoded into any tracked sbatch script.
#
# Usage: sbatch_scripts/submit.sh <path-to-sbatch-script> [extra sbatch args...]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

if [ -f "$REPO_ROOT/.env" ]; then
  set -a
  source "$REPO_ROOT/.env"
  set +a
fi

if [ -z "${SLURM_NOTIFY_EMAIL:-}" ]; then
  echo "Error: SLURM_NOTIFY_EMAIL is not set. Add it to .env (see .env.example)." >&2
  exit 1
fi

exec sbatch --mail-type=BEGIN,END,FAIL --mail-user="$SLURM_NOTIFY_EMAIL" "$@"
