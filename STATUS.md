# Status

Phase: Phase V rational-ReLU compiler validation for VCG redistribution; the
completed ternary-frontier theorem remains a baseline.

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

Exploratory extension (kept outside the frozen Phase II corpus): Guo's
PRIMA-2016 Equation (3) plus its published `U(n)/n` correction was audited on
the same 19,500-point rational grids with an independent implementation.  It
is non-deficit throughout that grid, while its retained-utility ratio is
negative at the observed worst points for `n=3,4` and positive for `n=5,6`.
This is a finite-grid diagnostic of the stated conservative correction, not a
refutation of its asymptotic competitive guarantee.

Phase III positive control (pre-specified separately): the three-agent exact
optimum reproduced in Guo (IJCAI 2019), Equation (2), was certified over the
continuous ordered cube by all piecewise-affine arrangement vertices and a
standalone replay. It has efficiency `2/3`, but is functionally distinct from
the printed Guo (AAAI 2024) three-agent formula. This shows the checker can
certify both a known closed-form optimum and a rounded neural formula without
conflating them; it is still a replication result, not a new mechanism.

The corpus registry is `AUDIT_CORPUS.md`: five source/formula entries have
explicit inclusion scope, four independent replays, and clear continuous versus
grid boundaries. It is still insufficient for a top-tier general-AI claim; the
next gate is a broader prespecified census or a new certified algorithmic result.

Phase IV (pre-registered before extension): a typed exact shallow max-affine
executable-specification engine now reproduces four continuous controls: Guo
(IJCAI 2019) Equation (2), Guo (AAAI 2024)'s printed three-agent rule, and its
four-agent decimal rule, plus the three-agent PRIMA-2016 direct redistribution
formula in an equivalent Groves-term representation. For the four-agent rule it independently reproduces both the
printed `1/5000` deficit and the `1/20000` per-term repair. Its emitted
certificate is `artifacts/max_affine_certification.json`. The source census
logs inaccessible and adjacent sources as exclusions rather than inferring
their formulas. A standalone replay consumes the serialized rational
expressions, derives the arrangement anew, and agrees on all five entries.
The largest entry has 22 planes, 7,315 exact candidate bases, and 116 feasible
vertices; these counts bound the demonstrated computational envelope. This is
a reusable method result within the restricted expression class, not a general
neural-network verifier.

Delivery gate: the replication lane has frozen certificates and clean
independent replays. A paper-grade main study still requires a broader,
prespecified audit corpus or a new certified mechanism-design result. The
strongest supported claim remains a bounded reproducibility artifact, not a
universal mechanism-design theorem or guaranteed publication result.

Phase V: the printed four-agent one-hidden-layer rational ReLU rule is now
lowered from a serialized network specification embedded in its certificate by
`src/mechanism_discovery/rational_relu.py`; it no longer relies solely on
boutique affine arithmetic in the corpus transcription. The standalone replay
also evaluates that source network independently at every vertex of the common
ReLU/expression branch refinement, and a regression test rejects a changed
source coefficient. `RESEARCH_GAP_AUDIT.md`
records the decisive prior-art boundary: formal mechanism verification and
neural mechanism design already exist, so this compiler validation is an
incremental artifact result, not a general-AI paper claim.

Phase V extension: a third, direct source-network route now derives its own
activation-boundary arrangement from the serialized ReLU coefficients and
recomputes extrema without reading the compiled max/min formula. It is frozen
against the same public source rules and must agree exactly with both prior
routes; a coefficient mutation is a negative control. This is a meaningful
falsification check, but still does not substitute for the broader corpus and
external baseline required for a publication-grade methodological claim.
