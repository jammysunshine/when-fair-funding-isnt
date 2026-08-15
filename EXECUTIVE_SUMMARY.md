# Executive summary

Experiment 67 is a certificate-first study of deterministic public-project
mechanisms. In the declared ternary anonymous monotone class, a human-checkable
argument gives the exact frontier for every agent count: `n+1` accepted rules
for costs through `n`, one rule through `2n`, and none above `2n`. Exhaustive
searches for three through six agents independently cross-check the result.

The accepted-count sequences are `4,4,4,1,1,1` (`n=3`),
`5,5,5,5,1,1,1,1` (`n=4`), and `6,6,6,6,6,1,1,1,1,1` (`n=5`). All 74
serialized accepted rows pass an independent checker. The efficient threshold
rule fails cost coverage at `(0,2,2)`, and a held-out value-3 audit records 207
failures. The defensible contribution is a narrow exact characterization plus
a reproducible finite frontier and falsification benchmark. It is not a
universal mechanism-design result, deployment evidence, or guarantee of
publication or a prize.

The later exact repair audit makes the limitation sharper: a scalar offset can
remove certified budget deficits, but it lowers every truthful Groves utility
by that offset. On the unchanged seven-source corpus, none of the repaired
rules is ex-post IR; compiler, direct-source, and exact-real Z3 checks agree.
