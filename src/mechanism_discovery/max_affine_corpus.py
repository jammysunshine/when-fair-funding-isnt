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


def guo_2024_four_agent_charge(charge_offset: Fraction = Fraction(0)) -> Expr:
    """Total charge of Guo (AAAI 2024)'s printed 4-agent decimal formula.

    The input is ordered.  Consequently, deleting any coordinate leaves the
    remaining coordinates ordered, so this is a direct typed transcription of
    the public formula rather than a reconstruction of unpublished weights.
    ``charge_offset`` is the per-term constant in the paper's repair family.
    """
    variables = tuple(affine(*(1 if index == coordinate else 0 for index in range(4)))
                      for coordinate in range(4))
    zero = affine(0, 0, 0, 0)

    def combine(weights, forms, bias=0):
        coefficients = tuple(sum((Fraction(weight) * form[index]
                                  for weight, form in zip(weights, forms)), Fraction(0))
                             for index in range(4))
        return coefficients + (sum((Fraction(weight) * form[-1]
                                    for weight, form in zip(weights, forms)), Fraction(bias)),)

    def h(first, second, third):
        forms = (first, second, third)
        relus = (
            ((-7220, -5927, -5925), Fraction(5926, 10000)),
            ((-4485, -5939, -3858), Fraction(3856, 10000)),
            ((1925, 4570, 4436), Fraction(-2218, 10000)),
            ((-4820, -3097, -915), Fraction(3667, 10000)),
        )
        base = combine((Fraction(9197, 10000), Fraction(6558, 10000), Fraction(6646, 10000)),
                       forms, Fraction(2218, 10000) + charge_offset)
        expression = Expr.from_affine(base)
        for index, (weights, bias) in enumerate(relus):
            expression = expression + Expr.maximum(zero, combine(
                tuple(Fraction(weight, 10000) for weight in weights), forms, bias
            )).scale(-1 if index == 3 else 1)
        return expression

    return _sum(*(h(*(variables[:index] + variables[index + 1:])) for index in range(4)))
