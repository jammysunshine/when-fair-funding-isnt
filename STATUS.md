# Status

Phase: Phase II feasibility gate for certificate-first VCG redistribution
synthesis/audit; the completed ternary-frontier theorem remains a baseline.

Current Phase II evidence: the initial finite-grid oracle is a negative
control—it returns the ordinary VCG charge rule on the three-agent grid. An
exact continuous audit of the 3-agent printed Guo (2024) formula reproduces
efficiency `2/3`. For the paper's printed four-agent decimal formula, two
independent exact arrangement-vertex implementations find a non-deficit
shortfall of `1/5000` at `(0,1/2,1/2,1/2)`. Adding the paper's prescribed
constant repair `1/20000` to each Groves term removes that shortfall; its
exact printed-decimal efficiency is `3333/5000`. This is a replication result
about displayed rounded coefficients, not an allegation about unreported
training weights.

Completed: specification, preregistration, prior-art positioning, antichain
enumerator, exact n=3/4/5/6 search, all-agent suffix-frontier theorem,
construction certificate, primary and independent verifiers, efficient-rule
counterexample, held-out stress audit, manuscript, tests, hashes, and legacy
regression checks.

Evidence: the theorem certificate checks 806 constructions for n=1..12 and
the exact rule-count formula; finite searches give candidate counts `16/32/64`
for three through five agents and 128 for six agents; accepted sequences
`4,4,4,1,1,1`, `5,5,5,5,1,1,1,1`, `6,6,6,6,6,1,1,1,1,1`, and
`7,7,7,7,7,7,1,1,1,1,1,1`; 122 cross-agent rows independently accepted; 207
held-out failures retained. The exploratory `max_value=3` extension has 66
candidates, 60 accepted rows replayed with zero independent failures, and
accepted counts `15,15,15,4,4,4,1,1,1`.

Resource use: local Python standard library, deterministic integer arithmetic,
no external data, paid API, or cloud compute. Symbolic construction handles
arbitrary n; full profile replay is bounded at n<=5 in the theorem certificate,
with the n=6 artifact providing a larger independent cross-check. Runtime and
memory for that extension remain recorded in the scaling logs.

The Phase II corpus now also includes a separately implemented IJCAI-2019
symbolic asymptotic baseline, exhaustively replayed on the frozen
`{0,1/4,1/2,3/4,1}^n` grids for `n=3..6` (19,500 profiles). It is non-deficit
there, but has poor low-agent efficiency, including negative utility at some
grid profiles; that is a scoped baseline observation, not a contradiction of
its asymptotic theorem.

Delivery gate: the replication lane has frozen certificates and clean
independent replays. A paper-grade main study still requires a broader,
prespecified audit corpus or a new certified mechanism-design result. The
strongest supported claim remains a bounded reproducibility artifact, not a
universal mechanism-design theorem or guaranteed publication result.
