# Scaling-extension protocol

This is an explicitly exploratory extension of the frozen three-agent study,
not a retroactive claim that the original preregistration covered additional
agent counts. The extension was frozen before the final artifact regeneration
on 2026-08-15.

- Domain: values `{0,1,2}`, deterministic anonymous monotone Boolean rules,
  normalized discrete critical payments, the same DSIC, ex-post IR,
  feasibility, no-subsidy, all-maximum-build, and weak-budget-balance checks.
- Agent counts: `n=3,4,5`.
- Costs: every integer `c=1,...,2n` for each `n`.
- Search: enumerate every upward-closed allocation table by its minimal active
  antichain; do not sample or tune after seeing results.
- Primary report: candidate count, accepted count, minimum worst-case welfare
  regret, and all serialized accepted rows for every `(n,c)` pair.
- Confirmation: the standalone checker replays every serialized accepted row;
  any failure is retained rather than removed.
- Scope: this extension tests finite scaling and does not establish a theorem
  for arbitrary `n`, continuous values, randomized mechanisms, or unrestricted
  transfers.
