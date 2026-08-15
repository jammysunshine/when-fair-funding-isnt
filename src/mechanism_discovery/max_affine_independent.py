"""Standalone replay for serialized shallow max-affine certificates.

This module deliberately imports neither ``piecewise_affine`` nor formula
transcriptions.  It interprets the certificate's rational expression payload,
derives its arrangement, and recomputes every reported extremum.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from typing import Any


def _fraction(value: str) -> Fraction:
    numerator, denominator = value.split("/")
    return Fraction(int(numerator), int(denominator))


def _forms(items: list[list[str]]) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(tuple(_fraction(value) for value in item) for item in items)


def _evaluate(form: tuple[Fraction, ...], point: tuple[Fraction, ...]) -> Fraction:
    return sum((weight * value for weight, value in zip(form[:-1], point)), form[-1])


def _expression_value(specification: dict[str, Any], point: tuple[Fraction, ...]) -> Fraction:
    total = sum((_evaluate(form, point) for form in _forms(specification["affine_terms"])), Fraction(0))
    total += sum((max(_evaluate(branch, point) for branch in branches)
                  for branches in (_forms(group) for group in specification["maxima"])), Fraction(0))
    return total + sum((min(_evaluate(branch, point) for branch in branches)
                        for branches in (_forms(group) for group in specification["minima"])), Fraction(0))


def _difference(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(a - b for a, b in zip(left, right))


def _planes(specification: dict[str, Any], dimension: int) -> tuple[tuple[Fraction, ...], ...]:
    planes = [[Fraction(1)] + [Fraction(0)] * (dimension - 1) + [Fraction(0)]]
    planes.append([Fraction(0)] * (dimension - 1) + [Fraction(1), Fraction(-1)])
    for index in range(dimension - 1):
        form = [Fraction(0)] * (dimension + 1)
        form[index], form[index + 1] = Fraction(1), Fraction(-1)
        planes.append(form)
    planes.append([Fraction(1)] * dimension + [Fraction(-1)])
    for key in ("maxima", "minima"):
        for group in specification[key]:
            forms = _forms(group)
            planes.extend(_difference(left, right) for left, right in combinations(forms, 2))
    return tuple(tuple(plane) for plane in planes)


def _solve(rows: tuple[tuple[Fraction, ...], ...]) -> tuple[Fraction, ...] | None:
    dimension = len(rows)
    table = [list(row[:-1]) + [-row[-1]] for row in rows]
    for column in range(dimension):
        pivot = next((row for row in range(column, dimension) if table[row][column] != 0), None)
        if pivot is None:
            return None
        table[column], table[pivot] = table[pivot], table[column]
        divisor = table[column][column]
        table[column] = [value / divisor for value in table[column]]
        for row in range(dimension):
            if row != column and table[row][column] != 0:
                multiplier = table[row][column]
                table[row] = [value - multiplier * pivot_value
                              for value, pivot_value in zip(table[row], table[column])]
    return tuple(row[-1] for row in table)


def replay_entry(entry: dict[str, Any]) -> dict[str, Any]:
    """Recompute a certificate entry from its serialized expression only."""
    dimension = int(entry["dimension"])
    specification = entry["specification"]
    planes = _planes(specification, dimension)
    vertices = set()
    bases_examined = 0
    for basis in combinations(planes, dimension):
        bases_examined += 1
        point = _solve(basis)
        if point is not None and all(Fraction(0) <= value <= Fraction(1) for value in point) and all(
            point[index] <= point[index + 1] for index in range(dimension - 1)
        ):
            vertices.add(point)
    ordered = tuple(sorted(vertices))
    rows = []
    for point in ordered:
        first_best = max(sum(point, Fraction(0)), Fraction(1))
        charge = _expression_value(specification, point)
        rows.append((charge / first_best, charge - Fraction(dimension - 1) * first_best, point))
    low, _, low_witness = min(rows)
    high, _, high_witness = max(rows)
    _, slack, slack_witness = min(rows, key=lambda row: (row[1], row[2]))
    return {
        "arrangement_planes": len(planes),
        "candidate_bases_examined": bases_examined,
        "vertices": [[f"{value.numerator}/{value.denominator}" for value in point] for point in ordered],
        "minimum_charge_ratio": f"{low.numerator}/{low.denominator}",
        "minimum_witness": [f"{value.numerator}/{value.denominator}" for value in low_witness],
        "maximum_charge_ratio": f"{high.numerator}/{high.denominator}",
        "maximum_witness": [f"{value.numerator}/{value.denominator}" for value in high_witness],
        "worst_case_efficiency": f"{(Fraction(dimension) - high).numerator}/{(Fraction(dimension) - high).denominator}",
        "minimum_budget_slack": f"{slack.numerator}/{slack.denominator}",
        "minimum_slack_witness": [f"{value.numerator}/{value.denominator}" for value in slack_witness],
    }


def replay_payload(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {name: replay_entry(entry) for name, entry in payload["entries"].items()}
