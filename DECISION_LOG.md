# Decision log

2026-08-15 (before main run): replace the small binary-table headline with a public-project efficiency/budget-balance frontier. Rationale: it is anchored in primary literature and has a nontrivial cost-indexed objective.

2026-08-15 (before main run): restrict to all anonymous monotone rules on the 10-state three-agent, three-level lattice. Rationale: exact completeness is more defensible than a large sampled mechanism class.

2026-08-15 (before main run): normalize payments to discrete critical values and forbid subsidies when the project is absent. Rationale: fixes a canonical single-parameter DSIC/IR class and makes budget coverage falsifiable.

2026-08-15 (after run): retain the held-out 207 failures. Rationale: they are a boundary result, not an inconvenient subgroup.

2026-08-15 (extension): replace brute-force Boolean-mask scanning with direct minimal-active-state antichain enumeration. An initial exploratory n=3..8 run was stopped after excessive CPU growth; the protocol was narrowed to exact n=3..5 and the known-anonymous checks were optimized, with all serialized rows still replayed by the full independent checker.

2026-08-15 (publication review): retain the finite certificate benchmark as the
paper's contribution and explicitly reject claims of a new general theorem,
unrestricted mechanism novelty, or guaranteed acceptance. Rationale: the
exact finite result is strong and auditable, while the broader claims are not
supported by the current domain.

2026-08-15 (publication review): rank the Journal of Mechanism and Institution
Design first, AAMAS journal second, and GEB/JAIR only after a stronger theorem
or broader algorithmic contribution. Rationale: match the current evidence to
the stated editorial scope and bar.

2026-08-15 (sensitivity extension): run a bounded exact `max_value=3` lattice
check after the preregistered analysis. Keep it labeled exploratory rather than
folding it into the headline; it adds a value-magnitude sensitivity result
without changing the frozen acceptance criterion.
