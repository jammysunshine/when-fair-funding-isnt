# Claim ledger

## FORMALLY VERIFIED / EXHAUSTIVELY VERIFIED ON DOMAIN

- In the declared finite integer-value critical-payment class, for every
  `n>=1`, cap `m>=1`, and integer cost `c`, accepted rules are exactly the
  nonempty upward-closed subsets of the sorted restricted lattice
  `{ceil(c/n),...,m}^n`; none exists when `c>nm`. The ternary suffix result is
  its `m=2` corollary. The proof is human-checkable and the untouched
  `n=3,m=4,c=1..12` confirmation has exact rule-set equality with 255
  independent accepted-rule replays and zero failures.
- The implementation enumerates all 16 anonymous monotone Boolean allocation rules for the frozen three-agent, three-level domain.
- The antichain implementation enumerates 16, 32, and 64 rules exactly for `n=3,4,5` on the declared domains.
- Every reported accepted row passes the primary verifier; all 74 serialized cross-agent rows pass the independent checker.
- In the finite integer-value public-project lattice (`n=3, max_value=2`), the
  cap-2 coalition-robust frontier at cost 3 is exactly
  `{anonymous_monotone_mask_512, anonymous_monotone_mask_960}` after checking all
  serialized DSIC frontier survivors.
- The efficient critical-payment rule has explicit weak-budget-balance witnesses at cost 3.
- For the declared rational sum-of-max/min-affine language on an ordered unit
  cube, the arrangement-vertex reduction exactly certifies the reported
  charge-ratio, efficiency, and budget-slack extrema.
- For six preregistered rational one-hidden-layer ReLU fixtures (three to five
  agents), source-direct and compiler-lowered certificates agree exactly;
  exact-real Z3 returns `unsat` for all 18 recorded strict-bound queries and
  independently validates the extremum witnesses.
- For a declared `n`-term deleted-input rational ReLU charge, the smallest
  nonnegative uniform output-bias offset that eliminates a certified minimum
  slack `s` is `max(0,-s/n)`. The Phase-VI seven-source corpus is certified
  through compiled, direct-source, and Z3 exact-real routes.
- For cap sizes `2` and `3` on `n=3..6`, coalition-robustness filtering of the
  DSIC frontier is reproducible at every serialized row, and the independent
  checker produces 0 selected failures on configured selected-cost checks.
- In the declared efficient-Groves model, the uniform offset lowers every
  truthful utility by exactly that offset. Across the frozen Phase-VII corpus,
  no repaired source is simultaneously no-deficit and ex-post IR; compiler,
  direct-source, and Z3 routes agree.
- The canonical efficient/pivotal (welfare-maximizing sum-threshold,
  critical-value payment) mechanism is single-agent DSIC on every domain
  tested but fails coalition-cap-2 DSIC in 66 of 75 audited `(domain, n,
  cost)` rows, independently of its separate weak-budget-balance deficit;
  the independent checker reproduces all 75 rows with 0 mismatches.
- The same canonical efficient/pivotal mechanism is manipulable by a false-name
  attack: a single real agent controlling their own report slot plus fake
  slots gains against 48 of 72 audited `(n_real, cost, fake_budget)` rows for
  fake budgets 1-2 across `n_real=3,4,5`, while the zero-fake-budget positive
  control shows no manipulable rows anywhere; an independent closed-form
  reimplementation (no import of `public_project.py`) reproduces all 72 rows'
  manipulable counts with 0 mismatches.
- (General theorem, not a search result.) For the sum-threshold/critical-value
  public-project mechanism, for every integer `n>=2`, `max_value=m>=1`, and
  `cost c<=(n-1)*m`, the grand-coalition deviation "every agent reports `m`"
  builds the project and forces payment 0 for every agent (the other `n-1`
  agents' reports alone already sum to `(n-1)*m>=c`), weakly Pareto-dominating
  truthful reporting for the whole coalition and strictly so whenever some
  agent's true value is positive. This closed-form condition is proven, not
  searched, and holds for every `(n,m,c)` satisfying it, not only the domains
  audited above. It has zero false positives against the baseline-audit
  artifact's 75 rows (every row it predicts fragile is fragile in the search
  data) and directly explains that artifact's single robust exception: at
  `cost=n*m` exactly, `(n-1)*m<n*m` so the construction never applies, and a
  separate closed-form argument (checked by exhaustive enumeration for
  `n=3,4` and `m=2,3`, zero counterexamples) shows any proper-coalition
  deviation that reaches the threshold at `cost=n*m` forces coalition members
  to pay exactly their own report, eliminating any free-ride gain.
- (Complete characterization, not a search result.) For the same mechanism, the
  minimum achievable total coalition payment for a size-`k` coalition against
  outsider true-value sum `S_O` is exactly
  `k*max(0,(cost-S_O)-(k-1)*m)`, and the worst-case (payment-maximizing)
  truthful distribution of a fixed coalition value-sum is the bang-bang
  extremal split (as many members at `m` as possible, one remainder, rest 0);
  both are proven by convexity of the critical-value payment. Combining them
  gives an existence check for coalition-cap-`k` manipulability by bounded
  integer sweep, with no report-level search. This reproduces the baseline
  audit's exact `min_failing_coalition_size` on all 75 rows (`75/75` exact
  matches, not merely zero false positives) and evaluates at agent counts
  (e.g. `n=20`) far beyond brute-force reach.

## EMPIRICALLY EVALUATED

- Uniform finite expected welfare and worst-case regret for costs 1–6.
- Seeded sum-threshold proposal probe and held-out value-magnitude audit.
- Cross-agent accepted counts and finite welfare regret for costs `1..2n`.
- Construction certificate over n=1..12, with bounded primary and independent replay.

## REFUTED / UNKNOWN

- Held-out cost coverage across values `{0,1,2,3}` is refuted for thresholds 1–6 (207 failures).
- No claim of universal optimality, randomized optimality, deployment effect,
  or generalization beyond the finite integer-value critical-payment class is made.
- The certificate method is not established for arbitrary neural networks,
  opaque learned weights, unrestricted programs, arbitrary depth, or instances
  beyond the recorded three-to-five-agent computational envelope.
- Uniform repair does not establish individual rationality, welfare quality,
  budget optimality outside its scalar family, or a useful economic mechanism;
  its synthetic large-offset cases are explicitly negative evidence against
  treating repair feasibility as practical mechanism quality.
- This all-fail trade-off result concerns only the fixed uniform-bias family
  and seven declared sources; it is not an impossibility theorem for arbitrary
  Groves redistribution mechanisms.
