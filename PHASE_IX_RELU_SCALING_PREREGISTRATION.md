# Phase IX dimensional scaling preregistration

Date frozen: 2026-08-15, before execution.

## Question

Does the exact rational one-hidden-layer ReLU certificate remain semantically
consistent across independently implemented compiler and source-only routes as
the symmetric deleted-input public-project construction grows from three to
seven agents?

## Fixed corpus and methods

`configs/phase_ix_relu_scaling.json` fixes five SHA-256-counter rational
networks, each with width two and denominator seven. Three development cases
cover 3--5 agents; two confirmation cases cover 6--7 agents and are not used
to change the method. For every source, the compiler emits an exact
max/min-affine certificate and a source-only enumerator independently derives
the ReLU-boundary arrangement. All serialized certificate fields must agree.
Each source is then subjected to a fixed nonzero output-bias mutation; its
source-only certificate must differ from the retained baseline certificate.

An external Z3 exact-real audit asks three strict counterexample queries per
case: lower budget slack, lower charge ratio, and higher charge ratio. It also
evaluates the retained rational witnesses directly from source coefficients.

## Acceptance and limits

The run accepts only if all five exact route comparisons agree, all five
mutations alter their certificates, and all 15 Z3 queries return `unsat`.
Any mismatch, `sat`, `unknown`, timeout, or witness disagreement is retained
as a failure; seeds, widths, and coefficients will not be changed afterward.

This is a verifier-scaling experiment on synthetic exact sources. It neither
trains a mechanism nor establishes economic quality, general neural-network
verification, or superiority to the neural/MIP public-project literature.
