# Research-gap audit

Date: 2026-08-15. This is a boundary check, not a claim of a completed
literature review.

| Prior work | Established capability | Consequence here |
|---|---|---|
| Barthe et al. (2015), *Computer-aided verification in mechanism design* | Machine-checked incentive arguments, including VCG | Do not claim to originate formal or proof-carrying mechanism verification. |
| Mittelmann et al. (2025), *Formal verification and synthesis of mechanisms for social choice* | Formal verification and synthesis of social-choice mechanisms | Do not claim verification/synthesis in general is unresolved. |
| Guo (IJCAI 2019) | Analytic VCG redistribution for public projects | Closed-form redistribution is not new. |
| Guo et al. (AAAI 2024) | MLP/MIP design of public-project redistribution mechanisms | Do not claim neural automated mechanism discovery is new. |

## Narrow unresolved question

For a **publicly disclosed rational one-hidden-layer ReLU redistribution
rule**, can a source-independent compiler emit an exact rational,
independently replayable certificate of worst-case budget slack and welfare on
the continuous ordered public-project cube? The certificate must contain the
formula, boundary arrangement, extrema witnesses, and resource envelope, and
must be rejected after either a coefficient or a reported metric is altered.

This repository now answers that question only for a small, transparent
corpus: four public formulas (five certificate entries, counting the repaired
four-agent formula). The exact compiler and independent replay are evidence
for the implementation claim, not evidence that this is a new general
verification method.

## What would make a paper-grade main result

Before a general-AI or top mechanism-design submission, pre-specify and
complete all of the following:

1. A substantially broader public corpus of disclosed learned or symbolic
   redistribution rules, with inclusion/exclusion criteria fixed before runs.
2. A comparison against a solver-backed ReLU verifier or a formal-methods
   baseline, including success/failure and resource measurements.
3. A theorem proving the compiler/checker sound for its declared network and
   public-project class; if claiming completeness, state the exact complexity
   bound and test it independently.
4. At least one result not already implied by the displayed formulas—for
   example a certified repair or a certified architecture/training constraint
   whose benefit is measured on untouched instances.
5. External review by a mechanism-design/formal-methods researcher before any
   novelty or venue claim.

Until these gates are met, the honest label is **useful reproducibility and
audit artifact**, not a publishable general-AI contribution.
