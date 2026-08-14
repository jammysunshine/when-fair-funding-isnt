# Automated Mechanism Discovery — Experiment 67

The headline artifact is a finite public-project study grounded in the
efficiency/budget-balance literature. It exhaustively enumerates anonymous
monotone Boolean allocation rules for `n=3,4,5` agents with values `{0,1,2}`
(16, 32, and 64 rules), uses normalized discrete critical payments, and
certifies the cost-indexed DSIC/IR/no-deficit frontier. The original
three-agent domain is preregistered; the cross-agent extension is explicitly
exploratory and now includes an exact six-agent extension (128 rules at each
of 12 costs, with every accepted row independently replayed). Earlier binary
allocation audits remain regression baselines.

## Reproduce

```bash
python3 -m unittest discover -s tests -v
python3 scripts/run_public_project_study.py
python3 scripts/verify_public_project_certificate.py
python3 scripts/run_experiment.py
python3 scripts/verify_certificates.py
python3 scripts/run_three_agent_extension.py
python3 scripts/verify_three_agent_certificates.py
python3 scripts/run_n6_extension.py
```

The public-project outputs are `artifacts/public_project_study.json`,
`artifacts/public_project_certificate.json`, `artifacts/public_project_scaling.csv`,
`artifacts/public_project_frontier.csv`, and `reports/public_project_frontier.svg`.
Read `PROJECT_CHARTER.md`, `MECHANISM_SPEC.md`, `PREREGISTRATION.md`,
`SCALING_EXTENSION_PROTOCOL.md`, `PRIOR_ART.md`, and `LIMITATIONS.md` before
interpreting them.
The six-agent artifact is `artifacts/public_project_n6_extension.json`; its
protocol is frozen in `SCALING_N6_EXTENSION_PROTOCOL.md`.
