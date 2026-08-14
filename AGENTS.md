# Experiment working instructions

## Mission

Read `PROMPT.md` completely before substantive work. Treat its research question, boundaries, claim discipline, required artifacts, and completion gate as authoritative.

## Execution

- Work autonomously within the permissions granted by the prompt and repository.
- Create and maintain a concrete goal when the active Codex product supports goals.
- Create `PROJECT_CHARTER.md`, `STATUS.md`, `EVIDENCE_INDEX.md`, `DECISION_LOG.md`, and `REPRODUCIBILITY_MANIFEST.md` before substantial implementation; keep them current at each phase gate.
- Plan briefly, then execute research, implementation, experiments, tests, and synthesis.
- Use parallel specialist agents only for genuinely separable work, independent replication, or adversarial review. Do not spawn a fixed number merely to consume capacity.
- Give each specialist a bounded deliverable and require the lead agent to integrate and verify its work; agent consensus is not independent confirmation.
- Continue from existing artifacts and logs; do not restart completed work after an interruption.
- Make bounded assumptions for routine choices, record them, and proceed.

## Research integrity

- Investigate current primary-source prior art before making novelty claims.
- Separate proven, empirically supported, observed, conjectured, refuted, and unknown claims.
- Preserve negative results, failed hypotheses, seeds, configurations, raw outputs, and compute measurements.
- Use untouched holdouts, credible baselines, leakage controls, sensitivity analysis, and independent verification where applicable.
- Report the highest evidence level actually achieved: foundation, useful artifact, candidate contribution, or independently confirmed contribution.
- Never present simulation, computational association, or preclinical evidence as real-world deployment, causation, clinical advice, or treatment.

## Repository and safety boundaries

- Keep this experiment in this repository; never create a nested Git repository.
- Preserve configured Git identity and do not add AI attribution or generated-by trailers.
- Never commit credentials, private data, restricted datasets, model caches, large weights, or unlicensed material.
- Do not use paid APIs, rent compute, create cloud resources, make purchases, send external messages, or perform regulated/high-impact actions without explicit approval.
- Prefer bounded local experiments first. Record CPU/GPU time, peak memory, dataset size, and estimated cost before proposing heavier compute.
- Commit coherent checkpoints after verification. Do not rewrite or discard user-authored history.

Completion is governed by `PROMPT.md`, not by the existence of a plausible prototype or polished narrative.
