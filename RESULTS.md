# Results

The frozen search checked all `1,296` tables and accepted exactly `4`: constant-0, constant-1, AND, and OR (fixed-tie majority is equivalent to AND/OR on this domain). Both checker implementations return the same set. The accepted frontier has uniform allocative welfare `1.0` for constants and `1.5` for AND/OR; `anonymous_or` is the frozen baseline.

The certificate finds no accepted table with strictly higher uniform welfare than the baseline. The seeded evolutionary probe evaluated `2,560` proposals and accepted `661`; its best vector was `[0,0,0,1]`, an accepted frontier table. This is rediscovery evidence only, not coverage evidence.
