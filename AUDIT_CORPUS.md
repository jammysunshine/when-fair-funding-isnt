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

## Phase-IV source census ledger

This is a provenance ledger, not an additional endpoint pool. It records the
backward and adjacent literature checked while extending the reusable
certificate engine. Exclusion means only that a source cannot support an
executable-formula certificate under the preregistered scope.

| ID | Source and access route | Census disposition | Reason |
|---|---|---|---|
| C1 | Naroditskiy et al., WINE 2012, [official repository record](https://digital.library.adelaide.edu.au/items/261238eb-51d1-4b28-b23f-9e0f73eab495) | Excluded | The accessible record identifies a three-agent optimum but its PDF is restricted; no formula is reconstructed. |
| C2 | Guo and Shen, PRIMA 2017, [official repository record](https://digital.library.adelaide.edu.au/items/147ffe40-1f6b-430b-8db6-d10fa38d1b33) | Lineage logged; independent formula excluded | IJCAI 2019 prints the credited Eq. (2), already audited as A5; the original record does not supply a separately accessible executable formula. |
| C3 | Guo et al., AAMAS 2024, [publisher record](https://link.springer.com/article/10.1007/s10458-024-09647-8) | Excluded as adjacent | It studies ML approaches to public projects, not an eligible displayed anonymous VCG-redistribution max-affine rule under this audit's convention. |
| C4 | Barthe et al., 2015, [preprint](https://arxiv.org/abs/1502.04052) | Method comparator, not corpus formula | It establishes prior computer-aided mechanism verification; this project makes no generic verification-novelty claim. |

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
- The generic engine is validated against A5, A1, and A2. For A2 it reproduces
  both the printed-decimal deficit and the declared uniform-offset repair,
  using a typed transcription separate from the source-specific evaluator.

## Source-transcription safeguards

Each formula is entered twice: a primary evaluator and a standalone evaluator
with no import of the primary module. PDF extraction is treated as a locator,
not authority: outer denominators, max thresholds, ordering conventions, and
correction signs are visually checked against the rendered page before the
certificate is accepted. This safeguard caught an initially omitted outer
denominator while transcribing the PRIMA-2016 expression; the failed reading
was discarded before the final artifact was emitted.
