# Reproducibility manifest

Environment: Python 3.14 (stdlib only), local CPU, no network/data download,
deterministic integer arithmetic. Repository commit and working-tree state are
recorded by Git.

Commands:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/run_public_project_study.py
python3 scripts/verify_public_project_certificate.py
python3 scripts/run_value_extension.py
python3 scripts/run_n6_extension.py
python3 scripts/verify_scaling_theorem.py
python3 -m unittest tests.test_vcg_redistribution -v
```

Expected summary: theorem construction checks for n=1..12 (806 constructed
mechanisms), with zero bounded replay failures; 16/32/64 candidates for `n=3,4,5`; accepted counts
`4,4,4,1,1,1`, `5,5,5,5,1,1,1,1`, and `6,6,6,6,6,1,1,1,1,1`; 74 cross-agent
rows; cross-agent independent failures 0; held-out failures 207.
The exploratory `n=3, max_value=3` extension has 66 candidates and accepted
counts `15,15,15,4,4,4,1,1,1`; all 60 serialized rows replay independently.
The exact six-agent extension has 128 candidates at each cost `1..12`, accepted
counts `7,7,7,7,7,7,1,1,1,1,1,1`, 48 serialized rows, and zero independent
replay failures. Its canonical digest is
`d13dfc940c38241ea21c4cc3f4abbbbda94fc012af643a1b9b4db0833963c5c7`.

Artifacts are regenerated, not hand-edited:
`artifacts/public_project_study.json`, `artifacts/public_project_certificate.json`,
`artifacts/public_project_scaling.csv`, `artifacts/public_project_frontier.csv`,
`artifacts/public_project_value_extension.json`,
`artifacts/public_project_n6_extension.json`, and
`reports/public_project_frontier.svg`.

Hashes for the clean run:

```text
configs/public_project_study.json          58d3de51c22a1136a5af8445bd2999b0067b0f439624ffab689026caa3808e58
artifacts/public_project_study.json        069096fd620b7ec995e57619c1edee8024718a705cf4e8506846d8763672dbbb
artifacts/public_project_certificate.json  59d43612156d6800e2163c809015ac6bdc5bd726d58c3041d82c718f8adf6760
artifacts/public_project_scaling.csv       ed52a586503579a1c7c929c6faae5a557bfbd095c735649f838680dd034b6b4b
artifacts/public_project_frontier.csv      18bfe664fb845cc25bddb2f82368ed9864dc85a6bba2e1192cb9d0aa594bb3d5
reports/public_project_frontier.svg        fe2f6e1d346aee94b2470be42f0da5d2217f547058ce4c0f83547d7d7ba34b5e
artifacts/public_project_value_extension.json c2e4d513ba464dd2a5de02ed4e0eaea064287d963c40d6f12fe18cc3cbb779b2
artifacts/public_project_n6_extension.json  9ecd187b249b4bcefe5b25b0ea233339a101be5cd4d41f455364fde15f43c4d4
artifacts/public_project_scaling_theorem.json  97dad770e4ffa74532c5546a9f3c170b2e266f669c9ca68bc111781065e09c6d
```
