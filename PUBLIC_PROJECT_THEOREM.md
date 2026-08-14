# Exact all-agent characterization

This is a theorem about the declared finite model, not a claim about arbitrary
public-project mechanisms.

**Model.** There are `n >= 1` agents, values in `{0,1,2}`, a binary project,
integer cost `c >= 1`, deterministic anonymous coordinatewise-monotone
allocation, and normalized discrete critical payments. An accepted rule must
build at `(2,...,2)`, satisfy DSIC, ex-post IR, feasibility, no subsidy when
the project is absent, and weak budget balance whenever it builds.

**Theorem.** For `1 <= c <= 2n`, the accepted allocation rules are exactly

```text
q_k(v) = 1  iff  every v_i >= 1 and at least k coordinates equal 2,
```

for `k = 0, ..., n` when `c <= n`, and only `k=n` when `n < c <= 2n`.
Consequently, the exact count is `n+1` for
`c <= n`, one for `n < c <= 2n`, and zero for `c > 2n` under the requirement
that the all-two profile builds.

## Proof

Let `h=(2,...,2)` and let

```text
t = min {x in {0,1,2}: q(x,2,...,2)=1}.
```

Anonymity makes every agent's critical payment at `h` equal to `t`. Since the
rule must build at `h`, `t` exists. Budget balance at `h` gives `n t >= c`, so
`t != 0` and `t` is either 1 or 2.

If `c > n`, the inequality forces `t=2`. Thus both
`q(0,2,...,2)=0` and `q(1,2,...,2)=0`. Every non-maximal state containing a
zero is coordinatewise below the first state, and every state with no zero is
coordinatewise below the second state. Monotonicity therefore leaves only
`h` active, which is `q_n`.

If `c <= n`, `q(0,2,...,2)=0`, so no active profile contains a zero. The
positive sorted states are the chain

```text
s_k = (1,...,1,2,...,2),  k=0,...,n.
```

An anonymous monotone rule on a chain is a suffix, so it is exactly one
`q_k`. Every active profile of `q_k` has all coordinates at least 1; hence
every critical payment is at least 1 and total revenue is at least `n >= c`.
The normalized critical-payment lemma supplies DSIC and ex-post IR, and the
other predicates hold by construction. Thus every `q_k` is accepted.

The two cases exhaust the possibilities, proving the characterization.

## Evidence boundary

`src/mechanism_discovery/public_project_theorem.py` constructs the predicted
rules without using the antichain enumerator. `scripts/verify_scaling_theorem.py`
checks the construction for agent counts 1–12 and independently replays it;
it also cross-checks the exhaustive n=3–6 artifacts. The symbolic argument is
the proof of the all-`n` claim; the script is a regression certificate, not a
formal proof assistant.

The result does **not** cover values above 2, continuous types, randomized or
subsidized rules, asymmetric mechanisms, arbitrary transfers, collusion, or a
Bayesian objective. It characterizes a narrow finite model and should be
presented as such.
