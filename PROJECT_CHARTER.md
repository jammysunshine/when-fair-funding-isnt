# Project Charter

Status: original study frozen 2026-08-15; Phase VII is complete. Phase VIII
has a preregistered, independently replayed finite value-lattice theorem
confirmation. A separate constrained-synthesis pilot was withdrawn at its
semantic-baseline gate because it rediscovered pivotal VCG. The original
binary-table audit remains a baseline and Phase II--IV results remain bounded
replication evidence.
Phase X adds a bounded coalition-robustness extension on the same finite class:
for cap-2 deviations in the three-agent ternary frontier, only 2 of 4 DSIC
survivors remain at cost 3, and those rows are independently replayed.

## Phase II feasibility question (active; not yet a headline claim)

Can a certificate-first exact verifier reproduce and audit automated VCG-redistribution design under the same public-project model, using a counterexample-guided path and an independent replay? The immediate deliverable is a falsifiable replication benchmark: exact continuous audits of the explicit 3- and 4-agent printed rules in Guo (2024), plus a finite-grid negative control. This phase will not claim a newly discovered redistribution mechanism: prior work already reports neural/MIP mechanisms through five agents.

## Primary question

Within a finite public-project domain, how much welfare is lost when deterministic anonymous DSIC and ex-post IR mechanisms must cover a known cost without deficit, and does exact automated search reveal a cost-indexed frontier that survives an independent checker and value-magnitude stress test?

## Frozen study

Main study: three agents; values `{0,1,2}`; binary project; costs `1..6`; all anonymous monotone Boolean allocation rules; normalized discrete critical payments; uniform finite evaluation distribution. There are 10 anonymous states and 16 rules, exhaustively enumerated at every cost. The finite-lattice extension now characterizes every integer cap `m>=1` and every `n>=1` in the same critical-payment class; the preregistered `n=3,m=4,c=1..12` run is an exact, independent confirmation. The earlier exact searches for `n=3..6` are computational cross-checks.

Acceptance: feasibility, DSIC, ex-post IR, anonymity, no subsidy when the project is absent, and weak budget balance when it is built. The rule must build at the all-2 profile. Primary metric: worst-case additive welfare regret against the efficient allocation; secondary metric: expected welfare. Threshold: complete enumeration, independent replay, and a held-out audit, with every failure retained.

Strong comparators: efficient critical-payment rule (expected to fail budget balance), all accepted frontier rules, and the seeded sum-threshold proposal probe. The original two-agent and three-agent audits are regression baselines only.

## Resource ceiling and non-goals

Local CPU only, no paid API/cloud/real data, under 10 minutes per complete run and under 100 MB of generated artifacts. No claim is made for continuous values, randomized mechanisms, Bayesian optimality, or a general impossibility theorem. The useful fallback is a complete finite certificate and a falsified generalization boundary.

## Evidence target

Candidate contribution/useful artifact: exact finite-lattice characterization plus independent machine-checkable certificate and preregistered full-domain confirmation. Any broader publication claim requires external novelty review, richer mechanism classes, and independent replication.

Phase V question: can a serialized public rational ReLU rule be compiled into
the exact certificate language, rather than transcribed as bespoke formula
code, while retaining an independent replay? The initial 4-agent control is a
validation target, not a claim of generality. Promotion beyond a useful
replication artifact requires the five gates in `RESEARCH_GAP_AUDIT.md`.

Phase V falsification extension (frozen before its run): the same declared
source networks must be certified by a direct activation-boundary enumerator
that does not consume compiled expressions. Exact equality of every reported
metric and witness is the acceptance predicate; any mismatch is retained as a
failure. This crosscheck is a verifier comparison, not a new mechanism search.

Phase V benchmark extension: `configs/relu_benchmark.json` fixes six
deterministic rational one-hidden-layer fixtures across 3--5 agents, split
before execution into development and confirmation cases. The acceptance
predicate is exact equality between compiled and source-only certificates;
the bounded compute metric is candidate bases. This is a stress test for the
declared verifier class only, with no claim about neural training or new
economic mechanisms.

Phase V solver extension: each frozen benchmark certificate is challenged by
an external Z3 exact-real satisfiability query for a strict improvement in its
reported extrema. Acceptance requires `unsat` for all three queries per case
and direct rational validation of each witness. This is an adversarial solver
check for the fixed source language, not a generic MIP/SMT performance study.

Phase VI repair extension: for a declared deleted-input rational ReLU source,
compute the exact smallest nonnegative uniform output-bias offset that removes
the certificate's minimum budget deficit. The frozen corpus is the printed
four-agent source plus all six Phase-V fixtures; every entry is reported. The
claim is restricted to this scalar repair family and requires compiler,
direct-source, and exact-real solver non-deficit checks.

Phase VII trade-off extension: keep the Phase-VI source corpus and repair
family fixed, and certify whether the minimal no-deficit repair also preserves
ex-post IR. This gate is deliberately falsifying: all seven repaired sources
fail IR under the stated efficient-Groves convention. It rules out claiming
that scalar repair itself discovers a viable mechanism.

Phase VIII baseline gate: before any constrained synthesis is preregistered,
the proposed comparator must be symbolically checked against the normalized
pivotal VCG term. The first four-value pilot failed this gate: its apparent
candidate was exactly `max(sum(theta_-i), 2/3)`, the three-agent pivotal VCG
term, while its comparator incorrectly used threshold one. The raw output is
preserved in `artifacts/withdrawn_phase_viii_comparator_failure.json`; it is a
negative control, not a discovery. A viable next question must quantify a
property distinct from known pivotal VCG and include this equivalence test.

Phase VIII finite-lattice theorem: before its `m=4` confirmation run, freeze
the claim that accepted active sets are exactly the nonempty upward-closed sets
inside `{ceil(c/n),...,m}^n`. Require full-domain rule-set equality and an
independent replay of every accepted rule. The run met those criteria for
`n=3,m=4,c=1..12`, with 255 accepted-rule replays and zero failures. This is
an exact result for the declared discrete critical-payment model, not a claim
about continuous values or a new neural mechanism.

Phase X coalition-robustness extension: run cap-2 coalition replay on all costs
`1..6` at three agents, then scale survivors to `n=4` and `n=5` with cap 3 as
an exact finite sensitivity and robustness stress test. This extension is
post-hoc relative to the Phase VIII frozen objective and is logged as a falsification
supplement.

Phase IX question: does the source-aware exact rational-ReLU certificate remain
semantically consistent as the public-project dimension rises from three to
seven agents? This bounded verifier study requires five pre-fixed sources,
compiler/direct-source equality, detected output-bias mutation, and three
exact-real Z3 strict-counterexample challenges per source; it is not a
mechanism-discovery or learned-policy study.
