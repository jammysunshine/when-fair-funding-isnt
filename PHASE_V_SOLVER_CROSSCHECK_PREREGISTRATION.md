# Phase V external SMT crosscheck preregistration

Date frozen: 2026-08-15, before solver execution.

## Question and target

Can an external exact SMT solver falsify any extrema reported by the frozen
six-case rational-ReLU benchmark? The target is the source-network semantics,
not the compiler expression.

## Method

Use Z3 `5.0.0.0` with exact real arithmetic. For every benchmark source,
encode the ordered unit cube, the direct affine--ReLU--affine deleted-input
charge, and first-best cost as symbolic real terms. For each reported minimum
budget slack, minimum charge ratio, and maximum charge ratio, query whether a
strictly better counterexample exists. A matching rational witness from the
frozen certificate is checked separately by direct source evaluation.

## Acceptance and stopping

All 18 strict counterexample queries must be `unsat`, and every frozen witness
must evaluate to its reported rational value. `sat`, `unknown`, timeout, or a
witness mismatch is a retained failure. The six fixtures, coefficients,
metrics, and query set are fixed by `configs/relu_benchmark.json` and its
results artifact; they will not be tuned after execution.

## Boundary

This is an external solver-backed crosscheck for shallow rational ReLU source
networks only. It is not a proof assistant, a performance comparison to all
MIP/SMT tools, or evidence of general neural verification.
