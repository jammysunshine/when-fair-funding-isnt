# Handoff for next model

## Objective
Continue Experiment 67 / public-project frontier work: complete reproducible, publication-oriented finish for the coalition-robust finite-domain frontier and decide what can and cannot be claimed in a peer-reviewed paper.

## Current repo state
- Branch: `main`
- Working tree: clean once this session's changes are committed (Phase X coalition work plus the new independent baseline audit)
- All ten coalition run/verify commands (the original eight plus the new baseline-audit pair) re-ran clean from a fresh state: 0 independent failures across frontier, scaling (`n=3..5`), scaling-extended (`n=3..6`), the `max_value=3` frontier extension, and the baseline audit.
- Full test suite: 77/77 passing.
- Fixed one digest transcription typo in `VERIFICATION_REPORT.md` (`eaba6dc76` -> `eabe6dc76`) found during hash reconciliation (prior session).
- New this session: `scripts/run_public_project_coalition_baseline_audit.py` /
  `scripts/verify_public_project_coalition_baseline_audit.py` (config
  `configs/public_project_coalition_baseline_audit.json`) independently audit
  the canonical efficient/pivotal mechanism against the same coalition bar
  across all four prior domains. Finding: single-agent DSIC everywhere, but
  fails coalition-cap-2 DSIC in 66/75 rows (10/11 selected checks), decoupled
  from its separately known budget-balance deficit. 0 independent-replay
  mismatches across 75 rows. This is HANDOFF.md task 4's independent baseline
  audit, now complete.
- Also new this session: `scripts/run_public_project_false_name_audit.py` /
  `scripts/verify_public_project_false_name_audit.py` (config
  `configs/public_project_false_name_audit.json`) extend the falsification
  program to false-name manipulation: can a single real agent gain by
  fabricating extra fake report identities against the canonical
  efficient/pivotal mechanism? Finding: `fake_budget=0` positive control
  shows 0 manipulable rows (confirms harness correctness); at
  `fake_budget in {1,2}` across `n_real=3,4,5`, 48 of 72 rows and 6 of 9
  selected checks are manipulable. Independent verifier is a standalone
  closed-form reimplementation (no import of `public_project.py`); 0
  mismatches across 72 rows. This is the coalition-class extension
  requested after task 4 ("the second part": false-name attacks, in
  preference to randomized mechanisms which would need a larger model
  change to support lottery allocation).
- Also new this session: `scripts/verify_public_project_coalition_lemma.py`
  proves (not searches) a closed-form sufficient condition for
  coalition-manipulability: for every `n>=2`, `max_value=m`,
  `cost<=(n-1)*m`, the grand-coalition "everyone reports `m`" deviation
  builds the project at zero payment to every agent. Cross-checked against
  all 75 baseline-audit rows with 0 false positives; a separate exhaustive
  check (`n=3,4`, `m=2,3`, 0 counterexamples) explains why `cost=n*m` is the
  baseline audit's sole robust exception (any successful proper-coalition
  deviation there forces members to pay their own full report). This is the
  "prove a general lemma instead of relying on brute-force counterexamples"
  novelty lever discussed with the user after they asked how to make the
  work publishable — the user replied "ok" to proceeding with it.
- Also new this session: `scripts/verify_public_project_coalition_characterization.py`
  closes the gap the lemma above left open (14/75 baseline-audit rows with
  `(n-1)*m<cost<n*m` were fragile but unexplained). Derives, by convexity, the
  exact minimum coalition payment `k*max(0,(cost-S_O)-(k-1)*m)` for any
  coalition size and outsider value-sum, plus the exact worst-case
  (bang-bang-extremal) truthful payment distribution, and combines them into a
  bounded-sweep existence check — no report-level search. Reproduces the
  baseline audit's exact `min_failing_coalition_size` on all `75/75` rows
  (exact match, not just no-false-positives) and evaluates at `n=20` in
  microseconds, far beyond brute-force reach. This is the full
  necessary-and-sufficient characterization the user asked for after "can you
  turn it into from a modest contribution to a fantastic contribution."
  Folded into `PAPER.md` (new §4.12, abstract, contribution 11,
  positioning table, limitations, conclusion), `CLAIM_LEDGER.md`, `STATUS.md`,
  `VERIFICATION_REPORT.md`, `REPRODUCIBILITY_MANIFEST.md`.

## Frozen configuration
- Core domain: public-project mechanism design with anonymous monotone rules
- Base domain profile: `n=3`, `max_value=2`, `cost=1..6`, `max_coalition_size=2` unless noted
- Frontier artifact for this run used config `configs/public_project_coalition_frontier.json`
- Coalition robustness target: cap-2 deviations; exact frontier replay with independent verifier

## Artifact paths (current)
- `configs/public_project_coalition_frontier.json`
- `configs/public_project_coalition_scaling.json`
- `configs/public_project_coalition_scaling_extended.json`
- `configs/public_project_coalition_value3_frontier.json`
- `scripts/run_public_project_coalition_frontier.py`
- `scripts/verify_public_project_coalition_frontier.py`
- `scripts/run_public_project_coalition_scaling.py`
- `scripts/verify_public_project_coalition_scaling.py`
- `scripts/run_public_project_coalition_scaling_extended.py`
- `scripts/verify_public_project_coalition_scaling_extended.py`
- `scripts/run_public_project_coalition_value3_frontier.py`
- `scripts/verify_public_project_coalition_value3_frontier.py`
- `artifacts/public_project_coalition_frontier.json`
- `artifacts/public_project_coalition_frontier_certificate.json`
- `artifacts/public_project_coalition_scaling.json`
- `artifacts/public_project_coalition_scaling_certificate.json`
- `artifacts/public_project_coalition_scaling_extended.json`
- `artifacts/public_project_coalition_scaling_extended_certificate.json`
- `artifacts/public_project_coalition_value3_frontier.json`
- `artifacts/public_project_coalition_value3_frontier_certificate.json`
- `configs/public_project_coalition_baseline_audit.json`
- `scripts/run_public_project_coalition_baseline_audit.py`
- `scripts/verify_public_project_coalition_baseline_audit.py`
- `artifacts/public_project_coalition_baseline_audit.json`
- `artifacts/public_project_coalition_baseline_audit_certificate.json`
- `configs/public_project_false_name_audit.json`
- `scripts/run_public_project_false_name_audit.py`
- `scripts/verify_public_project_false_name_audit.py`
- `artifacts/public_project_false_name_audit.json`
- `artifacts/public_project_false_name_audit_certificate.json`
- `scripts/verify_public_project_coalition_lemma.py`
- `artifacts/public_project_coalition_lemma_certificate.json`
- `scripts/verify_public_project_coalition_characterization.py`
- `artifacts/public_project_coalition_characterization_certificate.json`
- `scripts/verify_public_project_coalition_characterization_extended.py`
- `artifacts/public_project_coalition_characterization_extended_certificate.json`

## Exact commands already expected
```bash
python3 scripts/run_public_project_coalition_frontier.py
python3 scripts/verify_public_project_coalition_frontier.py
python3 scripts/run_public_project_coalition_scaling.py
python3 scripts/verify_public_project_coalition_scaling.py
python3 scripts/run_public_project_coalition_scaling_extended.py
python3 scripts/verify_public_project_coalition_scaling_extended.py
python3 scripts/run_public_project_coalition_value3_frontier.py
python3 scripts/verify_public_project_coalition_value3_frontier.py
python3 scripts/run_public_project_coalition_baseline_audit.py
python3 scripts/verify_public_project_coalition_baseline_audit.py
python3 scripts/run_public_project_false_name_audit.py
python3 scripts/verify_public_project_false_name_audit.py
python3 scripts/verify_public_project_coalition_lemma.py
python3 scripts/verify_public_project_coalition_characterization.py
python3 scripts/verify_public_project_coalition_characterization_extended.py
python3 scripts/generate_frontier_report.py
python3 -m unittest discover -s tests -v
```

## What has been established
- Finite-domain phase exists and is reproducible at least through the coalition-cap-2 frontier pass.
- In the frozen frontier with cap-2, DSIC frontier shrank from 4 accepted entries to 2 at cost=3.
- Independent frontier replay and certificate flow are integrated in the current documentation and logs.
- Existing result is a bounded finite artifact; not yet a broad publication-grade general theorem.

## Immediate remaining tasks
1. ~~Stage/commit `HANDOFF` plus untracked Phase X configs/scripts/artifacts.~~ Done (`41fa06c`).
2. ~~Re-run experiment commands from clean state and refresh `REPRODUCIBILITY_MANIFEST.md` hashes.~~ Done, all zero-failure.
3. ~~Reconcile mismatches in `STATUS.md`, `EVIDENCE_INDEX.md`, `VERIFICATION_REPORT.md`.~~ Done.
4. ~~Add paper-grade extension: independent baseline audit before any submission claim.~~ Done: the canonical efficient/pivotal mechanism is coalition-fragile (fails cap-2 DSIC in 66/75 rows), independently replayed with 0 mismatches.
5. ~~Extend the coalition claim (false-name attacks or randomized mechanisms).~~ Done: chose false-name attacks over randomized mechanisms (would need a larger model change to support lottery allocation). The mechanism is manipulable by fabricated fake identities: 48/72 rows, 6/9 selected checks, positive control clean, 0 independent-replay mismatches. Committed as `7013278`.
6. ~~Make the coalition/false-name results genuinely novel rather than a
   replication of Yokoo/Sakurai/Matsubara 2004 and Green--Laffont.~~ Done
   this session: proved a general closed-form lemma
   (`scripts/verify_public_project_coalition_lemma.py`, `cost<=(n-1)*m` =>
   grand-coalition zero-payment manipulation for every `n,m`, not just
   searched cells) and used it to explain the baseline audit's one robust
   row (`cost=n*m`). Folded into `PAPER.md` §4.11, positioning table,
   abstract, contribution list, limitations, conclusion, plus
   `CLAIM_LEDGER.md`/`STATUS.md`/`VERIFICATION_REPORT.md`/
   `REPRODUCIBILITY_MANIFEST.md`. Committed as `976d753`.
7. ~~Close the gap the lemma leaves open (14/75 fragile rows with
   `(n-1)*m<cost<n*m` unexplained) into a full necessary-and-sufficient
   characterization.~~ Done this session:
   `scripts/verify_public_project_coalition_characterization.py` derives
   exact minimum-payment and worst-case-truthful-payment formulas by
   convexity, reproduces `min_failing_coalition_size` exactly on all 75
   baseline-audit rows, and scales to `n=20` in microseconds. Folded into
   `PAPER.md` §4.12 plus all other tracking docs. Committed as `7c8ac0b`.
8. ~~Extend the characterization beyond 75 rows, quantify cheating gains in
   value units, and generalize/stress-test further.~~ Done this session:
   `scripts/verify_public_project_coalition_characterization_extended.py`
   brute-force-verifies 70 new `(n,max_value,cost)` cells (larger value caps
   at every previously tested agent count), 0 mismatches, total 145
   independently verified rows; computes exact free-gain size per fragile
   cell (up to 5 value units in the new rows); and runs a formula-only sweep
   to `n=40`, `max_value=15` (not brute-force re-verified — infeasible at
   that scale) finding 99.2% fragility at coalition size 2, gains up to 15
   value units. Folded into `PAPER.md` §4.13 plus all other tracking
   docs. Committed as `0e369ef`.
9. ~~Add a practical/policy-implications section, a catchy subtitle, and an
   editorial "de-AI" pass.~~ Done this session: `PAPER.md` gained a
   subtitle under the H1 title and a new §8 "Practical and policy
   implications" (real-world analogues, explicit non-audit caveats, what
   changes for a designer, the concrete risk pattern, a designer checklist,
   and a closing disclaimer that this is not a repair or behavioral claim);
   old §8 Reproduction and §9 Conclusion renumbered to §9/§10. Ran a
   diagnostic grep for classic AI-writing tells (moreover, furthermore, in
   conclusion, delve into, tapestry, landscape, etc.) across the whole file:
   zero matches, so no rewrite was needed. No new script/artifact, so
   `REPRODUCIBILITY_MANIFEST.md` is unchanged.

## Possible further extensions (not started, optional)
- Randomized mechanisms (lottery allocation) — would need a larger model change; not attempted.
- Brute-force verification of the large-scale formula-only sweep (`n>6`) would need a faster (non-Python-loop) reimplementation to be feasible.

## Commit practice
- Preserve commit identity:
  - `Mohit Mendiratta <mohit@zenith.com.au>`
- No AI attribution/Co-Authored trailers in git metadata.
- Push fallback command if GitHub returns 403 write-access errors:
  - `env -u GH_TOKEN git -c credential.helper='!gh auth git-credential' push`

## SSRN submission status (separate session, browser automation)
- Submitted 2026-08-16. SSRN Abstract ID **7293498**, status: pending editorial screening.
- Abstract page (live once approved): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7293498
- License: CC-BY. JEL codes D82/H41/C72. Classifications: "Other Microeconomics: Asymmetric & Private Information", "Public Economics: Publicly Provided Goods Alert", "Non-Cooperative Games" (SSRN's taxonomy has no literal node matching the paper's stated ERN path, so leaf-level equivalents were chosen and verified via tooltip JEL mapping).
- Not yet done: connect ORCID to SSRN author profile (needs user, may require account creation); arXiv submission (needs an endorser); Stack Exchange post / cold-email outreach (drafted earlier, unsent — needs explicit send confirmation).
- Note: this HANDOFF.md's other sections predate this entry and belong to a parallel research-extension session on the same repo — unrelated to SSRN submission mechanics.
- Related/alternate identifiers field (should link to `https://github.com/jammysunshine/research-showcase/tree/main/67-when-fair-funding-isnt`, folder renamed 2026-08-16 from `67-automated-mechanism-discovery` to match this repo's name) is blocked until SSRN's editorial screening clears — no "Edit" affordance exists while status is PRELIMINARY_UPLOAD. Already user-authorized ("Yes, update it"); just needs a return visit once status changes.

## Zenodo GitHub archiving access (same session)
- Restricted to exactly two repos in Zenodo's own "Enabled Repositories" toggle (`zenodo.org/account/settings/github/`): `jammysunshine/when-fair-funding-isnt` (DOI `10.5281/zenodo.21964295`) and `jammysunshine/research-showcase` (newly enabled, no release/DOI cut yet).
- All 8 other jammysunshine repos remain toggled OFF (never archived by Zenodo).
- Note: GitHub's OAuth grant to Zenodo is account-wide (Zenodo is a legacy OAuth App, not a GitHub App) — GitHub itself has no per-repo restriction UI for it, only an all-or-nothing "Revoke access". Left untouched deliberately, since revoking would also kill the working `when-fair-funding-isnt` archive. Per-repo control lives entirely in Zenodo's own toggle, which now reflects the desired 2-repo state.

## Evidence-artifact push fix (same session)
- A cross-session peer flagged missing artifact citations; peer's specific 5-file list was wrong (all 5 existed locally), but the real issue was real: a blanket `artifacts/` rule in `.gitignore` had silently excluded 18 locally-generated artifact JSONs (coalition/scaling/characterization/false-name/relu-benchmark, ~20MB total) from every prior push, even though `RESULTS.md`/`VERIFICATION_REPORT.md` cite them by path.
- Fixed: force-added and pushed all 18 as `45abd39` (confirmed on `origin/main`). `.gitignore`'s `artifacts/` rule itself was left as-is (not narrowed) — future artifact generations will need explicit `git add -f` until/unless that's revisited.
- Not yet done: reply to the peer session confirming the fix so they can re-sync the `research-showcase` copy.

SAFE FOR LUNA HANDOFF
