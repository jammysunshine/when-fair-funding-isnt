# Replication Guide

From the repository root, run:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/run_experiment.py
shasum -a 256 configs/experiment_67.json artifacts/experiment_67_results.json
```

Expected invariants: six tests pass; result JSON has `candidate_count: 1296`, `accepted_count: 16`, and both baseline checkers accepted. Python 3 with no package installation is sufficient.
