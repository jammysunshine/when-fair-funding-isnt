# Experiment 67 delivery record

## Frozen configuration

The preregistered headline is `configs/public_project_study.json`: three
agents, values `{0,1,2}`, costs `1..6`, all anonymous monotone Boolean rules,
normalized discrete critical payments, DSIC, ex-post IR, feasibility,
anonymity, no-subsidy, all-maximum-profile build, and weak budget balance.
`SCALING_EXTENSION_PROTOCOL.md` freezes the exploratory exact extension at
`n=3,4,5` and every cost `1..2n`, using the same checks and antichain
enumeration. It is not retroactively part of the main preregistration.

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
python3 scripts/run_value_extension.py
git diff --check
```

## Artifact paths

- Model/specification: `MECHANISM_SPEC.md`, `PREREGISTRATION.md`,
  `SCALING_EXTENSION_PROTOCOL.md`, `PRIOR_ART.md`
- Main and scaling results: `artifacts/public_project_study.json`,
  `artifacts/public_project_scaling.csv`, `artifacts/public_project_frontier.csv`
- Independent certificate: `artifacts/public_project_certificate.json`
- Value-lattice sensitivity: `artifacts/public_project_value_extension.json`
- Plot: `reports/public_project_frontier.svg`
- Code: `src/mechanism_discovery/public_project.py`,
  `src/mechanism_discovery/public_project_independent.py`,
  `scripts/run_public_project_study.py`,
  `scripts/verify_public_project_certificate.py`
- Manuscript and interpretation: `PAPER_DRAFT.md`, `RESULTS.md`,
  `VERIFICATION_REPORT.md`, `CLAIM_LEDGER.md`, `LIMITATIONS.md`

## Verified result

The exact candidate counts for `n=3,4,5` are `16,32,64`; accepted counts by
cost are `4,4,4,1,1,1`, `5,5,5,5,1,1,1,1`, and
`6,6,6,6,6,1,1,1,1,1`. All 74 serialized accepted rows pass independent
replay; the held-out efficient-threshold audit records 207 failures.
The exploratory `max_value=3` extension enumerates 66 rules over 20 states,
accepts `15,15,15,4,4,4,1,1,1` rules across costs `1..9`, and independently
replays all 60 serialized accepted rows with zero failures.

## Remaining research tasks

No implementation or verification task in the declared finite study remains.
Before journal submission, test whether the observed pattern persists beyond
`n=5`, extend beyond `max_value=3`, compare broader mechanism classes, and
obtain external replication. The manuscript must not claim a general theorem,
guaranteed novelty, or guaranteed acceptance from this finite certificate.
