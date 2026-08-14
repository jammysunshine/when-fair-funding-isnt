# Mechanism Specification

`Mechanism` in `src/mechanism_discovery/model.py` is a total four-row truth table ordered `(0,0),(0,1),(1,0),(1,1)`. A row is `Outcome(choice, (p0,p1))`. `value(t,c)=1` exactly when `t=c`; `utility(t,o,i)=value(t,o.choice)-o.payments[i]`.

The primary checker exhaustively evaluates both agents, all four truthful profiles, and their only nontruthful report. It reports a witness containing profile, agent, deviation, and utility change for DSIC failures. It separately emits feasibility, budget-balance, IR, and anonymity witnesses. `independent_verifier.py` independently loops by an agent's type and other report, and is used as a checker cross-check for the baseline.

The baseline `priority_majority_agent_0` chooses report 0 on every profile and has payments `(0,0)`. Therefore agent 0 always gets their reported preferred option and agent 1 cannot change the selected option; truthful reporting is weakly dominant. It has no transfers, so it is ex-post IR and exactly budget balanced.
