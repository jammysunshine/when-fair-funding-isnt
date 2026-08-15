# Verification report

Primary verification is in `src/mechanism_discovery/public_project.py`; it
checks every profile, unilateral report, payment, and anonymity permutation.
`public_project_independent.py` reconstructs the table and critical payments
without importing the primary verifier.

The preregistered run enumerates 16 rules; the exploratory extension enumerates
32 and 64 rules for four and five agents. The standalone replay accepts all 74
serialized rows (`cross_n_failure_count=0`, cross-agent digest
`a04706cd4d754debd5847529e3b3ebe22a14de45efa9b94db8edfd91823a9cc8`); the
original four cost-3 rows retain digest
`16e4f8d6f38faf5691a407f1da9bf60af9242b9bdf113465a3a59e6d255143be`.
The efficient comparator has a budget witness at `(0,2,2)` with payments
`(0,1,1)` and cost 3. Held-out checks cover all 64 profiles for each threshold
1–6 and report 207 failures.

For the frozen rational-ReLU benchmark, source-direct and compiler-lowered
certificate extrema match on all six cases. The independent Z3 verifier checks
three strict counterexample predicates for each source (budget slack below its
certificate, ratio below its minimum, and ratio above its maximum); all 18 are
`unsat`. It also evaluates each serialized rational extremum witness directly.
The resulting artifact is `artifacts/relu_benchmark_z3_certificate.json`.
