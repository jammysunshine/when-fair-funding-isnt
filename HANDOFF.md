# Handoff — Experiment 67

Status: **NOT READY — lead integration in progress.** This file is intentionally not a Luna handoff until the final verification and commit gate is complete.

Frozen domain/specification: `PROJECT_CHARTER.md`, `PREREGISTRATION.md`, `MECHANISM_SPEC.md`, `configs/experiment_67.json`, and `configs/confirmation_67.json`.

Verifiers and search: `src/mechanism_discovery/verifier.py`, `src/mechanism_discovery/independent_verifier.py`, `src/mechanism_discovery/search.py`, `scripts/run_experiment.py`, `scripts/verify_certificates.py`.

Expected artifacts: `artifacts/experiment_67_results.json`, `artifacts/experiment_67_independent_certificate.json`, `artifacts/frontier.csv`, `reports/frontier.svg`.

Frozen reproduction commands:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/run_experiment.py
python3 scripts/verify_certificates.py
sha256sum configs/experiment_67.json configs/confirmation_67.json artifacts/experiment_67_results.json artifacts/experiment_67_independent_certificate.json artifacts/frontier.csv reports/frontier.svg
```

Frozen invariants: 13 tests pass; 1,296 candidates; 4 accepted tables; primary/independent digest `3a729b20545161e401e7689ef4f3b491ce22269c9ecb49ef76e82d38145ab6e2`; baseline `anonymous_or` accepted by both checkers; no strict welfare improver; bounded baseline audits have zero failures.

Remaining tasks before handoff: rerun all commands after documentation/artifact generation, verify hashes and clean Git state, commit the coherent checkpoint with the preserved Mohit identity, then replace this status with the exact statement `SAFE FOR LUNA HANDOFF`.
