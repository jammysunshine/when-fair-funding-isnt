# Technical Report

The implementation represents a direct mechanism as a four-row outcome table. Each row admits two choices and three pointwise budget-balanced transfer pairs, so the certified search space is `(2×3)^4=1,296`. The primary verifier checks eight unilateral deviations, eight truthful IR evaluations, and four budget/feasibility rows per table; it returns witnesses. The independent verifier uses a distinct agent-type/other-report traversal for the baseline check. The result artifact records the full accepted frontier rather than only aggregates.
