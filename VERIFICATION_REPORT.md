# Verification Report

Commands: `python3 -m unittest discover -s tests -v`, `python3 scripts/run_experiment.py`, and `python3 scripts/verify_certificates.py`.

The primary and standalone row-table checker each enumerate all 1,296 candidates and accept exactly four tables. Their frontier SHA-256 is `3a729b20545161e401e7689ef4f3b491ce22269c9ecb49ef76e82d38145ab6e2`. The accepted tables are the two constants and the two anonymous monotone rules (AND/OR, equivalent to fixed-tie majority on this domain). The `anonymous_or` baseline passes both checkers; priority-majority/serial dictatorship is rejected by anonymity/fairness.

The certificate records no strict uniform-welfare improver over the baseline, held-out distributional evaluations, zero bounded coalition witnesses, zero `{0,1,2}` value-magnitude failures, and a minimal DSIC counterexample. The finite audit also records that no accepted table is neutral. These are exact or bounded claims only; the independent checker is a separate implementation, not an external lab replication.
