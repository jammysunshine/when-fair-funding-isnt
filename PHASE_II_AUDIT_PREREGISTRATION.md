# Phase II audit preregistration

Frozen: 2026-08-15, before the comparative symbolic-baseline run.

Question: do published, inspectable VCG-redistribution formulas preserve their
claimed no-deficit constraints when evaluated exactly, and what is the smallest
uniform repair needed for any displayed-decimal violation?

Corpus: (1) Guo (AAAI 2024) printed 3- and 4-agent formulas, treated as exact
terminating decimals; (2) Guo (IJCAI 2019) Equation (6) with its printed
symmetrisation, on `{0,1/4,1/2,3/4,1}^n`, `n=3,4,5,6`.  These are fixed source
targets; no unshared neural weights are reconstructed.

Primary endpoint: minimum no-deficit slack. Secondary endpoints: maximum total
charge / first-best ratio, induced worst-case efficiency, and (only for a
displayed-decimal deficit) the smallest common Groves-term offset that restores
non-deficit. Exact fractions, all arrangement vertices or all grid profiles,
and an independently implemented replay are required.

Stopping rule: publish every listed endpoint and every witness. A corpus member
is not promoted from its stated scope: continuous claims require an exact
arrangement proof; grid claims remain grid claims. The study makes no claim
about weights or code not released by an author.
