# Certificate-first exact frontiers for no-deficit public-project mechanisms

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
profile. An exact exploratory extension enumerates 32 and 64 rules for four
and five agents, respectively, across all costs `1,...,2n`; 74 serialized
accepted rows pass a standalone checker. A value-magnitude stress test finds
207 failures for the efficient threshold family on held-out `{0,1,2,3}`
profiles. A post-hoc exact value-lattice sensitivity run finds 66 rules and 60
independently replayed accepted rows at `max_value=3`. The result is a
reproducible finite characterization and a falsifiable
benchmark, not a theorem for continuous values or a claim of unrestricted
mechanism-design novelty.

## 1. Introduction

Public-project design exposes a basic tension: selecting the project whenever
total value covers cost is efficient, but its critical payments need not cover
the cost. Conversely, budget balance can require a more conservative allocation
rule and therefore lose welfare. Existing mechanism-design theory studies this
tension in broad quasi-linear domains, while automated mechanism-design work
shows how finite search can discover or reproduce rules. The practical gap is
an auditable benchmark in which the entire candidate class, verifier, negative
examples, and independent replay are shipped together.

This paper makes four deliberately narrow contributions:

1. a typed finite public-project model with exact critical payments;
2. an antichain enumerator that covers every anonymous monotone rule in the
   chosen finite domain;
3. a cost-indexed welfare frontier and explicit efficient-rule counterexample;
4. serialized certificates replayed by an implementation that does not import
   the primary mechanism code.

The scaling experiment is exploratory. It tests whether the finite pattern is
stable from three to five agents; it does not convert an observed pattern into
an asymptotic theorem.

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

### 4.2 Exact cross-agent scaling

The exploratory extension evaluates every cost from 1 through `2n`:

| agents | anonymous rules | accepted counts by cost | costs with one accepted rule |
|---:|---:|---|---|
| 3 | 16 | 4,4,4,1,1,1 | 4,5,6 |
| 4 | 32 | 5,5,5,5,1,1,1,1 | 5,6,7,8 |
| 5 | 64 | 6,6,6,6,6,1,1,1,1,1 | 6,7,8,9,10 |

The serialized accepted rows total 74 and all pass the standalone checker.
These data support a finite pattern—`n+1` accepted rows through cost `n`,
then one row above cost `n`—for the three tested values of `n`. They do not
prove that pattern for arbitrary agent counts.

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

The defensible contribution is thus a compact, replayable certificate and finite
frontier benchmark. The finite statement supported by the artifacts is: for
each `n` in `{3,4,5}` and each integer cost in `1,...,2n`, the declared
anonymous monotone class was exhaustively enumerated and the reported accepted
counts were independently replayed. This is a statement about the specified
finite class only. Any stronger novelty or generalization claim requires new
mathematical work and broader comparisons.

## 6. Reproducibility and falsification

The main JSON and scaling CSVs contain the complete serialized accepted rows;
the independent checker reconstructs allocation and critical payments without
importing the primary verifier. The clean run reports 74 accepted rows and zero
independent replay failures. The held-out audit evaluates every one of the 64
profiles for each efficient threshold on values `{0,1,2,3}` and records 207
failures. These are positive and negative controls: the first tests certificate
integrity, while the second tests whether the finite result is being
over-generalized. Exact commands and SHA-256 hashes are in
`REPRODUCIBILITY_MANIFEST.md`.

## 7. Limitations and next work

The mechanism class is anonymous, deterministic, finite-valued, and restricted
to normalized critical payments. The study does not cover randomized rules,
subsidies, Bayesian objectives, continuous values, collusion, false-name
reports, or arbitrary payment schemes. The cross-agent extension is exploratory
and only reaches five agents. The stress audit is intentionally negative for
the efficient threshold family; it is not an empirical estimate of deployment
risk. Before submission, a researcher should add a proof or counterexample for
the observed scaling pattern, compare unrestricted transfers and subsidies,
and obtain an independent external replication.

## 8. Reproduction

```bash
python3 -m unittest discover -s tests -v
python3 scripts/run_public_project_study.py
python3 scripts/verify_public_project_certificate.py
python3 scripts/run_value_extension.py
```

The main JSON, cross-agent CSV, certificate, plot, specification, and claim
ledger are committed under `artifacts/`, `reports/`, and the repository root.

## 9. Conclusion

Exact search does not magically produce a universally optimal mechanism. It
does produce a finite result that a skeptical reader can inspect: every rule in
the declared class was tested, the efficient comparator has a concrete failure,
the scaling rows were independently replayed, and the held-out stress test
records where the result stops generalizing. That is the appropriate evidence
level for this artifact.
