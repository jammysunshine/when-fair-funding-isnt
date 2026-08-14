# Phase IV preregistration: executable-rule certification census

Frozen: 2026-08-15, before adding further formulas to the corpus.

## Question

For publicly available VCG-redistribution rules in the bounded public-project
model, can a typed exact max-affine representation reproduce the reported rule,
produce a machine-checkable continuous or finite-grid certificate, and expose
the difference between an executable displayed formula and an unshared learned
parameterization?

This is a verification/reproducibility study, not a search for a new mechanism.

## Eligibility and sources

Search official proceedings and author-hosted primary PDFs for public-project
VCG redistribution rules.  An entry is eligible only when the source gives a
complete executable formula, the number of agents and normalization are clear,
and no unreported weights are needed.  We log eligible rules, formula-incomplete
papers, and inaccessible sources separately.  Sources already in the frozen
Phase II/III corpus are retained but not retuned.

Search terms: `public project VCG redistribution`, `VCG redistribution
mechanism public project`, `worst-case VCG redistribution`, and cited works
from Guo (2016, 2019, 2024).  Sources are recorded with URL, access date,
equation/page, and transcription convention.

## Methods and endpoints

The primary engine accepts sums, rational scalars, affine forms, and maxima of
affine forms.  It enumerates all vertices of the ordered unit cube induced by
domain facets and every max-branch and first-best break plane, using exact
`Fraction` arithmetic.  This is complete only for the represented shallow
max-affine class: on each resulting cell both charge and first-best are affine,
so extrema of the charge/first-best ratio occur at vertices.

Primary endpoints for a continuous entry are vertex count, minimum retained
budget slack, maximum charge ratio, and worst-case allocative efficiency.
Finite-grid entries retain their predeclared grids and are labelled grid-only.
Every continuous result needs a separately written replay or an existing
independent implementation.  Displayed decimals are exact terminating
rationals.  A discrepancy is reported only for the displayed formula, never as
a claim about unavailable source code or weights.

## Falsification and stopping

The engine must first reproduce the already certified IJCAI-2019 Equation (2)
and Guo-2024 three-agent displayed rule.  Any disagreement is a failed method
result, preserved with the smallest witness; formulas are not adjusted to make
the engine agree.  We stop this phase after the source census and all eligible
formulas are either certified, bounded by a stated limitation, or marked
untranscribable.  We will not claim novelty over computer-aided mechanism
verification (Barthe et al., 2015) or general neural-network verification.
