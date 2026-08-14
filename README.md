# Automated Mechanism Discovery — Experiment 67

The headline artifact is a finite public-project study grounded in the efficiency/budget-balance literature. It exhaustively enumerates all anonymous monotone Boolean allocation rules for three agents with values `{0,1,2}`, uses normalized critical payments, and certifies the cost-indexed DSIC/IR/no-deficit frontier. The earlier binary allocation audits remain regression baselines in the repository.

## Reproduce

```bash
python3 -m unittest discover -s tests -v
python3 scripts/run_public_project_study.py
python3 scripts/verify_public_project_certificate.py
python3 scripts/run_experiment.py
python3 scripts/verify_certificates.py
python3 scripts/run_three_agent_extension.py
python3 scripts/verify_three_agent_certificates.py
```

The public-project outputs are `artifacts/public_project_study.json`, `artifacts/public_project_certificate.json`, `artifacts/public_project_frontier.csv`, and `reports/public_project_frontier.svg`. Read `PROJECT_CHARTER.md`, `MECHANISM_SPEC.md`, `PREREGISTRATION.md`, `PRIOR_ART.md`, and `LIMITATIONS.md` before interpreting them.
