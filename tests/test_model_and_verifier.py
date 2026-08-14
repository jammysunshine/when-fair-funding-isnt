import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from mechanism_discovery.independent_verifier import check
from mechanism_discovery.model import Mechanism, Outcome, PROFILES, priority_majority, utility
from mechanism_discovery.search import exhaustive_search, evolutionary_search
from mechanism_discovery.verifier import metrics, verify


class ModelAndVerifierTests(unittest.TestCase):
    def test_utility_includes_transfer(self):
        self.assertEqual(utility(1, Outcome(1, (1, 0)), 0), 0)
        self.assertEqual(utility(0, Outcome(1, (-1, 1)), 0), 1)

    def test_baseline_is_accepted_by_both_checkers(self):
        mechanism = priority_majority()
        self.assertTrue(verify(mechanism).accepted)
        self.assertTrue(check(mechanism)["accepted"])
        self.assertEqual(metrics(mechanism)["expected_welfare"], 1.5)

    def test_dsic_counterexample_contains_profitable_deviation(self):
        mechanism = Mechanism(tuple(Outcome(1 - p[0], (0, 0)) for p in PROFILES), "anti_agent_0")
        report = verify(mechanism)
        self.assertFalse(report.dsic)
        witness = next(w for w in report.witnesses if w.property == "dsic")
        self.assertIsNotNone(witness.deviation)
        self.assertFalse(check(mechanism)["accepted"])

    def test_budget_balance_and_ir_witnesses(self):
        mechanism = Mechanism(tuple(Outcome(0, (1, 0)) for _ in PROFILES), "bad_transfers")
        report = verify(mechanism)
        self.assertFalse(report.budget_balance)
        self.assertFalse(report.ir)

    def test_exhaustive_search_covers_frozen_space(self):
        accepted = exhaustive_search()
        self.assertGreater(len(accepted), 0)
        self.assertTrue(all(row["verification"].accepted for row in accepted))

    def test_evolutionary_loop_is_seeded_and_verifies_proposals(self):
        result = evolutionary_search(seed=67, population_size=8, generations=3)
        self.assertEqual(result["evaluated"], 24)
        self.assertGreaterEqual(result["accepted"], 0)


if __name__ == "__main__":
    unittest.main()
