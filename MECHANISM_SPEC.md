# Mechanism Specification

`src/mechanism_discovery/model.py` defines a total deterministic direct mechanism with four outcomes ordered `(0,0),(0,1),(1,0),(1,1)`. Each outcome is `(choice, (payment_0,payment_1))`; choices and types are in `{0,1}` and payments are in `{-1,0,1}`.

`value(t,c)=1` iff `t=c`; `utility(t,outcome,i)=value-payment_i`. Feasibility is binary choice. Exact budget balance is `payment_0+payment_1=0` pointwise. DSIC compares truthful utility with the only alternative report for each agent at every true profile. IR is truthful utility `>=0`.

Fairness is frozen as exact anonymity plus maximum truthful utility disparity `<=1`. The bounded coalition predicate checks every true profile against every alternative joint report and rejects only strict Pareto improvements for both fixed agents. Neutrality complements both types and requires the choice to complement; it is reported for the finite impossibility audit, not accepted.

`verifier.py` emits typed witnesses for every failed predicate. `independent_verifier.py` reconstructs the row-table checks and enumeration without importing the primary verifier. `search.py` exhaustively enumerates all `6^4` tables and runs a seeded zero-transfer evolutionary proposal loop.
