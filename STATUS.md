# Status

Phase: exact public-project frontier plus exploratory cross-agent scaling,
independent replay, manuscript, and delivery verification.

Completed: specification, preregistration, prior-art positioning, antichain
enumerator, exact n=3/4/5 search, cost frontiers, primary verifier,
standalone certificate, efficient-rule counterexample, held-out stress audit,
paper-style manuscript, tests, hashes, and legacy regression checks.

Evidence: candidate counts `16/32/64`; accepted sequences
`4,4,4,1,1,1`, `5,5,5,5,1,1,1,1`, and `6,6,6,6,6,1,1,1,1,1`; 74 cross-agent
rows independently accepted; 207 held-out failures retained.

Resource use: local Python standard library, deterministic integer arithmetic,
no external data, paid API, or cloud compute. The initial n=3..8 scaling
attempt was stopped for excessive CPU growth; the bounded n=3..5 protocol and
limitation are recorded in `DECISION_LOG.md` and `SCALING_EXTENSION_PROTOCOL.md`.

Delivery gate: final clean-run verification is complete; package committed as
`870638f` and pushed to `origin/main`. The strongest supported claim is a
finite, reproducible characterization—not a general theorem or guaranteed
publication result.
