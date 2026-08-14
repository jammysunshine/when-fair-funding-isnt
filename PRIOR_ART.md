# Prior art and positioning

This study is a reproducible finite characterization and falsification benchmark. It is not a new proof of a classical impossibility theorem and does not claim to rediscover a previously unknown mechanism.

| Line of work | What is already established | Boundary of this study |
|---|---|---|
| Green and Laffont; Ohseto; Moulin | Public-project and cost-sharing theory characterizes strong incentive/efficiency/budget trade-offs and important strategy-proof classes. | We instantiate a much smaller finite, anonymous, deterministic class; we do not extend those theorems. |
| Nath and Sandholm (2019) | General quasi-linear efficiency/budget-balance results, tight inefficiency bounds, and automated optimization for finite randomized domains. | We provide an exhaustive certificate for a different normalized critical-payment class, not a competing general characterization. |
| Conitzer and Sandholm (2002) | Automated mechanism design can search a declared finite mechanism space subject to feasibility and incentive constraints. | We contribute a compact solver-free enumeration/replay artifact specialized to public projects. |
| Guo et al. (2024) | Machine-learning approaches can propose public-project mechanisms. | Our result is a checkable benchmark for proposals, not a learned mechanism or an empirical deployment claim. |

The claimed contribution is therefore narrow but falsifiable: enumerate *all anonymous monotone Boolean allocation rules* for the frozen three-agent, three-level domain under normalized critical payments; compute the cost-indexed weak-budget-balance frontier; serialize every accepted row; replay it with an independent checker; and test the efficient threshold family on held-out value magnitudes. The finite frontier is a useful computational artifact and candidate contribution. It is not a continuous-domain theorem, an unrestricted transfer result, or evidence of universal optimality.

## Sources

See [`SOURCES.json`](SOURCES.json) for URLs and access dates. Primary sources used for technical positioning:

- [Nath & Sandholm, arXiv:1610.01443](https://arxiv.org/abs/1610.01443) and the published [Games and Economic Behavior record](https://ideas.repec.org/a/eee/gamebe/v113y2019icp673-693.html).
- [Conitzer & Sandholm, AAAI 2002](https://ojs.aaai.org/index.php/AAAI/article/view/7708).
- [Guo et al., 2024 public-project ML study](https://link.springer.com/article/10.1007/s10458-024-09647-8).
- [Green & Laffont, *Incentives in Public Decision Making*](https://green.scholars.harvard.edu/publications/incentives-public-decision-making).
- [Ohseto, 2000, public-project characterization](https://www.sciencedirect.com/science/article/pii/S0899825699907558).
- [Moulin, 1994, serial cost sharing](https://academic.oup.com/restud/article-abstract/61/2/305/1517585).
