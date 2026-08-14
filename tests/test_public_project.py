import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from mechanism_discovery.public_project import (  # noqa: E402
    PublicProjectSpec,
    enumerate_anonymous_monotone,
    frontier,
    sum_threshold_mechanism,
    verify_public_project,
)
from mechanism_discovery.public_project_independent import check  # noqa: E402


class PublicProjectTests(unittest.TestCase):
    def test_exhaustive_monotone_count_is_finite_and_reproducible(self):
        spec = PublicProjectSpec(3, 2, 3)
        self.assertEqual(len(list(enumerate_anonymous_monotone(spec))), 16)
        self.assertEqual(len(frontier(spec)), 4)

    def test_efficient_rule_has_a_budget_counterexample(self):
        spec = PublicProjectSpec(3, 2, 3)
        report = verify_public_project(sum_threshold_mechanism(spec, 3))
        self.assertTrue(report["dsic"])
        self.assertTrue(report["ex_post_ir"])
        self.assertFalse(report["weak_budget_balance"])
        self.assertTrue(any(w["property"] == "weak_budget_balance" for w in report["witnesses"]))

    def test_serialized_accepted_rule_passes_independent_checker(self):
        row = frontier(PublicProjectSpec(3, 2, 3))[0]["mechanism"]
        serialized = {
            "name": row.name,
            "n_agents": row.spec.n_agents,
            "max_value": row.spec.max_value,
            "cost": row.spec.cost,
            "allocation_by_state": [[list(s), q] for s, q in row.allocation_by_state],
        }
        self.assertTrue(check(serialized)["accepted"])

    def test_sum_threshold_is_dsic_under_heldout_values(self):
        spec = PublicProjectSpec(3, 2, 3)
        report = verify_public_project(sum_threshold_mechanism(spec, 4))
        self.assertTrue(report["dsic"])
        self.assertTrue(report["ex_post_ir"])


if __name__ == "__main__":
    unittest.main()
