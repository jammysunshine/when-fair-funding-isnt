# Handoff — Experiment 67

SAFE FOR LUNA HANDOFF

Lead completion gate: Experiment 67 is complete and committed. Frozen lead checkpoint is the final commit containing this file; verify it with `git log -1 --oneline`.

Frozen configuration:

- Domain, acceptance predicates, evidence boundary: `PROJECT_CHARTER.md`, `PREREGISTRATION.md`, `MECHANISM_SPEC.md`.
- Main configuration: `configs/experiment_67.json` (SHA-256 `cce3d57be6fbcc021c4fa8da9f7785bf2a11a9645b8a15a13176fd9b1894d1d3`).
- Confirmation configuration: `configs/confirmation_67.json` (SHA-256 `3f2553cf3237dc13dd335bc60e672d68749832490cd8ecb8fa9ee15016650f3a`).
- Seed `67`, population `64`, generations `40`, payment grid `{-1,0,1}`, `1,296` candidates, primary baseline `anonymous_or`.

Exact commands from the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/run_experiment.py
python3 scripts/verify_certificates.py
sha256sum configs/experiment_67.json configs/confirmation_67.json artifacts/experiment_67_results.json artifacts/experiment_67_independent_certificate.json artifacts/frontier.csv reports/frontier.svg
```

Expected evidence: 13 tests pass; both enumerators accept exactly 4 tables and report frontier digest `3a729b20545161e401e7689ef4f3b491ce22269c9ecb49ef76e82d38145ab6e2`; no strict welfare improver is found; baseline held-out coalition and `{0,1,2}` magnitude audits have zero failures.

Artifact paths:

- `artifacts/experiment_67_results.json` — full baseline, canonical comparator, exhaustive, and evolutionary results.
- `artifacts/experiment_67_independent_certificate.json` — independent frontier, held-out audits, neutrality impossibility, and minimal counterexample certificate.
- `artifacts/frontier.csv` and `reports/frontier.svg` — raw frontier data and plot.
- `VERIFICATION_REPORT.md`, `RESULTS.md`, `CLAIM_LEDGER.md`, `EVIDENCE_INDEX.md`, `REPRODUCIBILITY_MANIFEST.md` — interpretation and evidence map.

Remaining tasks: none for the frozen Experiment 67 objective. Optional follow-ons must use a new charter/preregistration and confirmation boundary; Luna must not alter the frozen domain, verifier semantics, baseline, acceptance criteria, or conclusions.
