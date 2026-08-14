# Executable-formula audit corpus

This registry prevents post-hoc selection of eye-catching formulas. A source is
eligible only when it supplies a public, unambiguous closed form for an
anonymous VCG redistribution term, together with its convention (Groves charge
or redistribution) and a stated budget/efficiency target. Neural weights,
plots, sampled tables, and formulas whose notation cannot be resolved from the
public source are excluded rather than reverse engineered.

| ID | Public source/formula | Convention | Scope of this repository audit | Status |
|---|---|---|---|---|
| A1 | Guo, AAAI 2024, printed 3-agent formula | Groves charge | Exact continuous arrangement certificate | Included, frozen Phase II |
| A2 | Guo, AAAI 2024, printed 4-agent decimal formula | Groves charge | Exact continuous arrangement certificate and uniform-offset repair family | Included, frozen Phase II |
| A3 | Guo, IJCAI 2019, Eq. (6) and symmetrisation | Groves charge | Exhaustive `{0,1/4,1/2,3/4,1}^n`, `n=3..6` | Included, frozen Phase II |
| A4 | Guo, PRIMA 2016, Eq. (3) plus Proposition 1 correction | Redistribution | Exhaustive same rational grids | Included, exploratory after Phase II freeze |
| A5 | Guo, IJCAI 2019, Eq. (2), credited to Guo and Shen (2017) | Groves charge | Exact continuous arrangement certificate | Included, separately preregistered Phase III positive control |

## Interpretation rules

- A continuous certificate establishes only the displayed public formula on
  `[0,1]^n`, not its authors' private code, weights, or a different convention.
- A grid replay establishes the stated finite grid, not a continuous or
  asymptotic theorem.
- A displayed decimal is an executable specification here: every decimal is
  interpreted as the exact terminating rational it prints. A discrepancy is a
  reproducibility finding about that specification, never an attribution of
  error to unshared source material.
- The Phase II endpoints remain frozen. A later source is separately labelled
  and cannot be pooled into its primary claim.

## Source-transcription safeguards

Each formula is entered twice: a primary evaluator and a standalone evaluator
with no import of the primary module. PDF extraction is treated as a locator,
not authority: outer denominators, max thresholds, ordering conventions, and
correction signs are visually checked against the rendered page before the
certificate is accepted. This safeguard caught an initially omitted outer
denominator while transcribing the PRIMA-2016 expression; the failed reading
was discarded before the final artifact was emitted.
