# Verification report

Primary verification is in `src/mechanism_discovery/public_project.py`; it checks every profile, unilateral report, payment, and anonymity permutation. `public_project_independent.py` reconstructs the table and critical payments without importing the primary verifier.

The study run enumerates 16 rules and writes the full witness-bearing JSON. The independent replay accepts all 4 serialized cost-3 rows (`independent_failure_count=0`, digest `16e4f8d6f38faf5691a407f1da9bf60af9242b9bdf113465a3a59e6d255143be`). The efficient comparator has budget witnesses including `(0,2,2)` with payments `(0,1,1)` at cost 3. Held-out value-magnitude checks cover all 64 profiles for each threshold 1–6 and report 207 failures.
