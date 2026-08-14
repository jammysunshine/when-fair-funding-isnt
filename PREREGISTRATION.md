# Preregistration — Experiment 67

Frozen before executing `scripts/run_experiment.py` on 2026-08-14.

Agents are `{0,1}`. Each true type and report is `0` or `1`; alternatives are `0` or `1`. A deterministic direct mechanism maps each report pair to `(choice, payment_0, payment_1)`. Payments are in `{-1,0,1}`, positive when paid to the mechanism; only pointwise zero-sum transfers are enumerated. Utility is `1{choice=true_type}-payment`. Outcomes are feasible iff choice is binary. The outside option is zero.

Truthful dominant-strategy incentive compatibility means that at each true profile, neither agent obtains strictly higher utility by switching their report. Ex-post IR means truthful utility is nonnegative at each profile. Exact budget balance means payments sum to zero at every report profile. Anonymity is measured and reported but is not an acceptance constraint because the priority tie-break baseline is intentionally asymmetric. Randomization, fairness constraints, coalitions, false names, and continuous types are excluded.

The uniform distribution over the four true profiles is used only for descriptive welfare/disparity metrics; verification is distribution-free over the finite domain. Baselines: priority-majority and the constant rules contained in the exhaustive search. The search boundary is all `6^4=1,296` tables: 2 choices times 3 zero-sum grid payment pairs at each of four profiles. A separate seeded evolutionary zero-transfer proposal loop uses config seed 67, population 64, and 40 generations. Every proposal is verified; it cannot establish coverage.

Primary completion threshold: exhaustive search reports exactly 1,296 candidates; the baseline passes primary and independent verifiers; all recorded accepted mechanisms satisfy the primary verifier; all six tests pass. No post-run tuning, profile exclusion, criterion changes, or reuse of an adversarial failed profile is permitted. The independent checker and frozen config provide the confirmation boundary.
