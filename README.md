# Automated Mechanism Discovery — Experiment 67

Public showcase (paper, results, PDF deck): https://github.com/jammysunshine/research-showcase/tree/main/67-when-fair-funding-isnt

The headline artifact is a finite public-project study grounded in the
efficiency/budget-balance literature. In the declared ternary anonymous
monotone class, a human-checkable argument gives the exact frontier for every
agent count `n>=1`: `n+1` accepted rules for `1<=c<=n`, one for `n<c<=2n`,
and none above `2n`. Exact searches for `n=3..6` independently cross-check the
theorem; the original three-agent domain remains preregistered. Earlier binary
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
python3 scripts/verify_scaling_theorem.py
```

The public-project outputs are `artifacts/public_project_study.json`,
`artifacts/public_project_certificate.json`, `artifacts/public_project_scaling.csv`,
`artifacts/public_project_frontier.csv`, and `reports/public_project_frontier.svg`.
Read `PROJECT_CHARTER.md`, `MECHANISM_SPEC.md`, `PREREGISTRATION.md`,
`SCALING_EXTENSION_PROTOCOL.md`, `PRIOR_ART.md`, and `LIMITATIONS.md` before
interpreting them.
The six-agent artifact is `artifacts/public_project_n6_extension.json`; its
protocol is frozen in `SCALING_N6_EXTENSION_PROTOCOL.md`.
The all-agent construction certificate is
`artifacts/public_project_scaling_theorem.json`.
