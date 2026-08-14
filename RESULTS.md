# Results

The exact class contains 16 anonymous monotone rules. At cost `c=3`, 4 rules satisfy every frozen constraint; an independent checker accepts all 4 and rejects none. The cost-indexed accepted counts are 4, 4, 4, 1, 1, 1 for `c=1,...,6`.

Best worst-case regret is 3, 2, 1, 1, 0, 0 respectively. Best expected welfare under the uniform `3^3` profiles is 1.0370, 0.7407, 0.4444, 0.0741, 0.0370, and 0.0000. These are finite-domain values, not continuous-domain guarantees.

The efficient critical-payment rule passes DSIC, ex-post IR, feasibility, and anonymity but fails budget balance; `(0,2,2)` is a concrete witness at cost 3. The held-out value-magnitude audit finds 207 budget/IC audit failures across thresholds 1–6 on 64 profiles each. That stress result limits generalization and is part of the result.

Artifacts: `artifacts/public_project_study.json`, `artifacts/public_project_certificate.json`, `artifacts/public_project_frontier.csv`, and `reports/public_project_frontier.svg`.
