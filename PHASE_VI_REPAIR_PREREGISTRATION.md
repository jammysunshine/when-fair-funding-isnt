# Phase VI preregistration: exact uniform repair synthesis

Status: frozen before execution on 2026-08-15.

## Question and declared class

For a rational one-hidden-layer ReLU redistribution term `h`, used once after
deleting each of `n` reports, can an exact certificate synthesize the smallest
uniform additive output-bias offset that makes the total charge non-deficit on
the ordered public-project cube?

The study covers only this one-parameter family.  It neither searches over
allocation rules nor asserts welfare optimality, individual rationality, or a
general repair result for neural mechanisms.

## Frozen corpus and procedure

The corpus is the disclosed printed four-agent AAAI-2024 decimal network and
all six fixtures, without exclusions, from `configs/relu_benchmark.json`.
For each source, first certify its unmodified total charge.  If its minimum
budget slack is `s`, synthesize `delta = max(0, -s/n)` and add `delta` to the
serialized output bias.  Re-certify the repaired source through both the
compiler route and the independent direct-source route.

## Acceptance and falsification

The repaired certificate must have nonnegative minimum budget slack, and both
routes must agree exactly on every serialized certificate field.  Minimality
is tested against the original slack witness: for a positive offset, replacing
`delta` by `delta/2` must leave a negative slack at that witness.  A source
whose exact direct and compiled results disagree is retained as a failure.

## Proof obligation

At every report profile, increasing the output bias by `delta` increases each
of the `n` deleted-input terms by `delta`, hence total charge and budget slack
by `n*delta`.  Therefore the stated offset is sufficient; the original
minimum-slack witness proves no smaller nonnegative uniform offset can work.

## Reporting boundary

Report every corpus member, including zero-offset cases.  The published
four-agent rule is a reproduction control whose known offset is not treated as
a discovery.  Synthetic fixtures test only source/compiler robustness and are
not evidence about trained neural mechanisms or deployment.
