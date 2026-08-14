# Preregistration — Experiment 67

Frozen 2026-08-14 before the frozen run. Agents, types, alternatives, reports, and profile order are all binary and fixed. A mechanism is a total four-row table `(choice,p0,p1)` with payments in `{-1,0,1}` and pointwise zero-sum transfers. Utility is `1{choice=type}-payment`; the outside option is zero.

The primary acceptance predicate is distribution-free: DSIC, ex-post IR, binary feasibility, exact budget balance, exact anonymity (swapped reports leave choice unchanged and swap payments), truthful utility disparity `<=1`, and two-agent coalition strategyproofness (no joint report strictly improves both fixed identities). Neutrality is measured but deliberately excluded from acceptance so its empty intersection can be certified.

The primary baseline is `anonymous_or`; canonical comparators are AND, majority with both fixed tie breaks, both serial dictatorships, constants, and both VCG pivot tie breaks. Uniform-profile welfare and disparity are descriptive only. Search is exhaustive over `6^4=1,296` tables. The seeded proposal loop is seed `67`, population `64`, `40` generations and every proposal is verified.

The confirmation set is frozen in `configs/confirmation_67.json` before audit: point masses, diagonal/disagreement-heavy and asymmetric distributions; coalitions of the two fixed identities; value magnitudes `{0,1,2}` with unchanged binary favorites. False names and budget reports are explicitly out of scope. No post-run tuning or criterion changes are allowed.

Completion requires exact candidate and accepted counts, both checker frontiers equal, baseline reproduction, held-out/adversarial checks, a machine-readable certificate, and passing regression tests. These gates establish only a finite certified result.
