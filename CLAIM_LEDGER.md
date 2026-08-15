# Claim ledger

## FORMALLY VERIFIED / EXHAUSTIVELY VERIFIED ON DOMAIN

- In the declared ternary class, for every `n>=1`, accepted counts are `n+1`
  for `1<=c<=n`, one for `n<c<=2n`, and zero for `c>2n`; accepted rules are
  exactly the suffix family in `PUBLIC_PROJECT_THEOREM.md`.
- The implementation enumerates all 16 anonymous monotone Boolean allocation rules for the frozen three-agent, three-level domain.
- The antichain implementation enumerates 16, 32, and 64 rules exactly for `n=3,4,5` on the declared domains.
- Every reported accepted row passes the primary verifier; all 74 serialized cross-agent rows pass the independent checker.
- The efficient critical-payment rule has explicit weak-budget-balance witnesses at cost 3.
- For the declared rational sum-of-max/min-affine language on an ordered unit
  cube, the arrangement-vertex reduction exactly certifies the reported
  charge-ratio, efficiency, and budget-slack extrema.

## EMPIRICALLY EVALUATED

- Uniform finite expected welfare and worst-case regret for costs 1–6.
- Seeded sum-threshold proposal probe and held-out value-magnitude audit.
- Cross-agent accepted counts and finite welfare regret for costs `1..2n`.
- Construction certificate over n=1..12, with bounded primary and independent replay.

## REFUTED / UNKNOWN

- Held-out cost coverage across values `{0,1,2,3}` is refuted for thresholds 1–6 (207 failures).
- No claim of universal optimality, randomized optimality, deployment effect,
  or generalization beyond the ternary class is made.
- The certificate method is not established for arbitrary neural networks,
  opaque learned weights, unrestricted programs, or higher-dimensional
  instances beyond the recorded computational envelope.
