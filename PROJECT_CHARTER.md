# Project Charter

Status: original study frozen 2026-08-15; Phase V is active. The original
binary-table audit remains a baseline and Phase II--IV results remain bounded
replication evidence.

## Phase II feasibility question (active; not yet a headline claim)

Can a certificate-first exact verifier reproduce and audit automated VCG-redistribution design under the same public-project model, using a counterexample-guided path and an independent replay? The immediate deliverable is a falsifiable replication benchmark: exact continuous audits of the explicit 3- and 4-agent printed rules in Guo (2024), plus a finite-grid negative control. This phase will not claim a newly discovered redistribution mechanism: prior work already reports neural/MIP mechanisms through five agents.

## Primary question

Within a finite public-project domain, how much welfare is lost when deterministic anonymous DSIC and ex-post IR mechanisms must cover a known cost without deficit, and does exact automated search reveal a cost-indexed frontier that survives an independent checker and value-magnitude stress test?

## Frozen study

Main study: three agents; values `{0,1,2}`; binary project; costs `1..6`; all anonymous monotone Boolean allocation rules; normalized discrete critical payments; uniform finite evaluation distribution. There are 10 anonymous states and 16 rules, exhaustively enumerated at every cost. A post-hoc theorem extension characterizes every `n>=1` in this same ternary class; exact searches for `n=3..6` are computational cross-checks governed by the scaling protocols.

Acceptance: feasibility, DSIC, ex-post IR, anonymity, no subsidy when the project is absent, and weak budget balance when it is built. The rule must build at the all-2 profile. Primary metric: worst-case additive welfare regret against the efficient allocation; secondary metric: expected welfare. Threshold: complete enumeration, independent replay, and a held-out audit, with every failure retained.

Strong comparators: efficient critical-payment rule (expected to fail budget balance), all accepted frontier rules, and the seeded sum-threshold proposal probe. The original two-agent and three-agent audits are regression baselines only.

## Resource ceiling and non-goals

Local CPU only, no paid API/cloud/real data, under 10 minutes per complete run and under 100 MB of generated artifacts. No claim is made for continuous values, randomized mechanisms, Bayesian optimality, or a general impossibility theorem. The useful fallback is a complete finite certificate and a falsified generalization boundary.

## Evidence target

Candidate contribution/useful artifact: exact narrow all-agent characterization plus independent machine-checkable certificate and finite scaling cross-check. Any broader publication claim requires external novelty review, richer mechanism classes, and independent replication.

Phase V question: can a serialized public rational ReLU rule be compiled into
the exact certificate language, rather than transcribed as bespoke formula
code, while retaining an independent replay? The initial 4-agent control is a
validation target, not a claim of generality. Promotion beyond a useful
replication artifact requires the five gates in `RESEARCH_GAP_AUDIT.md`.
