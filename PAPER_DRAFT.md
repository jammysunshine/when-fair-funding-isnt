# Certificate-first exact frontiers and executable audits for public-project mechanisms

## Abstract

Automated mechanism design is only scientifically useful when proposed rules
can be checked exhaustively rather than judged by sampled performance. We
develop a small certificate-first benchmark for deterministic public-project
mechanisms. Agents have integer values in `{0,1,2}` for a binary project with
a known cost. We enumerate every anonymous monotone allocation rule over the
sorted report states and attach its normalized discrete critical payments.
Each candidate is checked for dominant-strategy incentive compatibility (DSIC),
ex-post individual rationality, feasibility, anonymity, no subsidy when the
project is absent, and weak budget balance. On the preregistered three-agent
domain, 16 rules are enumerated at each cost. The number satisfying all
constraints is `4,4,4,1,1,1` for costs `1,...,6`; at cost three the best
accepted rule has worst-case welfare regret one. An efficient sum-threshold
rule is DSIC and individually rational but fails budget balance at a concrete
profile. We prove an all-agent characterization in this declared class: there
are `n+1` accepted suffix rules for `1<=c<=n`, one rule for `n<c<=2n`, and none
above `2n`. Exact searches for three through six agents independently
cross-check the theorem. A value-magnitude stress test finds
207 failures for the efficient threshold family on held-out `{0,1,2,3}`
profiles. A post-hoc exact value-lattice sensitivity run finds 66 rules and 60
independently replayed accepted rows at `max_value=3`. The result is a
reproducible narrow theorem and falsifiable benchmark, not a theorem for
continuous values or a claim of unrestricted mechanism-design novelty. As a
separate source-integrity study, six preregistered rational one-hidden-layer
ReLU fixtures with three to five agents have identical direct-source and
compiled certificates; an exact-real Z3 cross-check returns `unsat` for all
18 strict-bound counterexample queries. This is bounded verification evidence,
not a newly discovered mechanism or a generic neural-verification result.

## 1. Introduction

Public-project design exposes a basic tension: selecting the project whenever
total value covers cost is efficient, but its critical payments need not cover
the cost. Conversely, budget balance can require a more conservative allocation
rule and therefore lose welfare. Existing mechanism-design theory studies this
tension in broad quasi-linear domains, while automated mechanism-design work
shows how finite search can discover or reproduce rules. The practical gap is
an auditable benchmark in which the entire candidate class, verifier, negative
examples, and independent replay are shipped together.

This paper makes seven deliberately narrow contributions:

1. a typed finite public-project model with exact critical payments;
2. an antichain enumerator that covers every anonymous monotone rule in the
   chosen finite domain;
3. a cost-indexed welfare frontier and explicit efficient-rule counterexample;
4. serialized certificates replayed by an implementation that does not import
   the primary mechanism code.
5. a human-checkable all-agent proof explaining the accepted-count sequence,
   with a construction certificate covering n=1..12.
6. an executable-specification audit layer for published shallow max-affine
   VCG-redistribution formulas, with a standalone replay from serialized
   rational expressions.
7. a preregistered source-to-certificate cross-check for rational shallow ReLU
   fixtures, independently challenged by exact-real SMT queries.

## 2. Model

There are `n` agents with values `v_i` in `{0,1,2}` for a public project with
cost `c`. A direct mechanism reports `r` and chooses `q(r) in {0,1}`. Agent
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
- `q(2,...,2)=1`, excluding the vacuous never-build rule.

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

### 4.2 All-agent theorem and finite cross-check

The theorem covers every `n>=1` and integer cost. Define `q_k(v)=1` iff every
reported value is at least 1 and at least `k` reports equal 2. Then the
accepted rules are exactly `q_0,...,q_n` when `c<=n`, only `q_n` when
`n<c<=2n`, and none when `c>2n`. At the all-2 profile, anonymity makes every
critical payment equal; budget balance forces the common threshold to be 2
above `n`, which leaves only `q_n`. At or below `n`, monotonicity excludes any
active profile containing zero, and the remaining positive chain has exactly
the suffix rules; each active profile yields at least one unit per agent, so
budget balance follows. Full details are in `PUBLIC_PROJECT_THEOREM.md`.

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
The symbolic construction certificate checks 806 mechanisms for n=1..12; it
is a regression certificate for the proof, not a formal proof assistant.

### 4.3 Stress and falsification

On held-out values `{0,1,2,3}`, the six sum-threshold rules produce 207 recorded
budget/IC failures across 64 profiles per threshold. This is a deliberate
generalization boundary: success on `{0,1,2}` does not justify a continuous or
larger-value claim.

### 4.4 Value-lattice sensitivity

As a post-hoc sensitivity check, we repeated the exact three-agent search on
values `{0,1,2,3}`. The 20-state sorted lattice contains 66 anonymous
monotone rules. Accepted counts over costs `1,...,9` are
`15,15,15,4,4,4,1,1,1`, and all 60 serialized accepted rows pass the
standalone checker. This result is useful evidence that the frontier is not an
artifact of the three-value coding, but it remains exploratory: it does not
replace the preregistered `{0,1,2}` headline or establish a continuous-value
characterization.

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

The defensible contribution is a compact, replayable certificate and an exact
theorem for the specified ternary class. It is not a claim of a new universal
impossibility result or unrestricted mechanism-design novelty.

## 6. Reproducibility and falsification

The main JSON, scaling CSVs, and six-agent JSON contain the complete serialized accepted rows;
the independent checker reconstructs allocation and critical payments without
importing the primary verifier. The clean run reports 122 accepted rows and zero
independent replay failures. The held-out audit evaluates every one of the 64
profiles for each efficient threshold on values `{0,1,2,3}` and records 207
failures. These are positive and negative controls: the first tests certificate
integrity, while the second tests whether the finite result is being
over-generalized. Exact commands and SHA-256 hashes are in
`REPRODUCIBILITY_MANIFEST.md`.

## 7. Limitations and next work

The theorem's mechanism class is anonymous, deterministic, finite-valued, and
restricted to normalized critical payments. The study does not cover randomized
rules, subsidies, Bayesian objectives, continuous values, collusion, false-name
reports, asymmetric rules, or arbitrary payment schemes. The n=3..6 searches
are computational cross-checks; the proof itself is the all-agent result. The
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
python3 scripts/run_max_affine_certification.py
python3 scripts/verify_max_affine_certificate.py
python3 scripts/verify_source_network_certificates.py
python3 scripts/run_relu_benchmark.py
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-verification.txt
.venv/bin/python scripts/verify_relu_benchmark_z3.py
python3 scripts/run_uniform_repair_study.py
.venv/bin/python scripts/verify_uniform_repair_z3.py
```

The main JSON, cross-agent CSV, certificate, plot, specification, and claim
ledger are committed under `artifacts/`, `reports/`, and the repository root.

## 9. Conclusion

Exact search does not magically produce a universally optimal mechanism. This
study does provide a narrow all-agent characterization that a skeptical reader
can inspect: the proof fixes the accepted family, finite searches replay it,
the efficient comparator has a concrete failure, and the held-out stress test
records where the result stops generalizing. It is a serious candidate paper
or thesis chapter, but publication, a PhD, or a prize still requires external
novelty review, broader theory, and peer review.
