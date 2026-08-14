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
