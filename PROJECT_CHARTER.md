# Project Charter

Status: frozen 2026-08-14. Experiment 67 is a finite, reproducible mechanism-design audit.

Question: within a two-agent binary-type, binary-choice direct-revelation domain, what is the complete deterministic allocation/payment frontier under incentive, feasibility, budget, fairness, and bounded coalition constraints, and can a seeded proposal search rediscover it?

Domain: profiles `(0,0),(0,1),(1,0),(1,1)`; value is `1{type=choice}`; integer payments are in `{-1,0,1}` (positive means paid to the mechanism); utilities are value minus payment; pointwise exact budget balance is required. Thus there are `6^4=1,296` candidate tables.

Acceptance: DSIC, ex-post IR, binary feasibility, exact budget balance, exact anonymity, truthful utility disparity at most `1` on every profile, and no joint report that strictly improves both fixed agents. Neutrality is audited and reported, but is not an acceptance requirement.

Primary baseline: zero-transfer anonymous OR (`choice=1` iff either report is `1`). Canonical comparators include AND, majority tie rules, constants, serial dictatorships, and VCG pivot; priority-majority is retained as a rejecting fairness diagnostic. Objectives are uniform allocative welfare, utility disparity, regret, revenue, and description length.

Evidence boundary: exhaustive enumeration plus a separately implemented checker is a complete result only on this frozen finite domain. The evolutionary loop is a rediscovery probe, not a coverage proof. No novelty, general theorem, deployment, randomized mechanism, continuous type, false-name, or real-world claim is made.
