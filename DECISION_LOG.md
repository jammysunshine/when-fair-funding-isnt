# Decision Log

| Decision | Timing | Rationale |
| --- | --- | --- |
| Freeze two agents, binary types/choices, integer transfer grid | Before implementation | Makes exact 1,296-table coverage possible while retaining transfers |
| Require DSIC, IR, feasibility, exact BB, anonymity, disparity, coalition predicate | Before frozen run | Machine-checkable incentive, fairness, and bounded robustness gate |
| Use anonymous OR as primary baseline; retain priority as diagnostic | Before frozen run | Primary baseline must satisfy the frozen fairness predicate; priority remains a meaningful rejecting comparator |
| Report neutrality but exclude it from acceptance | Before frozen run | Enables an explicit finite empty-intersection certificate without changing the main frontier |
| Freeze held-out confirmation threats before audit | Before adversarial audit | Prevents tuning against perturbation/distribution outcomes |
| Use exhaustive enumeration plus seeded evolutionary proposals | Before frozen run | Exact coverage and a genuinely separate discovery approach |
| Make no novelty/general claim | After prior-art review | Canonical binary rules are established prior art; evidence is finite |
