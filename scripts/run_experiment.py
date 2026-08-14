#!/usr/bin/env python3
"""Run the frozen Experiment 67 baseline, exact enumeration, and proposal loop."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from mechanism_discovery.independent_verifier import check
from mechanism_discovery.model import canonical_baselines, priority_majority
from mechanism_discovery.search import evolutionary_search, exhaustive_search
from mechanism_discovery.verifier import metrics, verify


def fingerprint(mechanism):
    return [{"profile": list(p), "choice": mechanism.outcome(p).choice,
             "payments": list(mechanism.outcome(p).payments)}
            for p in ((0, 0), (0, 1), (1, 0), (1, 1))]


def main():
    config = json.loads((ROOT / "configs/experiment_67.json").read_text())
    baseline = priority_majority()
    baselines = canonical_baselines()
    exact = exhaustive_search()
    frontier = []
    for row in exact:
        frontier.append({"outcomes": fingerprint(row["mechanism"]), "metrics": row["metrics"]})
    output = {
        "config": config,
        "baseline": {"name": baseline.name, "outcomes": fingerprint(baseline),
                     "primary_verifier": verify(baseline).as_dict(),
                     "independent_verifier": check(baseline), "metrics": metrics(baseline)},
        "canonical_baselines": [
            {"name": mechanism.name, "outcomes": fingerprint(mechanism),
             "primary_verifier": verify(mechanism).as_dict(),
             "independent_verifier": check(mechanism), "metrics": metrics(mechanism)}
            for mechanism in baselines
        ],
        "exhaustive_search": {"candidate_count": config["exhaustive_candidates"], "accepted_count": len(exact),
                              "frontier": frontier},
        "evolutionary_search": evolutionary_search(**config["evolutionary"]),
    }
    artifact = ROOT / "artifacts/experiment_67_results.json"
    artifact.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(artifact.relative_to(ROOT))


if __name__ == "__main__":
    main()
