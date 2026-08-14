# Reproducibility Manifest

Environment: Python 3 standard library; no downloads, packages, APIs, cloud, or paid compute. Frozen profile order is `(0,0),(0,1),(1,0),(1,1)`. Seed `67`; evolutionary population `64`; generations `40`; candidate count `1,296`.

Run:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/run_experiment.py
python3 scripts/verify_certificates.py
sha256sum configs/experiment_67.json configs/confirmation_67.json artifacts/experiment_67_results.json artifacts/experiment_67_independent_certificate.json artifacts/frontier.csv reports/frontier.svg
```

Frozen configuration hashes: `configs/experiment_67.json` SHA-256 `cce3d57be6fbcc021c4fa8da9f7785bf2a11a9645b8a15a13176fd9b1894d1d3`; `configs/confirmation_67.json` SHA-256 `3f2553cf3237dc13dd335bc60e672d68749832490cd8ecb8fa9ee15016650f3a`. The run must report 13 passing tests, 1,296 candidates, 4 accepted tables, and a primary/independent frontier digest of `3a729b20545161e401e7689ef4f3b491ce22269c9ecb49ef76e82d38145ab6e2`.

Generated paths and SHA-256: `artifacts/experiment_67_results.json` (`bfa20cc035bbe22e34502a183cb2dd170043ffed2ad5467c405cc8e0d9fd75cb`), `artifacts/experiment_67_independent_certificate.json` (`d2293e8cda3ec35b2209de2dee4ab371f52c3e4ec29e28cca22f9de0d4313aeb`), `artifacts/frontier.csv` (`e1c7b7d3de33f4b029616b2a524fbe8a220fa899011e2085b479035653ab45b3`), and `reports/frontier.svg` (`898b00d046c6c04eac759a95bba4eada0f13e8700132f370dd08dd381535004f`). No nondeterminism is expected.
