# Project Charter

Status: frozen 2026-08-14 (pre-results).

Primary question: in the frozen two-agent, binary-private-value direct-revelation domain, can exhaustive search map every deterministic allocation/payment table satisfying DSIC, ex-post IR, exact budget balance, and feasibility, and can a seeded evolutionary proposal loop rediscover a feasible table?

Domain: agents `i∈{0,1}` have types/reports and alternatives in `{0,1}`. Value is one iff the chosen alternative equals type, otherwise zero. Transfers are integer payments in `{-1,0,1}` (positive means paid); utility is value minus payment. A mechanism is four outcomes, one per report profile. The outside option is zero.

Acceptance predicate: enumerate all 6^4 = 1,296 budget-balanced candidate tables. Accept only if every truthful profile and unilateral binary deviation passes DSIC and every truthful profile passes ex-post IR; all choices must be binary. The priority-majority baseline must pass the primary and independent checkers. This is an exact finite statement only.

Comparator: priority-majority (`choice=report_0`, zero payments); constants are included in enumeration. Experimental unit: one complete mechanism table, evaluated over all four profiles. Primary descriptive objectives: uniform expected welfare, uniform expected utility disparity, worst-case deviation regret, and integer table description length.

Ceiling: local Python standard library only; at most 5 CPU-minutes, 256 MB memory, zero paid/API/cloud cost. Target audience: mechanism-design and formal-methods researchers. Non-goals: continuous types, randomized mechanisms, general theorems, real-world deployment, coalition resistance, or novelty claims. Fallback contribution: a reproducible exhaustive finite frontier and counterexample-witness harness.
