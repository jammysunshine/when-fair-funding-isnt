# Handoff — Experiment 67

Status: **SAFE FOR LUNA HANDOFF**

Lead-owned frozen implementation commit: `1773053bbf62c656481e2f29cffa7baabe13a2cf` (`Complete Experiment 67 finite verifier baseline`). The exact domain, mechanism specification, primary acceptance criteria, verifier semantics, and baseline are frozen in this commit. Luna must not modify them or alter research conclusions.

Run from the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/run_experiment.py
shasum -a 256 configs/experiment_67.json artifacts/experiment_67_results.json
```

Frozen configuration: `configs/experiment_67.json`, SHA-256 `48a32229954aefe983e4a434c21a338eca885115105927e8111afaed3e55acc7`; seed 67, evolutionary population 64, generations 40. Frozen specifications: `PROJECT_CHARTER.md`, `PREREGISTRATION.md`, and `MECHANISM_SPEC.md`. Verifiers: `src/mechanism_discovery/verifier.py` and `src/mechanism_discovery/independent_verifier.py`. Baseline: `priority_majority_agent_0` in `src/mechanism_discovery/model.py`.

Expected output: `artifacts/experiment_67_results.json`, SHA-256 `945fb3ebd1c3e7850a28252742f405e6b104c33a736fff48b4b95b59c1b08a41`; exactly 1,296 enumerated candidates, 16 accepted mechanisms, baseline accepted by both checkers, and 2,560 seeded evolutionary proposals. Supporting evidence: `VERIFICATION_REPORT.md`, `RESULTS.md`, `CLAIM_LEDGER.md`, and `REPRODUCIBILITY_MANIFEST.md`.

Bounded Luna queue:

1. Re-run the three commands and report any mismatch without changing files.
2. Add a separately authored SAT/SMT or other-language checker only in a new, explicitly frozen follow-on scope; compare its accepted set to the committed 16-table JSON frontier.
3. For any domain expansion, stop and escalate before editing frozen files; Terra must create a new charter/preregistration/confirmation boundary.

Escalate to Terra if a test, checksum, candidate count, accepted count, baseline checker result, or independently reproduced frontier differs; if prior art appears to make any wording misleading; or before changing agents, type space, transfers, objectives, verifier semantics, or acceptance criteria.
