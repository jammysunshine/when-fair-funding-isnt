# Project Charter

Status: frozen 2026-08-15. The original binary-table audit is a baseline; the headline study is the public-project frontier below.

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
