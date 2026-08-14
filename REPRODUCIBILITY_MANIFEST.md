# Reproducibility Manifest

Repository initialized: 2026-08-14. Code is Python 3 standard library only; no external data or models. The immutable finite fixture is `src/mechanism_discovery/model.py`: profiles `(0,0),(0,1),(1,0),(1,1)`, choices/types `{0,1}`, payments `{-1,0,1}`, and the uniform evaluation distribution.

Frozen configuration: `configs/experiment_67.json`, SHA-256 `48a32229954aefe983e4a434c21a338eca885115105927e8111afaed3e55acc7`. Seed: 67. Run `python3 -m unittest discover -s tests -v` then `python3 scripts/run_experiment.py`. Expected result: `artifacts/experiment_67_results.json`, SHA-256 `945fb3ebd1c3e7850a28252742f405e6b104c33a736fff48b4b95b59c1b08a41`, candidate count 1,296, accepted count 16, and baseline accepted by both checkers. Hardware nondeterminism: none expected; the proposal loop uses local `random.Random(67)`.
