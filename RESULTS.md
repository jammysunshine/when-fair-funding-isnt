# Results

The preregistered three-agent class contains 16 anonymous monotone rules. At
costs `1..6`, accepted counts are `4,4,4,1,1,1`; best worst-case regrets are
`3,2,1,1,0,0`. The four cost-3 rows all pass the independent checker.

The exact finite cross-check enumerates 16, 32, and 64 rules for `n=3,4,5`.
Across costs `1..2n`, accepted counts are:

| agents | accepted counts by cost |
|---:|---|
| 3 | 4,4,4,1,1,1 |
| 4 | 5,5,5,5,1,1,1,1 |
| 5 | 6,6,6,6,6,1,1,1,1,1 |

All 74 serialized accepted rows pass the standalone checker. The all-agent
theorem below explains these counts in the declared model. The efficient
critical-payment rule still fails budget balance at `(0,2,2)` (payments
`(0,1,1)` against cost 3). The held-out `{0,1,2,3}` stress audit records 207
failures for the efficient threshold family, preserving the generalization
boundary.

The harder six-agent extension enumerates 128 rules over 28 sorted states at
each cost `1..12`. Accepted counts are `7,7,7,7,7,7,1,1,1,1,1,1`; all 48
serialized accepted rows pass independent replay. The complete run took
56.394 seconds and recorded 29,474,816 bytes peak resident memory on Darwin.
This is a finite computational cross-check of the all-agent theorem; its
runtime and memory remain useful reproducibility measurements.

## All-agent theorem

For every `n>=1` and integer cost `c`, within the declared deterministic,
anonymous, coordinatewise-monotone ternary class with normalized critical
payments and required build at the all-2 profile, the accepted count is
`n+1` for `1<=c<=n`, `1` for `n<c<=2n`, and `0` for `c>2n`. The accepted rules
are exactly `q_k(v)=1` when every value is at least 1 and at least `k` values
equal 2, with `k=0..n` in the first range and `k=n` in the second. The proof
and machine-checkable construction certificate are in
`PUBLIC_PROJECT_THEOREM.md` and `artifacts/public_project_scaling_theorem.json`.

As a post-hoc sensitivity check, the exact three-agent lattice was expanded to
values `{0,1,2,3}` (20 sorted states, 66 anonymous monotone rules). Across
costs `1..9`, accepted counts were `15,15,15,4,4,4,1,1,1`; all 60 serialized
accepted rows passed independent replay. This extension is exploratory and
does not alter the preregistered headline.

Artifacts: `artifacts/public_project_study.json`,
`artifacts/public_project_certificate.json`,
`artifacts/public_project_scaling.csv`,
`artifacts/public_project_frontier.csv`, and `reports/public_project_frontier.svg`.
The value-lattice extension is in `artifacts/public_project_value_extension.json`.
The six-agent extension is in `artifacts/public_project_n6_extension.json`.
