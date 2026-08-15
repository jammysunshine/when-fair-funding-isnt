# Phase II: certificate-first VCG redistribution audit

Status: feasibility pilot; not preregistered confirmation and not a novelty claim.

## Question

Can independently replayable exact optimization expose the difference between a
candidate mechanism that looks good under sampled evaluation and one that is
globally feasible and optimal on a stated finite domain?

## Frozen pilot model

Three anonymous agents have values in `{0, 1/2, 1}` for a non-excludable
project with cost one. The project is built iff the reported sum is at least
one. A rule is an anonymous Groves term `h(theta_-i)` on the six sorted
two-agent inputs. We require nonnegative `h`, ex-post IR
`h(theta_-i) <= max(sum(theta), 1)`, and no deficit
`sum_i h(theta_-i) >= 2 max(sum(theta), 1)` at all 27 profiles.

The primary pilot objective minimizes expected total Groves offset under the
uniform product prior. At a fixed allocation and prior this is equivalent to
maximizing total agent utility, but an offset is not itself a realized payment:
the outcome-dependent Groves term must be included when discussing transfers.
Allocation and DSIC are inherited from the Groves representation.

## Two paths and checks

1. Complete rational vertex enumeration checks every six-constraint basis of
   the explicit 22-inequality LP.
2. Counterexample-guided synthesis begins with IR/nonnegativity, asks the full
   verifier for a maximally violated no-deficit profile, and adds one witness
   per round.
3. A standalone replay rebuilds the grid and solves the same finite LP without
   importing the primary synthesis module.

The pilot cannot establish optimality for continuous values, non-anonymous
rules, alternative payment conventions, or published neural mechanisms whose
weights/data are unavailable. Promotion to a main study requires a frozen
confirmation configuration, prespecified published comparators, and a result
that is more informative than merely reproducing the oracle.
