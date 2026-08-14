"""Typed transcriptions of fixed public-project formulas for Phase IV."""

from fractions import Fraction

from .piecewise_affine import Expr, affine


def _sum(*expressions: Expr) -> Expr:
    result = Expr()
    for expression in expressions:
        result = result + expression
    return result


def guo_2019_equation_two_charge() -> Expr:
    """Total charge of Guo (IJCAI 2019), Eq. (2), on ordered 3-agent reports."""
    a, b, c = affine(1, 0, 0), affine(0, 1, 0), affine(0, 0, 1)
    const = lambda value: affine(0, 0, 0, constant=value)

    def h(left, right):
        pair = tuple(x + y for x, y in zip(left, right))
        return _sum(Expr.maximum(pair, const(Fraction(2, 3))),
                    Expr.maximum(pair, const(1)).scale(Fraction(1, 2)),
                    Expr.maximum(left, right, const(Fraction(2, 3))).scale(Fraction(-1, 2)),
                    Expr.from_affine(const(Fraction(-1, 6))))
    return _sum(h(b, c), h(a, c), h(a, b))


def guo_2024_three_agent_charge() -> Expr:
    """Total charge of Guo (AAAI 2024)'s printed 3-agent formula."""
    a, b, c = affine(1, 0, 0), affine(0, 1, 0), affine(0, 0, 1)
    zero = affine(0, 0, 0)
    const = lambda value: affine(0, 0, 0, constant=value)

    def h(left, right):
        pair = tuple(x + y for x, y in zip(left, right))
        skew = tuple(5 * x + 3 * y for x, y in zip(left, right))
        return _sum(Expr.maximum(zero, tuple(x - y for x, y in zip(pair, const(1)))).scale(Fraction(2, 3)),
                    Expr.maximum(zero, tuple(x - y for x, y in zip(skew, const(2)))).scale(Fraction(1, 6)),
                    Expr.from_affine(const(Fraction(2, 3))))
    return _sum(h(b, c), h(a, c), h(a, b))
