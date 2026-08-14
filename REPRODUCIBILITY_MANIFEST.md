# Reproducibility manifest

Environment: Python 3.14 (stdlib only), local CPU, no network/data download, deterministic integer arithmetic. Repository commit and working-tree state are recorded by Git.

Commands:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/run_public_project_study.py
python3 scripts/verify_public_project_certificate.py
```

Expected public-study summary: 16 enumerated rules; cost-3 accepted count 4; accepted counts by cost `4,4,4,1,1,1`; independent failures 0; held-out failures 207.

Artifacts are regenerated, not hand-edited: `artifacts/public_project_study.json`, `artifacts/public_project_certificate.json`, `artifacts/public_project_frontier.csv`, `reports/public_project_frontier.svg`. Run `sha256sum` after the final clean run; this manifest is updated with the resulting hashes before commit.

Frozen hashes for the clean run:

```text
configs/public_project_study.json       57407aea68db75d133521ef03cc80560880a102d7d42821264ee6e53a7d0f68e
artifacts/public_project_study.json     74c830d7cbf79a1aa966c8cd3acb91f4239d5083747a7ed44862f78a14e78551
artifacts/public_project_certificate.json 4f4390967fb8223c12bfb63f3df50945fd62eca92ea34ec817a1b5cfdf08037d
artifacts/public_project_frontier.csv   18bfe664fb845cc25bddb2f82368ed9864dc85a6bba2e1192cb9d0aa594bb3d5
reports/public_project_frontier.svg     fe2f6e1d346aee94b2470be42f0da5d2217f547058ce4c0f83547d7d7ba34b5e
```
