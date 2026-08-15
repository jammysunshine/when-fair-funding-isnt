# Research log

2026-08-15 — Re-scoped after review. The prior two-agent and three-agent binary-table audits were retained as baselines but rejected as the headline study. Prior-art review selected the deterministic public-project efficiency/budget-balance frontier as the primary question.

2026-08-15 — Frozen the finite class: all anonymous monotone Boolean rules for three agents with values `{0,1,2}`, normalized critical payments, costs 1–6, and no-subsidy weak budget balance. The 10-state lattice has 16 monotone rules; no external solver or sampled search is used.

2026-08-15 — Implemented the primary verifier, independent serialized-table checker, cost-indexed frontier, seeded proposal probe, and held-out value-magnitude audit. The efficient rule fails budget balance; the exact frontier contains 4 accepted rules at cost 3 and contracts as cost increases.

2026-08-15 — Independent replay agrees on all 4 accepted cost-3 rows. Held-out `{0,1,2,3}` stress testing exposes 207 cost-coverage failures across thresholds 1–6. This negative result is preserved as a boundary condition, not omitted.

2026-08-15 — Added the exploratory cross-agent extension. Direct antichain enumeration gives 16/32/64 candidates for n=3/4/5; accepted counts are 4,4,4,1,1,1; 5,5,5,5,1,1,1,1; and 6,6,6,6,6,1,1,1,1,1. All 74 serialized accepted rows pass independent replay. An initial n=3..8 attempt exposed runaway scaling and was stopped; the bounded n=3..5 protocol and this limitation are recorded explicitly.

2026-08-15 — Refreshed the positioning review with public-project
characterization, automated mechanism-design, and learned-mechanism sources.
The manuscript now separates the finite certificate contribution from claims
that would require a theorem or broader mechanism class. A journal-fit plan was
added with a first target chosen by scope rather than prestige.

2026-08-15 — Ran the bounded exact value-lattice sensitivity extension. For
three agents and values `{0,1,2,3}`, the 20-state lattice yields 66 anonymous
monotone rules; accepted counts over costs 1–9 are
15,15,15,4,4,4,1,1,1. All 60 serialized accepted rows pass the independent
checker. This is recorded as exploratory and does not alter the preregistered
headline.

2026-08-15 — Ran the six-agent exact extension. Each of costs `1..12` has 128
anonymous monotone candidates over 28 sorted states; accepted counts are
`7,7,7,7,7,7,1,1,1,1,1,1`. All 48 serialized accepted rows pass the independent
permutation-aware checker. The run took 106.191 seconds and peaked at
29,671,424 bytes on Darwin. This is finite evidence through six agents, not an
asymptotic theorem; n=7 remains outside the declared result because of the
measured computational ceiling.

2026-08-15 — Derived the all-agent ternary frontier. Anonymity and budget at
the all-2 profile force the critical threshold to 2 when `c>n`, leaving only
the all-2 rule; when `c<=n`, monotonicity excludes zero reports and the positive
chain yields exactly the suffix rules `q_k`, `k=0..n`. The construction script
checks n=1..12 (806 mechanisms), replays n<=5 independently, and cross-checks
the n=3 and n=6 stored artifacts.

2026-08-15 — Began a separately scoped executable-formula audit program after
the finite search was found to overlap stronger public-project mechanism
design work. The corpus registry requires a public closed form, a stated
convention, and an independent evaluator; it excludes unavailable neural
weights and ambiguous displays rather than guessing them. The AAAI-2024
four-agent printed decimals have an exact `1/5000` no-deficit shortfall, while
the paper's stated uniform correction binds at `1/20000` per Groves term.

2026-08-15 — Added a separately preregistered positive control: IJCAI-2019
Equation (2), which reproduces a three-agent optimum credited to Guo and Shen
(2017). Exact continuous arrangement enumeration and a standalone replay both
give efficiency `2/3`; it differs from the later AAAI-2024 printed formula at
`(0,1/3,1/3)`. During the PRIMA-2016 audit, rendered-PDF inspection corrected
an initially missed outer denominator and a max threshold before any artifact
was accepted. This is retained as a transcription-risk finding, not hidden.

2026-08-15 — Frozen and executed the Phase-VI uniform-repair study. The exact
identity that a per-term output-bias offset changes total slack by `n*delta`
derives the smallest scalar non-deficit repair from the baseline certificate.
All seven repaired sources passed compiler/direct replay and exact-real Z3
no-deficit challenges. Five synthetic fixtures require large offsets, which is
retained as negative evidence: the result is a certified repair primitive, not
an economically persuasive new mechanism.

2026-08-15 — Preregistered and executed the Phase-VII budget--IR trade-off on
the unchanged seven-source corpus. The scalar repair lowers each utility by
its offset; all repaired sources fail ex-post IR. This is retained as the
decisive negative result preventing an unsupported mechanism-quality claim.
