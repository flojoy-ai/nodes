import numpy as np
from flojoy import flojoy, OrderedPair, Scalar, Vector
from functools import reduce


@flojoy
def DIVIDE(
    a: OrderedPair | Scalar | Vector, b: list[OrderedPair | Scalar | Vector]
) -> OrderedPair | Scalar | Vector:
    """Divide 2 or more numeric arrays, matrices, dataframes, or constants element-wise.
    When a constant is divideed to an array or matrix, each element in the array or
    matrix will be increased by the constant value.
    """
    if isinstance(a, Scalar) and all(isinstance(item, OrderedPair) for item in b):
        raise ValueError("The 'scalar' type should be connect to the 'y' input.")

    if isinstance(a, Vector) and all(isinstance(item, OrderedPair) for item in b):
        raise ValueError("The 'Vector' type should be connect to the 'y' input.")

    elif isinstance(a, OrderedPair) and all(
        isinstance(item, OrderedPair) for item in b
    ):
        x = a.x
        y = reduce(lambda u, v: np.divide(u, v.y), b, a.y)
        return OrderedPair(x=x, y=y)

    elif isinstance(a, OrderedPair) and all(isinstance(item, Vector) for item in b):
        x = a.x
        y = reduce(lambda u, v: np.divide(u, v.v), b, a.y)
        return OrderedPair(x=x, y=y)

    elif isinstance(a, OrderedPair) and all(isinstance(item, Scalar) for item in b):
        x = a.x
        y = reduce(lambda u, v: np.divide(u, v.c), b, a.y)
        return OrderedPair(x=x, y=y)

    elif (isinstance(a, Scalar) and all(isinstance(item, Vector)) for item in b):
        c = reduce(lambda u, v: np.divide(u, v.v), b, a.c)
        return Scalar(c=c)

    elif isinstance(a, Scalar) and all(isinstance(item, Scalar) for item in b):
        c = reduce(lambda u, v: np.divide(u, v.c), b, a.c)
        return Scalar(c=c)

    elif isinstance(a, Vector) and all(isinstance(item, Scalar) for item in b):
        v = reduce(lambda u, v: np.divide(u, v.c), b, a.v)
        return Vector(v=v)

    elif isinstance(a, Vector) and all(isinstance(item, Vector) for item in b):
        v = reduce(lambda u, v: np.divide(u, v.v), b, a.v)
        return OrderedPair(v=v)
