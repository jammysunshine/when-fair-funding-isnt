# Status

Phase: Phase X coalition-robustness extension, including its independent
baseline audit and false-name-manipulation supplement, is complete as a
post-hoc falsification study.
Phase VII budget--IR trade-off is complete for declared rational ReLU
sources. Phase VIII independently confirmed the finite value-lattice theorem
on an untouched `n=3,m=4,c=1..12` grid: exact predicted/exhaustive rule-set
equality, 255 accepted-rule replays, and zero independent failures. A separate
Phase VIII constrained-synthesis pilot was withdrawn because it was exactly
the normalized pivotal VCG rule under a mismatched comparator.

Post-hoc finite-domain coalition robustness:

- `configs/public_project_coalition_frontier.json` (frozen `n=3`, `max_value=2`, `cost=1..6`, `max_coalition_size=2`)
  shrinks the cost-3 DSIC frontier from 4 rows to 2 at coalition-cap-2.
- `scripts/run_public_project_coalition_frontier.py` and
  `scripts/verify_public_project_coalition_frontier.py` produced 6
  rejected frontier rows at cap-2, 0 rejected survivors, and matching
  frontier names (`anonymous_monotone_mask_512`, `anonymous_monotone_mask_960`).
- `scripts/run_public_project_coalition_scaling.py` plus
  `scripts/verify_public_project_coalition_scaling.py` recorded cap-keyed
  fragility summaries on `n=3..5`, elapsed `32.977s`, and `0` selected failures
  across 24 selected checks.
- `scripts/run_public_project_coalition_scaling_extended.py` plus
  `scripts/verify_public_project_coalition_scaling_extended.py` extended the
  same coalition filter to `n=3..6`, elapsed `91.758s`, with `34` selected
  checks and `0` selected failures.
- `scripts/run_public_project_coalition_value3_frontier.py` plus
  `scripts/verify_public_project_coalition_value3_frontier.py` extended the
  value domain to `n=3`, `max_value=3`, `cost=1..9`, cap up to 3, at selected
  costs `1,3,9`, with `9` cost rows and `0` independent failures.
- Independent baseline audit: `scripts/run_public_project_coalition_baseline_audit.py`
  plus `scripts/verify_public_project_coalition_baseline_audit.py` test the
  canonical efficient/pivotal (welfare-maximizing sum-threshold, critical-value
  payment) mechanism against the same coalition bar across all four domains
  above. It is single-agent DSIC everywhere but fails coalition-cap-2 DSIC in
  66 of 75 `(domain, n, cost)` rows and in 10 of 11 selected spot checks
  (only `value3_frontier` cost `9` survives). This is independent of, and
  decoupled from, that mechanism's separately known budget-balance deficit.
  `0` independent replay mismatches across all 75 rows.
- False-name manipulation audit: `scripts/run_public_project_false_name_audit.py`
  plus `scripts/verify_public_project_false_name_audit.py` test whether a
  single real agent gains by fabricating extra fake report identities against
  the same canonical efficient/pivotal mechanism, across `n_real=3,4,5`, fake
  budgets `{0,1,2}`. `fake_budget=0` is a positive control (0 manipulable
  rows everywhere, confirming ordinary single-agent DSIC). At `fake_budget=1`
  or `2`, 48 of 72 `(n_real, cost, fake_budget)` rows are manipulable, and 6
  of 9 selected checks are manipulable. The independent verifier recomputes
  the sum-threshold/critical-value rule from its closed-form definition
  (no import of `public_project.py`) and reproduces every row's manipulable
  count with `0` mismatches.
- General analytical lemma (not a search result): `scripts/verify_public_project_coalition_lemma.py`
  proves, in closed form, that for every `n>=2`, `max_value=m`, `cost c<=(n-1)*m`,
  the grand-coalition "everyone reports `m`" deviation builds the project at
  payment `0` for every agent. This holds for every `(n,m,c)` satisfying the
  bound, not just audited ones. It has `0` false positives against all 75
  baseline-audit rows and a separate exhaustive check (`n=3,4`, `m=2,3`, `0`
  counterexamples) shows why `cost=n*m` is the one immune boundary: any
  proper-coalition deviation that reaches that threshold forces coalition
  members to pay exactly their own report, killing any free-ride gain. This
  converts the empirically-found frontier from a finite search result into a
  proven general theorem, and pinpoints exactly why the sole robust row in the
  baseline audit is robust.
- Complete closed-form characterization (not a search result):
  `scripts/verify_public_project_coalition_characterization.py` derives, by
  convexity, the exact minimum total coalition payment
  `k*max(0,(cost-S_O)-(k-1)*m)` for any coalition size `k` and outsider
  value-sum `S_O`, plus the exact worst-case (extremal bang-bang) truthful
  payment distribution, and combines them into a bounded integer-sweep
  existence check for coalition-cap-`k` manipulability -- no report-level
  search required. It reproduces the baseline audit's exact
  `min_failing_coalition_size` on all `75/75` rows (closing the 14-row gap the
  Section-4.11 sufficient-only lemma left open) and evaluates at agent counts
  (e.g. `n=20`) far beyond brute-force enumeration.

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
enumerator, exact n=3/4/5/6 search, finite-lattice theorem, preregistered
`m=4` full-domain confirmation, construction certificate, primary and
independent verifiers, efficient-rule counterexample, held-out stress audit,
manuscript, tests, hashes, and legacy regression checks.

Evidence: the theorem certificate checks 806 constructions for n=1..12 and
the exact rule-count formula; finite searches give candidate counts `16/32/64`
for three through five agents and 128 for six agents; accepted sequences
`4,4,4,1,1,1`, `5,5,5,5,1,1,1,1`, `6,6,6,6,6,1,1,1,1,1`, and
`7,7,7,7,7,7,1,1,1,1,1,1`; 122 cross-agent rows independently accepted; 207
held-out failures retained. The exploratory `max_value=3` extension has 66
candidates, 60 accepted rows replayed with zero independent failures, and
accepted counts `15,15,15,4,4,4,1,1,1`.

Resource use: local Python standard library, deterministic integer arithmetic,
no external data, paid API, or cloud compute. The Phase VIII confirmation ran
in 24.00 seconds with 45,842,432 bytes peak resident memory and emitted a
1,248,674-byte artifact, within the frozen 10-minute/100-MB ceiling. Symbolic
construction handles arbitrary n; full profile replay is bounded at n<=5 in
the older theorem certificate, with the n=6 artifact providing a larger
cross-check.

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
independent replays. The finite-lattice theorem is now a stronger mathematical
result than the original ternary benchmark, but a paper-grade broad-AI claim
still requires a broader prespecified corpus or a new algorithmic result. The
strongest supported claim is a finite discrete mechanism-design theorem plus
bounded reproducibility artifacts—not a universal mechanism-design theorem or
guaranteed publication result.

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

Phase V benchmark: a frozen six-case synthetic rational-ReLU crosscheck spans
three through five agents and widths two through three, with separate
development and confirmation seeds. Its first confirmation execution exposed
a zero-output hidden-unit boundary mismatch; the source verifier now removes
only semantically inert zero-output activations, matching the compiler's
function-level arrangement. The original failed result and correction are
retained in `DECISION_LOG.md`; no benchmark seed was changed.

Phase V solver gate: Z3 5.0.0.0 now independently encodes the six frozen
source networks over exact reals. All 18 strict counterexample queries (lower
budget slack, lower charge ratio, higher charge ratio) returned `unsat`, and
all serialized witnesses evaluate exactly from source coefficients. This meets
the previously missing solver-backed baseline gate for this bounded benchmark,
but the corpus remains synthetic and too small for a broad publication claim.

Phase VI: the frozen seven-source repair study synthesizes the minimal uniform
per-deleted-input output-bias offset `max(0,-s/n)` from each exact baseline
slack `s`. Six sources require a positive offset and one requires none. Every
repaired compiled certificate exactly matches the direct source certificate;
all repaired slacks are exactly zero, and a half-offset fails at the original
minimum-slack witness for each positive case. A separate Z3 exact-real query
finds no repaired deficit in any of the seven sources. This is a small,
provable repair primitive, not an economically validated new mechanism: the
synthetic offsets can be large and do not preserve the broader constraints
needed for a deployable redistribution rule.

Phase VII tested that missing economic condition without changing the corpus.
The same uniform offset lowers every truthful utility by exactly that offset.
All seven repaired sources fail ex-post IR: the published control is already
negative before repair, and each initially nonnegative synthetic margin is
smaller than its necessary offset. Compiler, direct source, and exact-real Z3
routes agree, so the scalar repair is rejected as a viable mechanism result.

Phase IX: the preregistered five-case 3--7-agent rational-ReLU scaling study
completed with compiler/direct-source equality on every case, five detected
output-bias mutations, and 15/15 `unsat` Z3 strict-counterexample challenges.
Per-case exact certification time was 0.006, 0.077, 1.409, 11.567, and 112.935
seconds for 3 through 7 agents respectively (126.0 seconds total). The steep
seven-agent cost is a measured limitation, not evidence of practical
large-scale verification. A new certified synthesis or repair result against
relevant public baselines remains necessary for a publication-grade claim.
