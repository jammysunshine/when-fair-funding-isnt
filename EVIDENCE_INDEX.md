# Evidence index

| Claim | Evidence | Status |
|---|---|---|
| All 16 anonymous monotone rules were enumerated | `scripts/run_public_project_study.py`, `artifacts/public_project_study.json` | SUPPORTED on frozen domain |
| Antichain enumeration is exact for n=3,4,5 | `src/mechanism_discovery/public_project.py`, `artifacts/public_project_scaling.csv` | SUPPORTED on finite domains |
| Four rules satisfy the cost-3 predicate | `artifacts/public_project_study.json` | SUPPORTED on frozen domain |
| 74 cross-agent accepted rows replay independently | `scripts/verify_public_project_certificate.py`, `artifacts/public_project_certificate.json` | SUPPORTED |
| Efficient critical-payment rule can fail no-deficit | `COUNTEREXAMPLES.md`, witness in study JSON | SUPPORTED |
| Cost frontier contracts as cost rises | frontier CSV/SVG and RESULTS.md | SUPPORTED descriptively |
| Finite rule generalizes to value 3 | held-out certificate | REFUTED / 207 failures |
| Pattern beyond n=5, continuous/general novelty | none | UNKNOWN / explicitly not claimed |
