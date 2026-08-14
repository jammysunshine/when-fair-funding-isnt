# Technical report

The public-project study reduces a single-parameter DSIC/EPIR search to
allocation rules plus critical payments. Anonymous states are sorted report
vectors. The enumerator generates minimal-active-state antichains of the
sorted-state poset, constructs the corresponding up-sets, and therefore covers
every monotone table without scanning arbitrary masks. It yields 16, 32, and
64 candidates for three, four, and five agents.

For each rule and cost, the verifier computes critical payments, tests every
deviation, checks anonymity and budget coverage, and computes welfare regret
against the efficient allocation. The independent checker consumes only
serialized tables and replays all 74 accepted cross-agent rows. A seeded
threshold proposal loop is instrumentation only; it never establishes
completeness. The held-out value-magnitude audit probes the strongest natural
extrapolation and records its failures.
