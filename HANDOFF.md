# Handoff for next model

## Objective
Continue Experiment 67 / public-project frontier work: complete reproducible, publication-oriented finish for the coalition-robust finite-domain frontier and decide what can and cannot be claimed in a peer-reviewed paper.

## Current repo state
- Branch: `main`
- Working tree: dirty
- Top commits:
  - `a716da7` Add certified ReLU verifier scaling study
  - `936714e` Prove finite value-lattice public-project frontier
- Modified tracked files: `CLAIM_LEDGER.md`, `DECISION_LOG.md`, `EVIDENCE_INDEX.md`, `PREREGISTRATION.md`, `PROJECT_CHARTER.md`, `REPRODUCIBILITY_MANIFEST.md`, `STATUS.md`, `VERIFICATION_REPORT.md`, `src/mechanism_discovery/public_project.py`, `src/mechanism_discovery/public_project_independent.py`, `tests/test_public_project.py`
- Added but untracked: configs, scripts, and artifacts listed below

## Frozen configuration
- Core domain: public-project mechanism design with anonymous monotone rules
- Base domain profile: `n=3`, `max_value=2`, `cost=1..6`, `max_coalition_size=2` unless noted
- Frontier artifact for this run used config `configs/public_project_coalition_frontier.json`
- Coalition robustness target: cap-2 deviations; exact frontier replay with independent verifier

## Artifact paths (current)
- `configs/public_project_coalition_frontier.json`
- `configs/public_project_coalition_scaling.json`
- `configs/public_project_coalition_scaling_extended.json`
- `configs/public_project_coalition_value3_frontier.json`
- `scripts/run_public_project_coalition_frontier.py`
- `scripts/verify_public_project_coalition_frontier.py`
- `scripts/run_public_project_coalition_scaling.py`
- `scripts/verify_public_project_coalition_scaling.py`
- `scripts/run_public_project_coalition_scaling_extended.py`
- `scripts/verify_public_project_coalition_scaling_extended.py`
- `scripts/run_public_project_coalition_value3_frontier.py`
- `scripts/verify_public_project_coalition_value3_frontier.py`
- `artifacts/public_project_coalition_frontier.json`
- `artifacts/public_project_coalition_frontier_certificate.json`
- `artifacts/public_project_coalition_scaling.json`
- `artifacts/public_project_coalition_scaling_certificate.json`
- `artifacts/public_project_coalition_scaling_extended.json`
- `artifacts/public_project_coalition_scaling_extended_certificate.json`
- `artifacts/public_project_coalition_value3_frontier.json`
- `artifacts/public_project_coalition_value3_frontier_certificate.json`

## Exact commands already expected
```bash
python3 scripts/run_public_project_coalition_frontier.py
python3 scripts/verify_public_project_coalition_frontier.py
python3 scripts/run_public_project_coalition_scaling.py
python3 scripts/verify_public_project_coalition_scaling.py
python3 scripts/run_public_project_coalition_scaling_extended.py
python3 scripts/verify_public_project_coalition_scaling_extended.py
python3 scripts/run_public_project_coalition_value3_frontier.py
python3 scripts/verify_public_project_coalition_value3_frontier.py
python3 scripts/generate_frontier_report.py
python3 -m unittest discover -s tests -v
```

## What has been established
- Finite-domain phase exists and is reproducible at least through the coalition-cap-2 frontier pass.
- In the frozen frontier with cap-2, DSIC frontier shrank from 4 accepted entries to 2 at cost=3.
- Independent frontier replay and certificate flow are integrated in the current documentation and logs.
- Existing result is a bounded finite artifact; not yet a broad publication-grade general theorem.

## Immediate remaining tasks
1. Stage/commit `HANDOFF` plus untracked Phase X configs/scripts/artifacts.
2. Re-run the seven experiment commands above from clean state and refresh `REPRODUCIBILITY_MANIFEST.md` hashes.
3. Reconcile any mismatches in `STATUS.md`, `EVIDENCE_INDEX.md`, and `VERIFICATION_REPORT.md`.
4. Add paper-grade extension if continuing (broader mechanism class, stronger benchmarks, and/or independent baseline audit) before any submission claim.

## Commit practice
- Preserve commit identity:
  - `Mohit Mendiratta <mohit@zenith.com.au>`
- No AI attribution/Co-Authored trailers in git metadata.
- Push fallback command if GitHub returns 403 write-access errors:
  - `env -u GH_TOKEN git -c credential.helper='!gh auth git-credential' push`

SAFE FOR LUNA HANDOFF
