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
python3 scripts/run_published_rule_audit.py
python3 scripts/run_guo_2019_baseline_audit.py
python3 scripts/run_guo_2016_baseline_audit.py
python3 scripts/run_guo_2019_three_agent_optimal_audit.py
python3 scripts/run_max_affine_certification.py
python3 scripts/verify_max_affine_certificate.py
python3 scripts/verify_source_network_certificates.py
python3 scripts/run_relu_benchmark.py
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
The published-rule audit emits `artifacts/published_rule_audit.json`; the
frozen clean-run SHA-256 is
`4056655ed759dacaf561b36344b206745f98066e7d361bb78ed8a68bf50850df`.
The Phase III positive-control audit emits
`artifacts/guo_2019_three_agent_optimal_audit.json`; its SHA-256 is
`45df2f83d27eb70dd4874c7faf1ee3e764b8f4ab194c6df6269afce3a9b69a2b`.
The Phase IV generic shallow-max-affine certificate emits
`artifacts/max_affine_certification.json`; its SHA-256 is
`3bdb0c02b39107994f989894d1fcbe04157e0dce6814004e1cd11b217916f882`.
Its independent replay is `artifacts/max_affine_independent_certificate.json`;
its SHA-256 is `8b89a8ca8b4ed937f865be2b33c72f7d0d35518870c8bfbc3a9644bd13194f98`.
The direct source-network replay writes
`artifacts/max_affine_source_network_certificate.json`; it must match each
embedded public source network without reading a compiled expression.
Its frozen SHA-256 is
`1bcde48fc4f23e58a510027310fc723195a6553f23354472c904332111745d4f`.
The frozen Phase-V source/compiler crosscheck uses
`configs/relu_benchmark.json` (SHA-256
`0eadd9b57f377174cc370af5c122db81e09f00e2d98c1a7022c72f8d4c79a6e8`)
and emits `artifacts/relu_benchmark_results.json` (SHA-256
`8589d83fb5fcd4b3c9721ff4d3c2de2d7723c71a08fb5c46a518c88f96fd5cbd`).
It contains six deterministic rational fixtures over 3--5 agents; both exact
routes agree on every field after the retained zero-output-boundary bug fix.
The largest frozen entry uses 22 arrangement planes, evaluates 7,315 exact
four-plane bases, and retains 116 feasible vertices.

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
artifacts/published_rule_audit.json       4056655ed759dacaf561b36344b206745f98066e7d361bb78ed8a68bf50850df
artifacts/guo_2019_grid_audit.json        61f4dc2efd184375e0ebd79a94dcecfe98a24005e0f78899087a56425ad48fb3
artifacts/guo_2016_grid_audit.json        92e3078d55320c4d6a9130cab16a07d0d264aef3db648244d61cb97adf7bdbf2
artifacts/guo_2019_three_agent_optimal_audit.json 45df2f83d27eb70dd4874c7faf1ee3e764b8f4ab194c6df6269afce3a9b69a2b
artifacts/max_affine_certification.json 3bdb0c02b39107994f989894d1fcbe04157e0dce6814004e1cd11b217916f882
artifacts/max_affine_independent_certificate.json 8b89a8ca8b4ed937f865be2b33c72f7d0d35518870c8bfbc3a9644bd13194f98
artifacts/max_affine_source_network_certificate.json 1bcde48fc4f23e58a510027310fc723195a6553f23354472c904332111745d4f
configs/relu_benchmark.json 0eadd9b57f377174cc370af5c122db81e09f00e2d98c1a7022c72f8d4c79a6e8
artifacts/relu_benchmark_results.json 8589d83fb5fcd4b3c9721ff4d3c2de2d7723c71a08fb5c46a518c88f96fd5cbd
```
