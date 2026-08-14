# Status

Phase: Phase II feasibility gate for certificate-first VCG redistribution
synthesis/audit; the completed ternary-frontier theorem remains a baseline.

Current Phase II evidence: a three-agent, three-type exact rational LP has six
anonymous Groves-term variables and 22 finite constraints. Complete vertex
enumeration checks 74,613 bases and yields uniform-prior objective `10/3`; a
counterexample-guided run adds five no-deficit witnesses and reaches the same
candidate. This is pilot evidence only until standalone replay, frozen
confirmation priors, and comparator audit are complete.

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

Delivery gate: final clean-run verification is pending after this theorem
upgrade. The strongest supported claim is an exact theorem in the declared
finite ternary mechanism class, not a universal mechanism-design theorem or
guaranteed publication result.
