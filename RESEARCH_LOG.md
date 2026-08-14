# Research log

2026-08-15 — Re-scoped after review. The prior two-agent and three-agent binary-table audits were retained as baselines but rejected as the headline study. Prior-art review selected the deterministic public-project efficiency/budget-balance frontier as the primary question.

2026-08-15 — Frozen the finite class: all anonymous monotone Boolean rules for three agents with values `{0,1,2}`, normalized critical payments, costs 1–6, and no-subsidy weak budget balance. The 10-state lattice has 16 monotone rules; no external solver or sampled search is used.

2026-08-15 — Implemented the primary verifier, independent serialized-table checker, cost-indexed frontier, seeded proposal probe, and held-out value-magnitude audit. The efficient rule fails budget balance; the exact frontier contains 4 accepted rules at cost 3 and contracts as cost increases.

2026-08-15 — Independent replay agrees on all 4 accepted cost-3 rows. Held-out `{0,1,2,3}` stress testing exposes 207 cost-coverage failures across thresholds 1–6. This negative result is preserved as a boundary condition, not omitted.

2026-08-15 — Added the exploratory cross-agent extension. Direct antichain enumeration gives 16/32/64 candidates for n=3/4/5; accepted counts are 4,4,4,1,1,1; 5,5,5,5,1,1,1,1; and 6,6,6,6,6,1,1,1,1,1. All 74 serialized accepted rows pass independent replay. An initial n=3..8 attempt exposed runaway scaling and was stopped; the bounded n=3..5 protocol and this limitation are recorded explicitly.
