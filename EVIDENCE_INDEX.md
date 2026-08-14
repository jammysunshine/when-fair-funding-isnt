# Evidence Index

| Claim | Supporting artifact/check |
| --- | --- |
| Domain, predicates, baseline frozen | `PROJECT_CHARTER.md`, `PREREGISTRATION.md`, `MECHANISM_SPEC.md`, configs |
| Every candidate table checked | `src/mechanism_discovery/search.py`, result JSON (`1,296`) |
| Four-table accepted frontier | result JSON, certificate, `frontier.csv`, `frontier.svg` |
| Independent agreement | certificate frontier digests; independent verifier test |
| Baseline reproduction | result JSON baseline records; baseline tests |
| No strict welfare improver | certificate empty improver list; `NEGATIVE_RESULTS.md` |
| Held-out/adversarial bounded robustness | confirmation config, `adversarial_audit.py`, certificate |
| Failure witnesses | verifier regression tests, certificate minimal DSIC witness |
| Prior-art and claim boundaries | `PRIOR_ART.md`, `SOURCES.json`, `CLAIM_LEDGER.md`, `LIMITATIONS.md` |
