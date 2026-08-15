# Phase V rational-ReLU crosscheck preregistration

Date frozen: 2026-08-15, before benchmark execution.

## Question

Does the typed rational-ReLU compiler agree exactly with a separately written,
source-only activation-boundary certificate on a deterministic, diverse set of
one-hidden-layer deleted-input public-project charges?

## Cases and split

`configs/relu_benchmark.json` fixes six synthetic rational networks. The
generator is deterministic SHA-256 counter expansion with numerator range
`[-5, 5]` and denominator `7`. Three development cases and three confirmation
cases span `(agents,width) = (3,3), (4,3), (5,2)`. The confirmation seeds are
frozen here and are not eligible for tuning. Synthetic fixtures are used only
to test verifier semantics and resource scaling; they are not evidence about
trained mechanisms or economic performance.

## Methods and acceptance

For each case, compile the serialized source to the max/min-affine language
and certify the ordered unit cube. Separately derive all source ReLU
activation boundaries and certify the source directly. The primary acceptance
predicate is exact equality of every serialized certificate field (including
vertices and witnesses), with zero unexpected exceptions. A source coefficient
mutation is a required negative control. Report all six outcomes, including a
failure. Candidate-basis counts are the frozen compute metric.

## Boundaries and stopping rule

The study is limited to deterministic rational, one-hidden-layer networks and
the symmetric deleted-input charge construction. It does not compare against
an external MIP/SMT solver, prove neural-network verification generally, or
claim a new allocation mechanism. Stop after each frozen case is run once by
both routes; any mismatch is the result and triggers investigation rather than
configuration changes.
