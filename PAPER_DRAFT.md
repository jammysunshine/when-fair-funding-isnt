# Certificate-first exact frontiers and executable audits for public-project mechanisms

## Abstract

Automated mechanism design is only scientifically useful when proposed rules
can be checked exhaustively rather than judged by sampled performance. We
develop a certificate-first study for deterministic public-project mechanisms.
Agents have integer values in a finite lattice `{0,...,m}` for a binary project
with a known cost. We enumerate every anonymous monotone allocation rule over
the sorted report states and attach normalized discrete critical payments.
Each candidate is checked for dominant-strategy incentive compatibility (DSIC),
ex-post individual rationality, feasibility, anonymity, no subsidy when the
project is absent, and weak budget balance. On the preregistered three-agent
domain, 16 rules are enumerated at each cost. The number satisfying all
constraints is `4,4,4,1,1,1` for costs `1,...,6`; at cost three the best
accepted rule has worst-case welfare regret one. An efficient sum-threshold
rule is DSIC and individually rational but fails budget balance at a concrete
profile. We prove a finite-lattice characterization in this declared class:
writing `k=ceil(c/n)`, accepted rules are exactly the nonempty upward-closed
sets inside `{k,...,m}^n`, and none exists for `c>nm`. The original ternary
suffix result is its `m=2` corollary. A preregistered untouched
`n=3,m=4,c=1..12` confirmation reproduces every accepted rule set by full
enumeration and independently replays all 255 accepted rules with zero
failures. Exact searches for three through six ternary agents independently
cross-check that corollary. A value-magnitude stress test finds
207 failures for the efficient threshold family on held-out `{0,1,2,3}`
profiles. A post-hoc exact `m=3` precursor finds 66 rules and 60 independently
replayed accepted rows. The result is a reproducible finite theorem and
falsifiable benchmark, not a theorem for
continuous values or a claim of unrestricted mechanism-design novelty. As a
separate source-integrity study, six preregistered rational one-hidden-layer
ReLU fixtures with three to five agents have identical direct-source and
compiled certificates; an exact-real Z3 cross-check returns `unsat` for all
18 strict-bound counterexample queries. This is bounded verification evidence,
not a newly discovered mechanism or a generic neural-verification result.
Finally, as a post-hoc falsification supplement, we extend the certificate to
bounded-size coalitions. Cap-2 coalition deviations shrink the cost-3 DSIC
frontier from 4 to 2 accepted rules, and the canonical efficient/pivotal
comparator itself -- single-agent DSIC by construction -- fails coalition-cap-2
DSIC in 66 of 75 audited `(domain, agent count, cost)` cells spanning
`n=3..6` on the `{0,1,2}` value domain and `n=3` on the wider `{0,1,2,3}`
value domain. All coalition claims are independently replayed with zero
mismatches.

## 1. Introduction

Public-project design exposes a basic tension: selecting the project whenever
total value covers cost is efficient, but its critical payments need not cover
the cost. Conversely, budget balance can require a more conservative allocation
rule and therefore lose welfare. Existing mechanism-design theory studies this
tension in broad quasi-linear domains, while automated mechanism-design work
shows how finite search can discover or reproduce rules. The practical gap is
an auditable benchmark in which the entire candidate class, verifier, negative
examples, and independent replay are shipped together.

This paper makes eight deliberately narrow contributions:

1. a typed finite public-project model with exact critical payments;
2. an antichain enumerator that covers every anonymous monotone rule in the
   chosen finite domain;
3. a cost-indexed welfare frontier and explicit efficient-rule counterexample;
4. serialized certificates replayed by an implementation that does not import
   the primary mechanism code.
5. a human-checkable finite-lattice proof, with a construction independent of
   full-domain search and a preregistered full-domain confirmation.
6. an executable-specification audit layer for published shallow max-affine
   VCG-redistribution formulas, with a standalone replay from serialized
   rational expressions.
7. a preregistered source-to-certificate cross-check for rational shallow ReLU
   fixtures, independently challenged by exact-real SMT queries;
8. a post-hoc bounded-coalition falsification supplement, including an
   independent audit of whether the canonical single-agent-DSIC comparator
   itself resists coalitions, with a standalone replay of every claim.

## 2. Model

There are `n` agents with values `v_i` in `{0,...,m}` for a public project with
integer cost `c`. A direct mechanism reports `r` and chooses `q(r) in {0,1}`. Agent
`i` receives utility

`u_i(v_i,r) = v_i q(r) - p_i(r)`.

The allocation rule is anonymous and monotone in every report. For each
monotone rule we use the normalized discrete critical payment: if the project
is built, agent `i` pays the smallest report at which the project would be
built holding other reports fixed; otherwise the payment is zero. This
normalization removes arbitrary transfers from the search and makes the
candidate table sufficient to reconstruct payments.

The verifier requires:

- feasibility and no payment when `q=0`;
- DSIC against every report in the finite type set;
- ex-post IR at every truthful profile;
- anonymity under every profile permutation;
- weak budget balance, `sum_i p_i(r) >= c`, whenever `q(r)=1`;
- `q(m,...,m)=1`, excluding the vacuous never-build rule.

The primary objective is worst-case additive welfare regret relative to the
efficient allocation `q*(v)=1{sum_i v_i >= c}`:

`R(q) = max_v [max(0,sum_i v_i-c) - q(v)(sum_i v_i-c)]`.

Uniform expected welfare and project rate are secondary diagnostics.

## 3. Exact search and certificates

Anonymous states are sorted value vectors. A monotone allocation table is an
upward-closed subset of this finite poset, uniquely represented by its minimal
active states (an antichain). The enumerator generates antichains directly;
this avoids scanning all bit masks and makes the cross-agent extension exact.
For each table, the primary verifier checks every profile, every unilateral
report, and every permutation. A seeded threshold-proposal loop is included as
an optimization-style discovery probe, but proposals never bypass the exact
verifier.

The independent checker reconstructs the state table and critical payments from
JSON. It independently checks DSIC, ex-post IR, weak budget balance, and
anonymity. It does not import the primary search or verifier. The certificate
also evaluates the efficient sum-threshold family on all `4^3=64` profiles with
values `{0,1,2,3}` and records every failure.

## 4. Results

### 4.1 Preregistered three-agent frontier

The domain contains 10 sorted states and 16 monotone rules. The exact frontier
is:

| cost | accepted rules | best worst-case regret | best expected welfare |
|---:|---:|---:|---:|
| 1 | 4 | 3 | 1.0370 |
| 2 | 4 | 2 | 0.7407 |
| 3 | 4 | 1 | 0.4444 |
| 4 | 1 | 1 | 0.0741 |
| 5 | 1 | 0 | 0.0370 |
| 6 | 1 | 0 | 0.0000 |

At cost three, the four accepted tables are nested upper sets in the sorted
state poset. Their minimum active states move from `(2,2,2)` down through the
highest-value states, while the normalized critical payments continue to cover
the cost. The result is a complete finite frontier, not a sampled
optimization claim.

The efficient threshold rule passes DSIC, ex-post IR, feasibility, and
anonymity, but fails budget balance at `(0,2,2)`: its payments are `(0,1,1)`,
whose total is 2 while cost is 3. This is the smallest informative negative
example in the main domain and is retained in the certificate.

### 4.2 Finite value-lattice theorem and cross-check

The theorem covers every `n>=1`, finite integer cap `m>=1`, and integer cost.
Put `k=ceil(c/n)`. If `k>m`, no accepted rule exists. Otherwise, an allocation
rule is accepted exactly when its active set is a nonempty upward-closed subset
of the sorted restricted lattice `{k,...,m}^n`. At the all-`m` profile,
anonymity makes all critical payments equal; budget balance forces their common
threshold to be at least `k`. Monotonicity then rules out every active profile
with a coordinate below `k`. Conversely, every upward-closed set inside the
restricted lattice has every active critical payment at least `k`, so its total
revenue covers cost. Full details are in `PUBLIC_PROJECT_THEOREM.md`.

Finite exhaustive searches independently cross-check the theorem:

| agents | anonymous rules | accepted counts by cost | costs with one accepted rule |
|---:|---:|---|---|
| 3 | 16 | 4,4,4,1,1,1 | 4,5,6 |
| 4 | 32 | 5,5,5,5,1,1,1,1 | 5,6,7,8 |
| 5 | 64 | 6,6,6,6,6,1,1,1,1,1 | 6,7,8,9,10 |
| 6 | 128 | 7,7,7,7,7,7,1,1,1,1,1,1 | 7,8,9,10,11,12 |

The serialized accepted rows total 122 (74 through five agents and 48 in the
six-agent extension), and all pass the standalone checker. The six-agent run
took 56.394 seconds and used 29,474,816 bytes peak resident memory on Darwin.
The symbolic ternary construction certificate checks 806 mechanisms for
`n=1..12`; it is a regression certificate for the `m=2` corollary, not a
formal proof assistant.

### 4.3 Stress and falsification

On held-out values `{0,1,2,3}`, the six sum-threshold rules produce 207 recorded
budget/IC failures across 64 profiles per threshold. This is a deliberate
generalization boundary: success on `{0,1,2}` does not justify a continuous or
larger-value claim.

### 4.4 Preregistered value-lattice confirmation

The theorem and frozen confirmation protocol were committed before a fresh
three-agent `m=4` run. Full-domain enumeration and the theorem construction
produce identical accepted rule sets at all costs `1,...,12`; counts are
`65,65,65,15,15,15,4,4,4,1,1,1`. The standalone checker accepted all 255
serialized rules, with no failures. The run took 24.00 seconds and used
45,842,432 bytes peak resident memory. This is a direct falsification attempt
on a larger untouched lattice, not an extrapolated performance metric.

The prior post-hoc `m=3` run is retained as a precursor: it has 66 anonymous
monotone rules and counts `15,15,15,4,4,4,1,1,1`, with 60 independent replays.
Neither run establishes a continuous-value characterization.

### 4.5 Executable audit of published max-affine rules

The finite frontier is complemented, but not replaced, by an external audit
lane. We define a deliberately restricted typed language: rational affine
forms combined by addition, scalar multiplication, and finite `max`/`min`.
On an ordered unit cube, every branch boundary and the public-project
first-best boundary are affine. Enumerating every intersection of the declared
boundaries therefore gives a finite exact certificate for extrema of total
Groves charge divided by first-best cost. On each arrangement cell the selected
branches are affine, budget slack is affine, and the ratio is linear-fractional
with denominator at least one; extrema therefore occur at a cell vertex.

The generic engine reproduces four pre-existing continuous formulas: the
three-agent direct-redistribution formula in Guo (PRIMA 2016) Equation (3),
the three-agent optimum displayed as Guo (IJCAI 2019) Equation (2), and the
three- and four-agent printed formulas in Guo (AAAI 2024). The four-agent
network is lowered from a serialized rational one-hidden-layer ReLU
specification rather than only bespoke arithmetic. A separate evaluator also
compares the source network and compiled expression on every vertex of their
common branch refinement. The PRIMA rule is
converted to its Groves-term equivalent and independently checked against the
source-convention evaluator at every certificate vertex; it has slack `64/81`
and minimum retained efficiency `-47/162` on the three-agent ordered cube.
The four-agent case is the hard control: it includes signed ReLU terms and terminating
decimal coefficients. The generic certificate reproduces the displayed
formula's `1/5000` deficit and its published `1/20000` per-term uniform repair.
An independent program consumes only the serialized rational expression,
derives branch planes and arrangement vertices itself, and exactly matches all
five certificates (including the repaired four-agent entry).
The largest frozen entry has 22 planes, 7,315 exact four-plane bases, and 116
feasible vertices. These are a demonstrated resource boundary, not evidence of
scalability to arbitrary architecture depth or dimension.

### 4.6 Frozen ReLU source and solver cross-check

Source replay at shared certificate vertices could still conceal a lowering or
boundary-generation error. We therefore freeze six deterministic rational
one-hidden-layer fixtures before evaluation: three development and three
confirmation cases, covering three to five agents and widths two or three.
The direct route derives activation boundaries and charge values from the
serialized source network; the other lowers it into the typed max/min-affine
language. All six pairs agree exactly on extrema and witnesses. Their
candidate-basis counts are `165,3060,6188,364,3060,792`, with respectively
`6,14,49,23,8,19` feasible vertices.

An external exact-real Z3 model encodes the source ReLU network without
importing the compiler or certificate engine. Per fixture it asks whether
budget slack is strictly smaller than reported, whether charge ratio is
strictly below the reported minimum, and whether it is strictly above the
reported maximum. All 18 queries return `unsat`; direct rational evaluation
also validates every reported extremum witness. This rules out those
counterexamples for the six frozen source models, not arbitrary learned
networks or a generic scalable SMT procedure.

This is a reproducibility result about displayed formulas. It does not recover
training weights, diagnose authors' unshared implementation, prove properties
of arbitrary neural networks, or establish a new mechanism. Its value is that
the claim boundary, formula, arithmetic, witness, and independent replay are
all inspectable.

### 4.7 Exact uniform repair synthesis

We add a deliberately small synthesis result rather than another synthetic
benchmark. If an `n`-agent deleted-input source has certified minimum slack
`s`, adding `delta` uniformly to its output bias changes total charge by
`n*delta` at every profile. Consequently `max(0,-s/n)` is the smallest
nonnegative offset that removes deficit within this one-parameter family: the
baseline slack witness establishes necessity and the identity establishes
sufficiency.

The seven frozen sources include the printed four-agent decimal rule and all
six Phase-V fixtures. The printed control recovers `1/20000`; six sources need
positive repairs and one needs none. Compiled and direct-source certificates
agree after every repair, all positive repairs bind at zero slack, every
half-sized repair fails at the original witness, and seven exact-real Z3
strict-negative-slack queries are `unsat`. This is not a new mechanism or a
welfare result. In fact, the large synthetic offsets are negative evidence
against interpreting scalar feasibility repair as economically useful design.

### 4.8 Certified budget--IR incompatibility of the scalar repair

The preceding result is not sufficient for a Groves mechanism because truthful
utility is `S-h(theta_-i)`. The same offset `delta` that adds `n*delta` to total
slack subtracts `delta` from every agent's utility. We therefore froze the
corpus and repair family before computing exact minimum utility. All seven
repaired sources fail ex-post IR: the displayed control is negative already,
and every initially nonnegative synthetic margin is smaller than the offset
required for budget repair. Direct source replay agrees with the compiler; 28
exact-real Z3 lower-bound queries are `unsat`, and seven IR queries agree.
This is a calibrated negative result, not an impossibility theorem for other
redistribution families.

### 4.9 Bounded-coalition falsification and independent baseline audit

Sections 4.1-4.4 establish DSIC only against unilateral deviations. We add a
post-hoc, non-preregistered supplement (`PREREGISTRATION.md`, "Post-hoc
coalition robustness extension") checking whether accepted rules also resist
joint deviations by small groups. For a coalition `T` of size up to a frozen
cap `k`, we exhaustively enumerate every joint report deviation `T` could make
and reject a rule if any joint deviation strictly increases the coalition's
summed utility over truthful reporting.

**Frontier shrinkage.** On the preregistered three-agent, cost-3 domain, cap-2
deviations shrink the DSIC frontier from 4 accepted rules to 2
(`anonymous_monotone_mask_512`, `anonymous_monotone_mask_960`); 6 frontier
rows are rejected at cap-2 across all six costs, with 0 rejected survivors
among the cap-2-accepted rules under independent replay.

**Scaling.** The same filter applied to `n=3..5` (cap 3, 32.977s) and
`n=3..6` (cap 3, 91.758s) reproduces fragility at every selected
`(n,cost)` checkpoint with 0 independent failures across 24 and 34 selected
checks respectively. A separate extension to the wider `{0,1,2,3}` value
domain (`n=3`, costs `1..9`, cap up to 3) reproduces the same qualitative
result at selected costs `1,3,9` with 0 independent failures.

**Independent baseline audit.** The preceding results only characterize the
*search-discovered* frontier. A skeptical reader could ask whether coalition
fragility is an artifact of that search rather than a property of natural
mechanisms. We therefore separately audit the canonical efficient/pivotal
comparator from Section 4.1 -- the welfare-maximizing sum-threshold rule with
critical-value payments, single-agent DSIC and ex-post IR by construction --
against the identical coalition bar, across all four domains above (75
`(domain, n, cost)` cells total). Fragility is judged strictly from the
verifier's `dsic`/`coalitional_dsic` fields, decoupled from that same rule's
separately documented weak-budget-balance deficit (Section 4.1), so the two
independent negative results are not conflated. The comparator is
single-agent DSIC in every cell tested, but fails coalition-cap-2 DSIC in 66
of 75 cells and in 10 of the 11 preregistered-style selected spot checks (the
lone survivor is `n=3`, cost `9` on the `{0,1,2,3}` domain). A concrete
witness at `n=3`, cost `3`: truthful reports `(0,1,1)` (project not built,
all utilities 0). If agents 0 and 1 jointly misreport `(2,2)` while agent 2
reports truthfully, the profile becomes `(2,2,1)`, which crosses the cost-3
threshold and builds the project. Because critical-value payments are
computed from the *post-deviation* profile, each deviator's payment is the
smallest report at which the project would still build holding the other
deviator's inflated report fixed -- which is 0 for both, since the other
deviator's report alone already covers cost. Both deviators pay nothing and
jointly gain 1 unit of utility they could not obtain by reporting truthfully,
at agent 2's expense of unknowingly co-funding a project neither deviator
truthfully valued at that cost. This single witness generalizes the
mechanism-design intuition that critical-value payments, calibrated against
single-agent deviations, do not account for a coalition's ability to jointly
manufacture the threshold it is then charged against.

Every coalition claim above is replayed by a standalone implementation
(`public_project_independent.py`) that reconstructs allocation tables and
payments from serialized JSON without importing the primary verifier: 0
mismatches across the frontier, scaling, scaling-extension, and baseline-audit
studies (independent digests recorded in `VERIFICATION_REPORT.md`).

This supplement is deliberately narrow. It bounds coalition size at 2 or 3, it
does not claim coalition-proofness for arbitrary group size, and it does not
extend to randomized rules, continuous values, or false-name attacks. It does
show, with an exact and independently replayed counterexample, that
single-agent DSIC -- the standard acceptance bar used throughout Sections
4.1-4.4 and in most automated-mechanism-design search -- is not sufficient
for robustness against even the smallest possible group manipulation, and
that this failure is not specific to the search-discovered frontier: it also
afflicts the textbook efficient/pivotal comparator.

## 5. Positioning and contribution boundary

The study is deliberately positioned against established theory and automated
mechanism design rather than claiming to replace either. [Green--Laffont](https://green.scholars.harvard.edu/publications/incentives-public-decision-making),
[Ohseto](https://www.sciencedirect.com/science/article/pii/S0899825699907558),
and [Moulin](https://academic.oup.com/restud/article-abstract/61/2/305/1517585)
provide foundational public-project and cost-sharing results;
Nath and Sandholm analyze efficiency and budget balance in general quasi-linear
domains ([paper](https://arxiv.org/abs/1610.01443)); Conitzer and Sandholm give
the general computational approach to automated mechanism design
([AAAI paper](https://ojs.aaai.org/index.php/AAAI/article/view/7708)); and Guo
et al. study machine-learning approaches for public-project mechanism design
([2024 article](https://link.springer.com/article/10.1007/s10458-024-09647-8)).

| Existing line | This paper adds | This paper does not add |
|---|---|---|
| General public-project and cost-sharing theory | A finite, fully enumerated benchmark with explicit payment reconstruction and witnesses | A new impossibility theorem or a continuous-value characterization |
| Automated mechanism design | A solver-free antichain enumerator, machine-readable certificates, and an independent replay implementation | A claim that the search discovered a new mechanism |
| Learned public-project mechanisms | A falsification harness showing exactly where an efficient threshold proposal fails | A learned policy, deployment result, or causal claim |
| Computer-aided mechanism and neural-network verification | Typed formula provenance, direct-source replay, and exact-real SMT cross-checks for a small public-project audit corpus | Generic verification novelty or coverage of arbitrary architectures |
| Coalition-proof/group-strategyproof mechanism theory | An exact, independently replayed bounded-coalition falsification supplement, including a baseline audit showing the textbook efficient/pivotal rule is itself coalition-cap-2 fragile | A coalition-proofness theorem, an unbounded-coalition-size result, or a repaired coalition-resistant mechanism |

The defensible contribution is a compact, replayable certificate and an exact
theorem for the specified finite integer-value class. It is not a claim of a
new universal impossibility result or unrestricted mechanism-design novelty.

## 6. Reproducibility and falsification

The main JSON, scaling CSVs, and six-agent JSON contain the complete serialized accepted rows;
the independent checker reconstructs allocation and critical payments without
importing the primary verifier. The ternary clean run reports 122 accepted rows
and zero independent replay failures; the frozen `m=4` confirmation adds 255
accepted rows with exact predicted/exhaustive equality and zero failures. The held-out audit evaluates every one of the 64
profiles for each efficient threshold on values `{0,1,2,3}` and records 207
failures. These are positive and negative controls: the first tests certificate
integrity, while the second tests whether the finite result is being
over-generalized. Exact commands and SHA-256 hashes are in
`REPRODUCIBILITY_MANIFEST.md`.

## 7. Limitations and next work

The theorem's mechanism class is anonymous, deterministic, finite-valued, and
restricted to normalized critical payments. The study does not cover randomized
rules, subsidies, Bayesian objectives, continuous values, arbitrary-size
collusion, false-name reports, asymmetric rules, or arbitrary payment schemes.
The coalition supplement (Section 4.9) is bounded to coalitions of size 2 or 3
within the same finite integer-value class; it establishes fragility, not a
repair, and does not claim anything about coalitions above the tested cap or
about mechanisms outside the anonymous-monotone class. The n=3..6 searches
are computational cross-checks; the finite-lattice proof is the general result. The
stress audit is intentionally negative for
the efficient threshold family; it is not an empirical estimate of deployment
risk. The ReLU cross-check covers six frozen synthetic fixtures and publicly
displayed formulas, not opaque trained weights or a representative network
corpus. Before submission, a researcher should test the theorem against richer
value domains and broader mechanisms, compare unrestricted transfers and
subsidies, evaluate a broader independently sourced formula corpus, and obtain
an external replication.

## 8. Reproduction

```bash
python3 -m unittest discover -s tests -v
python3 scripts/run_public_project_study.py
python3 scripts/verify_public_project_certificate.py
python3 scripts/run_value_extension.py
python3 scripts/run_n6_extension.py
python3 scripts/verify_scaling_theorem.py
python3 scripts/verify_value_lattice_theorem.py
python3 scripts/run_max_affine_certification.py
python3 scripts/verify_max_affine_certificate.py
python3 scripts/verify_source_network_certificates.py
python3 scripts/run_relu_benchmark.py
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-verification.txt
.venv/bin/python scripts/verify_relu_benchmark_z3.py
python3 scripts/run_uniform_repair_study.py
.venv/bin/python scripts/verify_uniform_repair_z3.py
python3 scripts/run_repair_ir_tradeoff_study.py
.venv/bin/python scripts/verify_repair_ir_z3.py
python3 scripts/run_public_project_coalition_frontier.py
python3 scripts/verify_public_project_coalition_frontier.py
python3 scripts/run_public_project_coalition_scaling.py
python3 scripts/verify_public_project_coalition_scaling.py
python3 scripts/run_public_project_coalition_scaling_extended.py
python3 scripts/verify_public_project_coalition_scaling_extended.py
python3 scripts/run_public_project_coalition_value3_frontier.py
python3 scripts/verify_public_project_coalition_value3_frontier.py
python3 scripts/run_public_project_coalition_baseline_audit.py
python3 scripts/verify_public_project_coalition_baseline_audit.py
```

The main JSON, cross-agent CSV, certificate, plot, specification, and claim
ledger are committed under `artifacts/`, `reports/`, and the repository root.

## 9. Conclusion

Exact search does not magically produce a universally optimal mechanism. This
study does provide a finite-lattice characterization that a skeptical reader
can inspect: the proof fixes the accepted family, a preregistered larger-lattice
enumeration reproduces it exactly, the efficient comparator has a concrete
budget-balance failure, a bounded-coalition supplement shows the same
comparator also has a concrete, independently replayed incentive failure
against groups as small as size 2, and the held-out stress test records where
the result stops generalizing. It is a credible foundation for a
theory/verification paper, but publication still requires external novelty
review, broader theory, and peer review.
