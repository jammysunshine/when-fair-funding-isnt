# Results

The preregistered three-agent class contains 16 anonymous monotone rules. At
costs `1..6`, accepted counts are `4,4,4,1,1,1`; best worst-case regrets are
`3,2,1,1,0,0`. The four cost-3 rows all pass the independent checker.

The exploratory exact extension enumerates 16, 32, and 64 rules for `n=3,4,5`.
Across costs `1..2n`, accepted counts are:

| agents | accepted counts by cost |
|---:|---|
| 3 | 4,4,4,1,1,1 |
| 4 | 5,5,5,5,1,1,1,1 |
| 5 | 6,6,6,6,6,1,1,1,1,1 |

All 74 serialized accepted rows pass the standalone checker. This supports a
finite pattern in the tested range, not an asymptotic theorem. The efficient
critical-payment rule still fails budget balance at `(0,2,2)` (payments
`(0,1,1)` against cost 3). The held-out `{0,1,2,3}` stress audit records 207
failures for the efficient threshold family, preserving the generalization
boundary.

Artifacts: `artifacts/public_project_study.json`,
`artifacts/public_project_certificate.json`,
`artifacts/public_project_scaling.csv`,
`artifacts/public_project_frontier.csv`, and `reports/public_project_frontier.svg`.
