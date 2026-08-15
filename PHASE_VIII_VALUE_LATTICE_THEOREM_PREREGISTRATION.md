# Phase VIII: value-lattice frontier theorem

Status: preregistered before confirmation execution on `max_value=4`.

## Claim under test

For `n` anonymous agents with integer reports in `{0,...,m}`, normalized
critical payments, monotone allocation, no payment when the project is absent,
ex-post IR, and weak budget balance at integer cost `c`, let
`k=ceil(c/n)`. A non-vacuous rule is accepted exactly when its active set is a
nonempty upward-closed subset of the sorted states whose smallest coordinate
is at least `k`. Thus there are no accepted rules for `c>nm`; otherwise the
accepted count equals the number of nonempty upper sets in the sorted
`{k,...,m}^n` state poset.

The proof obligation is two-sided: an active state below `k` must yield an
underfunded all-`m` profile by anonymity and monotonicity; every rule confined
to the restricted lattice must pass the exact verifier because all active
critical values are at least `k`.

## Frozen confirmation

- Primary untouched grid: `n=3`, `m=4`, all integer costs `1..12`.
- Comparator: exhaustive anonymous-monotone enumeration over the full
  `{0,...,4}^3` sorted-state lattice, using the existing primary verifier.
- Independent check: serialize every accepted full-lattice rule and replay it
  with `public_project_independent.py`; independently enumerate the restricted
  lattice for the predicted count.
- Acceptance: exact equality of the predicted and exhaustive accepted counts
  at every cost, exact equality of the serialized accepted rule sets, and zero
  independent failures. Any mismatch is a counterexample to the claim.
- Resource ceiling: local CPU only, at most ten minutes and 100 MB generated
  artifact data. The confirmation grid was not used in previous result tables.

## Scope

This is a theorem for the stated discrete critical-payment model, not a claim
about continuous values, arbitrary transfers, randomized mechanisms, or a
new neural mechanism. It strengthens the prior `m=2` theorem by making the
value cap explicit; publication novelty remains unresolved.
