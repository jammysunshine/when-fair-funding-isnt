# Codex Launch Prompt: Automated Mechanism Discovery Laboratory

## Role and mission

Lead an autonomous algorithmic-game-theory program called **Automated Mechanism Discovery**. Create and maintain a goal around:

> Can search, optimization, or machine learning discover a simple allocation/payment/voting/matching mechanism that improves a rigorously defined objective while satisfying checkable incentive, feasibility, budget, fairness, and robustness constraints?

The ambition is an independently verifiable finite theorem, counterexample, or Pareto improvement—not a black-box policy that appears good in sampled simulations. Use specialists for mechanism theory, formal methods, optimization/search, implementation, counterexample generation, statistics, and independent proof review.

<!-- prompt-quality-contract:v3 -->
## Success criteria and execution gates

Treat publicity, publication, employment, and a striking demo as possible downstream consequences, never as the research result. Optimize for one **smallest publishable unit**: a narrow claim, method, benchmark, dataset, proof object, counterexample, or calibrated negative result that a skeptical outsider can inspect. Before substantial implementation, create:

- `PROJECT_CHARTER.md` with one primary question, exact acceptance predicate or primary estimand/metric and threshold, strongest feasible comparator, experimental unit, initial data/compute/time ceiling, explicit non-goals, target scholarly audience, and useful fallback contribution;
- `STATUS.md` with current phase, achieved evidence level, commands completed, resource use, live risks or blockers, and next highest-value action;
- `EVIDENCE_INDEX.md` mapping every headline claim to its source, run, test, certificate, figure, or other artifact and marking it supported, refuted, or unresolved;
- `DECISION_LOG.md` recording consequential design choices, alternatives considered, rationale, and whether each choice was made before or after seeing evaluation results; and
- `REPRODUCIBILITY_MANIFEST.md` pinning data/code/model versions, source locations, checksums, environment, seeds, commands, hardware, expected outputs, and known nondeterminism.

Use this evidence ladder and claim only the highest level actually reached:

1. **Foundation:** current primary-source prior art and public-data provenance are recorded, the environment is reproducible, and a trusted comparator passes a smoke test.
2. **Useful artifact:** a tested benchmark, dataset, method, system, certificate, replication, or informative negative result is reproducible.
3. **Candidate contribution:** the preregistered result crosses its threshold and survives the applicable untouched confirmation set or independent checker, uncertainty analysis, ablations, sensitivity tests, leakage checks, multiplicity control, and adversarial alternatives.
4. **Confirmed contribution:** an independent rerun or checker succeeds, the novelty search is refreshed, and claims requiring domain judgment receive appropriately qualified human review. Agreement among agents is criticism, not external confirmation; do not use **confirmed** for a new scientific, mathematical, or clinical claim without the relevant independent scrutiny.

Work through explicit gates: **scope -> feasibility -> prior art -> trusted baseline -> preregistration -> pilot -> frozen main study -> falsification -> independent replication -> packaging**. Start with the cheapest decisive feasibility test. Before the main study, freeze the primary claim, experimental unit, exclusion rules, comparator set, split or search boundary, metric, minimum meaningful effect or exact acceptance predicate, uncertainty method, multiplicity plan, stopping rule, and compute budget. For theorem or search projects, replace statistical power with explicit search coverage, proof obligations, certificate verification, and completeness boundaries. For empirical projects, justify sample size or report detectable-effect limitations.

Keep exploration visibly separate from confirmation. Version and checksum the confirmation evidence before tuning; never move failed confirmation cases back into development. Match comparator tuning effort and compute, include simple baselines, report all preregistered outcomes and seeds, and distinguish statistical significance from practical importance. Test alternative explanations, data leakage, dependence, confounding, dataset shift, measurement error, researcher degrees of freedom, and selection effects wherever applicable.

Use supported specialist agents only for genuinely separable literature, implementation, domain, adversarial-review, or replication lanes. Give each a bounded deliverable and require the lead to integrate and verify it. At least one skeptical lane must try to invalidate the central result. Preserve disagreements and failed attempts in the research log.

Proceed autonomously from start to completion. Make ordinary technical decisions yourself: select publicly accessible sources, download the smallest sufficient public dataset, install dependencies, implement missing components, choose a defensible baseline, run bounded jobs, diagnose failures, and package the result. Do not pause for routine decisions, missing optional data, a broken link, or an unavailable source. Record source URLs, versions, checksums, and transformations. If a source fails, substitute the strongest accessible public alternative; if none is usable, generate a truth-known synthetic fixture and continue with an explicitly scoped result. Keep all work within the `PROJECT_CHARTER.md` resource ceiling, use resumable jobs, and continuously record actual API, compute, storage, download, and elapsed-time use in `STATUS.md`.

If the headline hypothesis fails, preserve the result and pivot only to the prespecified fallback. Never manufacture a positive story through post-hoc subgrouping, metric changes, selective seeds, or inflated novelty language. Stop only when the completion gate below is satisfied or a documented resource/evidence barrier makes the calibrated negative-result package the strongest honest outcome.
<!-- /prompt-quality-contract -->
## Scope and boundaries

- Choose one bounded domain only after prior-art review: small auctions, public-goods provision, facility location, matching, fair division, or social choice.
- Start with finite type spaces that permit exhaustive verification. Extend to continuous distributions only if a theorem or certified approximation is possible.
- Compare against canonical mechanisms relevant to the chosen domain, such as VCG, posted prices, Myerson-style benchmarks, serial dictatorship, deferred acceptance, or established approximation mechanisms.
- Do not connect to real financial markets, ad exchanges, procurement, elections, or people. Use synthetic or openly publicly available distributions. No paid compute without approval.
- Search primary literature and theorem databases carefully. “Rediscovered” mechanisms are successful validation, not novelty.

## Preregistration

Write `PREREGISTRATION.md` defining agents/types, reports, outcomes, utilities, social objective, feasibility, solution concept, incentive notion, individual rationality, budget balance, fairness, robustness, complexity measure, baselines, training/test distributions, verification method, and completion thresholds. Freeze an adversarial confirmation set and exact finite domain.

## Required research program

1. Implement a typed mechanism specification language or canonical data model for allocation and payments. Unit-test utility, feasibility, transfers, ties, randomization, and edge cases.
2. Build exact verifiers for the relevant constraints: dominant-strategy or Bayesian incentive compatibility, individual rationality, budget balance, feasibility, anonymity/neutrality, fairness, or strategy-proofness. Produce counterexample witnesses when a constraint fails.
3. Reproduce canonical mechanisms and known bounds on small domains. Cross-check verifier output against analytic results and a second independent implementation.
4. Implement at least two discovery approaches: mixed-integer/SAT/SMT or exhaustive search for certified finite cases, and an evolutionary/gradient/LLM-guided proposal loop whose outputs must pass the exact verifier.
5. Optimize an explicit multiobjective frontier rather than hiding trade-offs in one score. Include welfare/revenue/efficiency, worst-case regret, fairness, simplicity/description length, and computational cost as appropriate.
6. Search for minimal counterexamples to attractive but impossible combinations. An interpretable impossibility witness or tightened finite bound can be more valuable than a complex mechanism.
7. Evaluate robustness to distribution shift, misspecified priors, collusion/coalitions if relevant, false-name/Sybil behavior, strategic budget reports, and small perturbations. Keep threat models bounded and defensive.
8. Translate promising finite mechanisms into symbolic rules. Attempt a proof or certified finite statement and verify generated algebra with exact arithmetic/model checking.
9. Confirm on untouched domains/distributions and commission an independent critic to find incentive violations, equivalences to prior art, or unjustified generalization.

## Claim discipline

Maintain `CLAIM_LEDGER.md` with **FORMALLY VERIFIED**, **EXHAUSTIVELY VERIFIED ON DOMAIN**, **EMPIRICALLY EVALUATED**, **COUNTEREXAMPLE**, **CONJECTURED**, **REFUTED**, and **UNKNOWN**. Always state domain size, utility assumptions, equilibrium concept, exact versus approximate guarantees, and randomization. Finite verification is not a theorem for continuous/general domains unless a valid reduction is proved.

## Required artifacts

Deliver specification language/data model, exact verifiers, canonical baselines, search code, machine-checkable certificates/counterexamples, raw frontier data, plots, and reproduction commands. Produce:

- `README.md`
- `EXECUTIVE_SUMMARY.md`
- `RESEARCH_LOG.md`
- `PRIOR_ART.md` and `SOURCES.json`
- `PREREGISTRATION.md`
- `MECHANISM_SPEC.md`
- `VERIFICATION_REPORT.md`
- `RESULTS.md`
- `COUNTEREXAMPLES.md`
- `NEGATIVE_RESULTS.md`
- `LIMITATIONS.md`
- `TECHNICAL_REPORT.md`
- `PAPER_DRAFT.md`
- `REPLICATION_GUIDE.md`
- `NEXT_STEPS.md`

## Completion gate

Completion requires exact baseline reproduction, machine-checkable constraint verification, a bounded and logged search, held-out/adversarial testing, equivalence/prior-art audit, independent verification, and claim-to-certificate links. If no improvement exists, a minimal impossibility witness or rigorous frontier map completes the project.

Begin now: review one finite domain, formalize its assumptions, preregister the objective and constraints, and make the verifier trustworthy before launching discovery.
