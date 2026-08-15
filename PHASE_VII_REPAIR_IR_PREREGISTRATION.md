# Phase VII preregistration: exact budget--IR repair trade-off

Frozen before execution on the same seven declared Phase-VI sources: the
disclosed four-agent decimal control and all six cases in
`configs/relu_benchmark.json`. No source is excluded based on its result.

For an efficient Groves rule with deleted-input term `h(theta_-i)`, truthful
utility is `S(theta)-h(theta_-i)`, where `S=max(sum(theta),1)`. Let `s` be the
certified minimum budget slack and let `u` be the certified minimum truthful
utility over the ordered continuous cube and all deleted reports. Phase VI's
fixed scalar repair is `delta=max(0,-s/n)`. It changes total slack by `n*delta`
and every truthful utility by `-delta`.

Primary outcome: exact tuple `(s, delta, u, u-delta)`, with the predicate
`delta <= u` when `u >= 0`. This predicate is necessary and sufficient for the
fixed scalar repair to simultaneously have no deficit and ex-post IR in this
declared model. The compiler route and the direct source-network route must
agree on `u`; an independent exact-real Z3 query must prove that no smaller
utility exists for every source and deleted report. A source may fail the
combined predicate; that is a result, not a reason to alter the corpus or
repair family.

Non-goals: this does not optimize arbitrary redistribution functions, claim
economic usefulness of synthetic fixtures, or establish a continuous-domain
result beyond the exactly represented piecewise-affine source class.
