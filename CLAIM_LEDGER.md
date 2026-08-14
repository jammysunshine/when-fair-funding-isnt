# Claim Ledger

| Claim | Status | Evidence |
| --- | --- | --- |
| Exactly four of 1,296 frozen tables satisfy all primary constraints | FORMALLY VERIFIED ON FINITE DOMAIN | `artifacts/experiment_67_independent_certificate.json`; both enumerators; regression test |
| Independent checker returns the identical accepted set | INDEPENDENTLY VERIFIED | certificate frontier digests and `test_independent_enumerator_matches_primary_frontier` |
| `anonymous_or` is an accepted baseline | REPRODUCED | result artifact; both checker records; tests |
| No accepted mechanism strictly improves baseline uniform welfare | EXHAUSTIVE NEGATIVE RESULT | certificate `strict_uniform_welfare_improvers_over_baseline: []` |
| No accepted table is neutral | EXHAUSTIVE NEGATIVE RESULT | certificate witnesses and verifier neutrality field |
| Held-out coalition and magnitude perturbation audits pass for baseline | BOUNDED EMPIRICAL AUDIT | `configs/confirmation_67.json`, `adversarial_audit.py`, certificate |
| Seeded evolutionary loop rediscovers an accepted frontier table | EMPIRICALLY EVALUATED | result artifact, seed 67 |
| A novel or general mechanism-design theorem exists | UNKNOWN / OUT OF SCOPE | prior-art review and limitations |
| Anti-agent-0 zero-transfer rule is DSIC | REFUTED | witness regression test and certificate counterexample |
