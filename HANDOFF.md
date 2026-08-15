# Handoff for next model

## Objective
Continue Experiment 67 / public-project frontier work: complete reproducible, publication-oriented finish for the coalition-robust finite-domain frontier and decide what can and cannot be claimed in a peer-reviewed paper.

## Current repo state
- Branch: `main`
- Working tree: clean (all Phase X coalition work committed)
- Top commit: `41fa06c` Extend coalition-robustness study to max_value=3 frontier and refresh reproducibility manifest
- All eight coalition run/verify commands re-ran clean from a fresh state: 0 independent failures across frontier, scaling (`n=3..5`), scaling-extended (`n=3..6`), and the new `max_value=3` frontier extension.
- Full test suite: 77/77 passing.
- Fixed one digest transcription typo in `VERIFICATION_REPORT.md` (`eaba6dc76` -> `eabe6dc76`) found during hash reconciliation.

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

## Immediate remaining tasks (all above completed this session)
1. ~~Stage/commit `HANDOFF` plus untracked Phase X configs/scripts/artifacts.~~ Done (`41fa06c`).
2. ~~Re-run experiment commands from clean state and refresh `REPRODUCIBILITY_MANIFEST.md` hashes.~~ Done, all zero-failure.
3. ~~Reconcile mismatches in `STATUS.md`, `EVIDENCE_INDEX.md`, `VERIFICATION_REPORT.md`.~~ Done.
4. Remaining: add paper-grade extension if continuing (broader mechanism class, stronger benchmarks, and/or independent baseline audit) before any submission claim. Not yet started.

## Commit practice
- Preserve commit identity:
  - `Mohit Mendiratta <mohit@zenith.com.au>`
- No AI attribution/Co-Authored trailers in git metadata.
- Push fallback command if GitHub returns 403 write-access errors:
  - `env -u GH_TOKEN git -c credential.helper='!gh auth git-credential' push`

SAFE FOR LUNA HANDOFF
