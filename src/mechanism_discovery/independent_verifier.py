"""Independent checker intentionally does not reuse primary verifier logic."""

from .model import PROFILES, Mechanism, utility


def check(mechanism: Mechanism) -> dict:
    failures: list[dict] = []
    for own_truth in (0, 1):
        for other_report in (0, 1):
            for agent in (0, 1):
                honest_profile = (own_truth, other_report) if agent == 0 else (other_report, own_truth)
                lie = 1 - own_truth
                lie_profile = (lie, other_report) if agent == 0 else (other_report, lie)
                if utility(own_truth, mechanism.outcome(lie_profile), agent) > utility(own_truth, mechanism.outcome(honest_profile), agent):
                    failures.append({"property": "dsic", "profile": honest_profile, "agent": agent, "deviation": lie})
    for profile in PROFILES:
        outcome = mechanism.outcome(profile)
        if outcome.choice not in (0, 1): failures.append({"property": "feasibility", "profile": profile})
        if sum(outcome.payments) != 0: failures.append({"property": "budget_balance", "profile": profile})
        for agent in (0, 1):
            if utility(profile[agent], outcome, agent) < 0:
                failures.append({"property": "individual_rationality", "profile": profile, "agent": agent})
    return {"accepted": not failures, "failures": failures}
