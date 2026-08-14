"""Finite, deterministic binary social-choice mechanisms with transfers."""

from dataclasses import dataclass
from itertools import product
from typing import Iterable

Type = int
Profile = tuple[int, int]
PAYMENT_GRID = (-1, 0, 1)  # positive means paid to the mechanism
PROFILES: tuple[Profile, ...] = tuple(product((0, 1), repeat=2))


@dataclass(frozen=True)
class Outcome:
    choice: int
    payments: tuple[int, int]


@dataclass(frozen=True)
class Mechanism:
    """A total direct-revelation rule, represented by its four profile outcomes."""

    outcomes: tuple[Outcome, Outcome, Outcome, Outcome]
    name: str = "unnamed"

    def outcome(self, reports: Profile) -> Outcome:
        return self.outcomes[PROFILES.index(reports)]


def value(true_type: Type, choice: int) -> int:
    """Unit value for the agent's preferred binary alternative, zero otherwise."""
    return int(true_type == choice)


def utility(true_type: Type, outcome: Outcome, agent: int) -> int:
    return value(true_type, outcome.choice) - outcome.payments[agent]


def priority_majority() -> Mechanism:
    """Choose agent 0's report on disagreement; use zero transfers."""
    return Mechanism(
        tuple(Outcome(choice=profile[0], payments=(0, 0)) for profile in PROFILES),
        name="priority_majority_agent_0",
    )


def constant(choice: int) -> Mechanism:
    return Mechanism(tuple(Outcome(choice, (0, 0)) for _ in PROFILES), name=f"constant_{choice}")


def valid_outcomes() -> Iterable[Outcome]:
    for choice in (0, 1):
        for payments in product(PAYMENT_GRID, repeat=2):
            if sum(payments) == 0:
                yield Outcome(choice, payments)
