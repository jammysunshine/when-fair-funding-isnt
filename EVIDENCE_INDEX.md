# Evidence index

| Claim | Evidence | Status |
|---|---|---|
| For every `n>=1`, the declared ternary class has `n+1` accepted suffix rules when `1<=c<=n`, one when `n<c<=2n`, and none when `c>2n` | `PUBLIC_PROJECT_THEOREM.md`, `src/mechanism_discovery/public_project_theorem.py`, `scripts/verify_scaling_theorem.py`, `artifacts/public_project_scaling_theorem.json` | SUPPORTED in the declared model; human-checkable proof plus regression certificate |
| All 16 anonymous monotone rules were enumerated | `scripts/run_public_project_study.py`, `artifacts/public_project_study.json` | SUPPORTED on frozen domain |
| Antichain enumeration is exact for n=3,4,5,6 | `src/mechanism_discovery/public_project.py`, `artifacts/public_project_scaling.csv`, `artifacts/public_project_n6_extension.json` | SUPPORTED as finite cross-checks |
| Four rules satisfy the cost-3 predicate | `artifacts/public_project_study.json` | SUPPORTED on frozen domain |
| 74 n=3..5 cross-agent accepted rows replay independently | `scripts/verify_public_project_certificate.py`, `artifacts/public_project_certificate.json` | SUPPORTED |
| 48 n=6 accepted rows replay independently (122 total through n=6) | `scripts/run_n6_extension.py`, `artifacts/public_project_n6_extension.json` | SUPPORTED finite cross-check |
| Efficient critical-payment rule can fail no-deficit | `COUNTEREXAMPLES.md`, witness in study JSON | SUPPORTED |
| Cost frontier contracts as cost rises | frontier CSV/SVG and RESULTS.md | SUPPORTED descriptively |
| Value-lattice extension has 66 exact rules and 60 independently replayed accepted rows | `scripts/run_value_extension.py`, `artifacts/public_project_value_extension.json` | SUPPORTED exploratory domain |
| Finite rule generalizes to value 3 | held-out certificate | REFUTED / 207 failures |
| Continuous values, randomized/subsidized/asymmetric classes, and broader novelty | none | UNKNOWN / explicitly not claimed |
| Phase II pilot: uniform-prior anonymous VCG redistribution optimum is `10/3` on the 3-agent `{0,1/2,1}` grid | `src/mechanism_discovery/vcg_redistribution.py`, `tests/test_vcg_redistribution.py` | SUPPORTED as an exact pilot only; certificate artifact not yet frozen |
| Phase II complete-oracle and counterexample-guided paths agree | same test file | SUPPORTED as a pilot only |
| Exact audit of Guo (2024)'s printed 3-agent formula yields efficiency `2/3` | `src/mechanism_discovery/published_rule_audit.py`, `artifacts/published_rule_audit.json` | SUPPORTED for the printed decimal formula |
| Guo (2024)'s printed 4-agent decimals have non-deficit witness `(0,1/2,1/2,1/2)` with shortfall `1/5000`; constant repair `1/20000` eliminates it | primary and independent audit modules, `scripts/run_published_rule_audit.py`, certificate artifact | SUPPORTED for displayed rounded coefficients only; does not infer a defect in unshared weights |
| Guo (2019) Equation (6) baseline is non-deficit on the frozen rational grids for `n=3..6`, but has poor small-`n` grid efficiency | `src/mechanism_discovery/guo_2019_baseline.py`, independent replay, `artifacts/guo_2019_grid_audit.json` | EXHAUSTIVELY VERIFIED ON THE STATED GRIDS; not a continuous or asymptotic reproof |
