import json
import argparse
import os
import sys

import numpy as np


def no_answer_rate(path):
    with open(path, "r") as f:
        results = json.load(f)
    total = len(results)
    no_answer = sum(
        1 for r in results if not str(r.get("ExtractedAnswer") or "").strip()
    )
    return no_answer / total if total > 0 else 0.0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compute the no-answer rate (empty ExtractedAnswer / total) "
        "averaged across multiple result JSON files (one per evaluation round), "
        "and save the summary alongside them."
    )
    parser.add_argument("files", nargs="+", help="Path(s) to raw_results_run_*.json file(s)")
    args = parser.parse_args()

    rates = []
    for file_path in args.files:
        try:
            rates.append(no_answer_rate(file_path))
        except FileNotFoundError:
            print(f"Error: File not found: {file_path}", file=sys.stderr)
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in file: {file_path}", file=sys.stderr)
            sys.exit(1)

    mean_rate = float(np.mean(rates))
    std_rate = float(np.std(rates))

    lines = [f"No-answer rate per round: {[f'{r * 100:.1f}%' for r in rates]}"]
    lines.append(f"No-answer rate (mean ± std across {len(rates)} round(s)): {mean_rate * 100:.1f}% ± {std_rate * 100:.1f}%")
    output = "\n".join(lines)
    print(output)

    out_dir = os.path.dirname(os.path.abspath(args.files[0]))
    out_path = os.path.join(out_dir, "no_answer_rate.txt")
    with open(out_path, "w") as f:
        f.write(output + "\n")
    print(f"\nSaved to {out_path}")
