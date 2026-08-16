# Publication strategy

## Editorial assessment

The strongest honest paper is a finite computational-characterization and
falsification benchmark. It is publishable only if the paper foregrounds the
exact coverage, machine-checkable certificates, independent replay, and the
negative held-out result. It should not be presented as a new impossibility
theorem, a universal mechanism, or a learned deployment system.

## Journal fit

| Priority | Venue | Fit and required revision |
|---|---|---|
| 1 | [Journal of Mechanism and Institution Design](https://www.mechanism-design.org/) | Closest scope: it explicitly welcomes rigorous theoretical, empirical, experimental, and practical mechanism studies. Submit after a careful economics rewrite, complete references, and author metadata. |
| 2 | [Autonomous Agents and Multi-Agent Systems](https://link.springer.com/journal/10458) | Plausible computational/MAS venue. Strengthen the automated-mechanism-design and independent-verification algorithmic contribution, and compare with a broader mechanism class. |
| 3 | [Games and Economic Behavior](https://www.sciencedirect.com/journal/games-and-economic-behavior) | A stretch target. It would require a theorem, a genuinely new economic implication, or a substantially broader result beyond this finite benchmark. |
| Not yet | [Journal of Artificial Intelligence Research](https://www.jair.org/index.php/jair/about) | Its charter requires high originality and significance plus clear practical or theoretical advancement. The current finite artifact is not yet strong enough for that bar without a new algorithmic or theoretical contribution. |

## Submission package

1. Convert `PAPER.md` to the target journal template and add author,
   affiliation, funding, conflict, and data/code-availability statements.
2. Include the repository commit, `REPRODUCIBILITY_MANIFEST.md`, certificates,
   raw frontier tables, and the independent replay instructions as a supplement.
3. Add a short cover letter stating the finite scope, the exact negative result,
   and why the work fits the selected journal; do not claim guaranteed novelty
   or acceptance.
4. Obtain a human coauthor/editorial read of the prior-art coverage and the
   economic interpretation before uploading. No external submission is made
   by this repository workflow.
