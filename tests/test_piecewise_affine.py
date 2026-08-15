from fractions import Fraction
from copy import deepcopy
import json
from pathlib import Path
import unittest

from src.mechanism_discovery.guo_2019_three_agent_optimal import audit as equation_two_audit
from src.mechanism_discovery.max_affine_corpus import (
    guo_2019_equation_two_charge,
    guo_2024_three_agent_charge,
    guo_2024_four_agent_charge,
)
from src.mechanism_discovery.piecewise_affine import certify_ordered_public_project_charge
from src.mechanism_discovery.max_affine_independent import replay_payload
from src.mechanism_discovery.published_rule_audit import audit_printed_four_agent_rule, audit_printed_rule


class PiecewiseAffineCertificateTest(unittest.TestCase):
    def test_reproduces_known_three_agent_optimum(self):
        generic = certify_ordered_public_project_charge(guo_2019_equation_two_charge(), 3)
        known = equation_two_audit()
        self.assertEqual(len(generic.vertices), known.vertices_examined)
        self.assertEqual(generic.minimum_charge_ratio, known.minimum_charge_ratio)
        self.assertEqual(generic.maximum_charge_ratio, known.maximum_charge_ratio)
        self.assertEqual(generic.worst_case_efficiency, known.worst_case_efficiency)

    def test_reproduces_printed_aaai_rule(self):
        generic = certify_ordered_public_project_charge(guo_2024_three_agent_charge(), 3)
        known = audit_printed_rule()
        self.assertEqual(len(generic.vertices), known.vertices_examined)
        self.assertEqual(generic.minimum_charge_ratio, known.minimum_charge_ratio)
        self.assertEqual(generic.maximum_charge_ratio, known.maximum_charge_ratio)
        self.assertEqual(generic.worst_case_efficiency, known.worst_case_efficiency)

    def test_reproduces_four_agent_decimal_rule_and_repair(self):
        for offset in (Fraction(0), Fraction(1, 20000)):
            generic = certify_ordered_public_project_charge(guo_2024_four_agent_charge(offset), 4)
            known = audit_printed_four_agent_rule(offset)
            self.assertEqual(len(generic.vertices), known.vertices_examined)
            self.assertEqual(generic.minimum_charge_ratio, known.minimum_charge_ratio)
            self.assertEqual(generic.minimum_budget_slack, known.minimum_deficit)
            self.assertEqual(generic.maximum_charge_ratio, known.maximum_charge_ratio)
            self.assertEqual(generic.worst_case_efficiency, known.worst_case_efficiency)

    def test_certificate_reports_exact_arrangement_work(self):
        certificate = certify_ordered_public_project_charge(guo_2024_four_agent_charge(), 4)
        self.assertGreater(certificate.arrangement_planes, 4)
        self.assertGreater(certificate.candidate_bases_examined, len(certificate.vertices))

    def test_serialized_certificate_replays_without_primary_engine(self):
        root = Path(__file__).resolve().parents[1]
        payload = json.loads((root / "artifacts" / "max_affine_certification.json").read_text())
        expected = {name: entry["certificate"] for name, entry in payload["entries"].items()}
        self.assertEqual(replay_payload(payload), expected)

    def test_independent_replay_detects_tampered_result(self):
        root = Path(__file__).resolve().parents[1]
        payload = json.loads((root / "artifacts" / "max_affine_certification.json").read_text())
        corrupted = deepcopy(payload)
        corrupted["entries"]["guo_aaai_2024_printed_4_agent"]["certificate"]["minimum_budget_slack"] = "0/1"
        expected = {name: entry["certificate"] for name, entry in corrupted["entries"].items()}
        self.assertNotEqual(replay_payload(corrupted), expected)

    def test_independent_replay_detects_tampered_formula(self):
        root = Path(__file__).resolve().parents[1]
        payload = json.loads((root / "artifacts" / "max_affine_certification.json").read_text())
        corrupted = deepcopy(payload)
        specification = corrupted["entries"]["guo_aaai_2024_printed_4_agent"]["specification"]
        specification["affine_terms"][0][-1] = "0/1"
        expected = {name: entry["certificate"] for name, entry in corrupted["entries"].items()}
        self.assertNotEqual(replay_payload(corrupted), expected)


if __name__ == "__main__":
    unittest.main()
