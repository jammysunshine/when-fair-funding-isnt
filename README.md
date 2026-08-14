# Research Experiment Workspace

This is the independent repository for Experiment 67, **Automated Mechanism Discovery**. Its complete research brief and completion gate are in [`PROMPT.md`](PROMPT.md). The frozen useful artifact is a complete finite search over 1,296 deterministic binary allocation/payment tables; start with [`REPLICATION_GUIDE.md`](REPLICATION_GUIDE.md).

## Start here

1. Read `PROMPT.md` before choosing tools, architecture, datasets, or claims.
2. Open this repository as its own Codex project and start a new top-level task.
3. Start with Terra as lead and paste the complete `PROMPT.md` as the first message.
4. Terra owns scope, the exact mechanism/verifier, baseline reproduction, and interpretation. It must not hand off until `HANDOFF.md` says `SAFE FOR LUNA HANDOFF`.
5. Luna may then execute only the frozen task queue recorded in `HANDOFF.md`; it must not change the specification, verifier semantics, success criteria, or conclusions.
5. Use worktrees only when multiple sessions need to edit this same experiment. Independent experiments belong in independent repositories.

## Working structure

- `src/` — reusable implementation
- `tests/` — automated correctness and regression tests
- `benchmarks/` — benchmark harnesses and frozen configurations
- `experiments/` — executable experimental definitions
- `notebooks/` — exploratory analysis that does not replace reproducible scripts
- `scripts/` — setup, data acquisition, reproduction, and verification commands
- `data/` — manifests, small fixtures, and data instructions
- `reports/` — research logs, results, limitations, replication notes, and paper drafts
- `PROJECT_CHARTER.md` — frozen primary question, success threshold, baseline, resource ceiling, non-goals, and fallback contribution
- `STATUS.md` — phase, evidence level, executed commands, blockers, and next action
- `EVIDENCE_INDEX.md` — headline claims mapped to their supporting or refuting evidence
- `DECISION_LOG.md` — consequential design choices, alternatives, timing, and rationale
- `REPRODUCIBILITY_MANIFEST.md` — pinned data/code/model versions, checksums, environment, seeds, hardware, commands, and expected outputs

The research prompt may require additional root-level artifacts. Its requirements take precedence over this starter layout.

## Evidence and storage

Keep code, configurations, small fixtures, summaries, and machine-readable evidence in Git. Do not commit secrets, private data, restricted datasets, large model weights, caches, or generated build artifacts. Store large reproducible artifacts externally and record their source, license, checksum, acquisition command, and expected location in `data/README.md` or an artifact manifest.

GitHub synchronizes repository files; it does not transfer a running Codex session or its compute. Clone this repository on another machine to continue from committed artifacts.
