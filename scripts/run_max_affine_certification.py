#!/usr/bin/env python3
"""Emit the Phase-IV generic-engine reproduction certificate."""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.mechanism_discovery.max_affine_corpus import (
    guo_2019_equation_two_charge,
    guo_2024_three_agent_charge,
    guo_2024_four_agent_charge,
)
from src.mechanism_discovery.piecewise_affine import certify_ordered_public_project_charge


def encode(value):
    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, tuple):
        return [encode(item) for item in value]
    if hasattr(value, "__dict__"):
        return {key: encode(item) for key, item in value.__dict__.items()}
    return value


def main():
    payload = {
        "scope": "exact shallow max-affine certificates on ordered continuous public-project unit cubes",
        "method_limit": "not a general neural-network verifier; completeness follows only for the declared shallow max-affine representation",
        "entries": {
            "guo_ijcai_2019_equation_2": encode(certify_ordered_public_project_charge(guo_2019_equation_two_charge(), 3)),
            "guo_aaai_2024_printed_3_agent": encode(certify_ordered_public_project_charge(guo_2024_three_agent_charge(), 3)),
            "guo_aaai_2024_printed_4_agent": encode(certify_ordered_public_project_charge(guo_2024_four_agent_charge(), 4)),
            "guo_aaai_2024_printed_4_agent_uniform_repair": encode(certify_ordered_public_project_charge(guo_2024_four_agent_charge(Fraction(1, 20000)), 4)),
        },
    }
    serialized = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    output = ROOT / "artifacts" / "max_affine_certification.json"
    output.write_text(serialized)
    print(output)
    print(hashlib.sha256(serialized.encode()).hexdigest())


if __name__ == "__main__":
    main()
