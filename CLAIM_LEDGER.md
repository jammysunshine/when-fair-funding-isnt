# Claim ledger

## FORMALLY VERIFIED / EXHAUSTIVELY VERIFIED ON DOMAIN

- The implementation enumerates all 16 anonymous monotone Boolean allocation rules for the frozen three-agent, three-level domain.
- The antichain implementation enumerates 16, 32, and 64 rules exactly for `n=3,4,5` on the declared domains.
- Every reported accepted row passes the primary verifier; all 74 serialized cross-agent rows pass the independent checker.
- The efficient critical-payment rule has explicit weak-budget-balance witnesses at cost 3.

## EMPIRICALLY EVALUATED

- Uniform finite expected welfare and worst-case regret for costs 1–6.
- Seeded sum-threshold proposal probe and held-out value-magnitude audit.
- Cross-agent accepted counts and finite welfare regret for costs `1..2n`.

## REFUTED / UNKNOWN

- Held-out cost coverage across values `{0,1,2,3}` is refuted for thresholds 1–6 (207 failures).
- No claim of a new asymptotic theorem, universal optimality, randomized optimality, or deployment effect is made; the observed `n+1` pattern remains unknown beyond `n=5`.
