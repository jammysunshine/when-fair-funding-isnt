# Verification Report

Run: `python3 -m unittest discover -s tests -v && python3 scripts/run_experiment.py`.

The primary verifier and independent checker both accept `priority_majority_agent_0`. Its exact uniform-profile metrics are welfare 1.5, utility disparity 0.5, worst-case regret 0, and description length 2. The exhaustive enumerator visited all 1,296 frozen candidates and primary-verifier accepted 16. The checked result is `artifacts/experiment_67_results.json`.

Coverage is finite and complete only for the configured type, alternative, transfer, determinism, and direct-revelation boundary. The independent checker repeats DSIC/IR/budget/feasibility logic separately; it is not an external research replication.
