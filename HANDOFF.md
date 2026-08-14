# Experiment 67 handoff

## Frozen configuration

Headline study: `configs/public_project_study.json` — three agents, values `{0,1,2}`, costs `1..6`, all anonymous monotone Boolean allocation rules, normalized discrete critical payments, no-subsidy weak budget balance, and a project required at the all-2 profile. The original binary and three-agent audits are regression baselines only.

## Exact commands

```bash
cd /Users/mohitmendiratta/Projects/personal/research/automated-mechanism-discovery
python3 -m unittest discover -s tests -v
python3 scripts/run_public_project_study.py
python3 scripts/verify_public_project_certificate.py
python3 scripts/run_experiment.py
python3 scripts/verify_certificates.py
python3 scripts/run_three_agent_extension.py
python3 scripts/verify_three_agent_certificates.py
git diff --check
```

## Artifact paths

- Specification and claims: `MECHANISM_SPEC.md`, `PREREGISTRATION.md`, `PRIOR_ART.md`, `CLAIM_LEDGER.md`
- Main result: `artifacts/public_project_study.json`
- Independent certificate: `artifacts/public_project_certificate.json`
- Frontier table/plot: `artifacts/public_project_frontier.csv`, `reports/public_project_frontier.svg`
- Code: `src/mechanism_discovery/public_project.py`, `src/mechanism_discovery/public_project_independent.py`, `scripts/run_public_project_study.py`, `scripts/verify_public_project_certificate.py`
- Interpretation: `RESULTS.md`, `COUNTEREXAMPLES.md`, `LIMITATIONS.md`, `PAPER_DRAFT.md`

## Remaining tasks

No in-scope implementation tasks remain. A future paper submission still needs external novelty review, larger domains, subsidy/randomization comparisons, and an independent external replication; these are explicitly outside this handoff.

The package is reproducible and safe to pass to the next operator: **SAFE FOR LUNA HANDOFF.**

Delivered commit: `bde1b7c` on `origin/main`.
