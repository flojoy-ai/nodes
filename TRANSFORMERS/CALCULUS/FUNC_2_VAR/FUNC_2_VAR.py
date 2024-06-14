from flojoy import flojoy, OrderedPair, OrderedTriple
from sympy import parse_expr, lambdify


@flojoy
def FUNC_2_VAR(points: OrderedPair, function: str) -> OrderedTriple:
    func = parse_expr(function)
    symbols = tuple(func.free_symbols)

    f = lambdify(symbols, func)

    x = points.x
    z = points.y
    y = f(x, z)

    return OrderedTriple(x=x, y=y, z=z)
