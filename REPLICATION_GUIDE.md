# Replication Guide

From the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/run_experiment.py
python3 scripts/verify_certificates.py
sha256sum configs/experiment_67.json configs/confirmation_67.json artifacts/experiment_67_results.json artifacts/experiment_67_independent_certificate.json artifacts/frontier.csv reports/frontier.svg
```

Expected invariants: 13 tests pass; both JSON artifacts report 1,296 candidates and 4 accepted tables; certificate `set_equal` is true; frontier digest is `3a729b20545161e401e7689ef4f3b491ce22269c9ecb49ef76e82d38145ab6e2`; baseline is `anonymous_or` and accepted by both checkers.
