# Prior art and positioning

This study is deliberately positioned as a reproducible finite characterization and falsification benchmark, not as a new proof of the Green–Laffont impossibility theorem.

- Green–Laffont established the incompatibility of efficiency, strategyproofness, and budget balance in general quasi-linear public-good settings.
- Nath and Sandholm (Games and Economic Behavior, 2019) characterize a deterministic strategyproof budget-balanced mechanism as having a sink agent whose valuation is ignored, derive tight worst-case inefficiency bounds, and use optimization-based automated mechanism design for randomized finite domains.
- Conitzer and Sandholm (AAAI 2002) established automated mechanism design as a search problem over feasible mechanisms; their later complexity work shows why finite restricted classes and certificates matter.
- Guo et al. (Autonomous Agents and Multi-Agent Systems, 2024) apply machine-learning approaches to public-project mechanism design, motivating an exact checker rather than trusting learned proposals.

The contribution claimed here is narrower: an exact, solver-free certificate pipeline that enumerates *all anonymous monotone Boolean allocation rules* for a three-agent, three-level public-project domain under normalized critical payments, maps the cost-indexed weak-budget-balance frontier, and tests the resulting threshold family on held-out value magnitudes. This is a useful artifact/candidate computational result. It is not a claim that the finite frontier is a continuous-domain theorem, nor that the search discovers a previously unknown mechanism.

## Sources

See [`SOURCES.json`](SOURCES.json) for URLs and access dates. Primary sources used for technical positioning:

- [Nath & Sandholm, arXiv:1610.01443](https://arxiv.org/abs/1610.01443) and the published [Games and Economic Behavior record](https://ideas.repec.org/a/eee/gamebe/v113y2019icp673-693.html).
- [Conitzer & Sandholm, AAAI 2002](https://ojs.aaai.org/index.php/AAAI/article/view/7708).
- [Guo et al., 2024 public-project ML study](https://link.springer.com/article/10.1007/s10458-024-09647-8).
