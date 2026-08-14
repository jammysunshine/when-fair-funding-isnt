# Phase III positive-control preregistration

Frozen: 2026-08-15, before implementation and evaluation.

Question: does the exact three-agent optimum reproduced in Guo (IJCAI 2019),
Equation (2), satisfy its stated VCG-redistribution inequalities over the full
continuous type cube, and is it distinct from the later printed Guo (AAAI
2024) three-agent formula?

Target: Equation (2) only.  The formula is credited there to Guo and Shen
(2017); this study audits the inspectable IJCAI-2019 rendering and does not
claim to audit an unavailable 2017 source file.

Acceptance predicate: enumerate every vertex of the ordered cube induced by
the cube facets, the first-best break, and all max-function break planes,
using exact rational arithmetic.  At every vertex require total Groves charge
between `2S(theta)` and `(3 - 2/3)S(theta)`.  A separately written evaluator
must agree on all reported extrema.  The comparison endpoint is exact
functional equality to the AAAI-2024 printed 3-agent formula; a counterexample
is retained if they differ.

Stopping rule: report the full-domain result, the independent replay, and any
distinctness witness.  This is a positive-control reproduction, not a new
mechanism or a re-evaluation of the frozen Phase II corpus.
