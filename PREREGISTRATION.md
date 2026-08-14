# Preregistration: public-project exact frontier

Frozen before the main run on 2026-08-15.

- Agents/types: 3 agents, each value in `{0,1,2}` for a binary public project.
- Cost: each integer `c=1,...,6` is evaluated separately.
- Mechanisms: deterministic, direct, anonymous, monotone Boolean allocation rules over sorted report states; exactly 16 rules per cost.
- Payments: normalized discrete critical values, zero when the project is not built.
- Constraints: DSIC, ex-post IR, feasibility, anonymity, and weak budget balance.
- Primary objective: minimum worst-case additive social-welfare regret versus `max(0,Σv-c)`; secondary expected welfare under uniform profiles.
- Baselines: efficient sum-threshold rule, every accepted frontier rule, and seeded sum-threshold proposal loop.
- Confirmation: independent checker over every serialized accepted table; held-out sum-threshold audit over all 64 profiles with values `{0,1,2,3}`.
- Stopping: no tuning after observing frontier outputs; report all costs, accepted counts, witnesses, and held-out failures.
- Completion: artifacts, tests, hashes, commands, limitations, and claim-to-evidence links committed together.

## Exploratory scaling extension

The post-main extension is governed by `SCALING_EXTENSION_PROTOCOL.md`. It
enumerates the same mechanism class exactly for `n=3,4,5` and all costs
`1..2n`. It is reported as a separate finite-scaling result, not as a change
to the original three-agent preregistration.

## Post-hoc theorem extension

After the frozen analysis, a separate proof and regression certificate were
added for all `n>=1` in the same ternary mechanism class. This does not alter
the preregistered estimand: it explains the finite scaling counts and is
reported as post-hoc mathematical analysis, with its own artifact and tests.
