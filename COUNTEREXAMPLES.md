# Counterexamples

`tests/test_model_and_verifier.py::test_dsic_counterexample_contains_profitable_deviation` uses the rule that chooses `1-report_0` at every profile with zero payments. The primary verifier rejects it and emits a DSIC witness with truthful profile, deviator, report, and a positive utility change. `test_budget_balance_and_ir_witnesses` similarly exercises non-zero-sum, IR-violating payments. These are machine-executed regression fixtures, not general impossibility results.
