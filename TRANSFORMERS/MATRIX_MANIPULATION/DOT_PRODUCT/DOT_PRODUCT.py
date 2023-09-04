import numpy as np
from flojoy import flojoy, Vector, Matrix, Scalar
from typing import Union


@flojoy
def DOT_PRODUCT(a: Matrix | Vector, b: Matrix | Vector) -> Matrix | Vector | Scalar:
    """The DOT_PRODUCT node takes two input matrices, multiplies them
    (by dot product), and returns the result.

    When multiplying a scalar use the MULTIPLY node.

    Inputs
    ------
    a : Matrix
        The input matrix to be multiplied to input b.
    b : Matrix
        The input matrix to be multiplied to input a.

    Returns
    -------
    Matrix
        The matrix result from the matrix multiplication.
    """

    if isinstance(a, Vector) and isinstance(b, Vector):
        assert a.v.shape == b.v.shape, "Vector sizes must be equal."
        return Scalar(c=np.dot(a.v, b.v))
    elif isinstance(a, Matrix) and isinstance(b, Vector):
        print(a.m.shape[1], b.v.shape, flush=True)
        assert (
            a.m.shape[0] == b.v.shape[0]
        ), "Vector size must be equal to Matrix column size."
        return Vector(v=np.dot(a.m, b.v))
    elif isinstance(a, Vector) and isinstance(b, Matrix):
        assert (
            a.v.shape[0] == b.m.shape[0]
        ), "Vector size must be equal to Matrix column size."
        return Vector(v=np.dot(a.v, b.m))
    elif isinstance(a, Matrix) and isinstance(b, Matrix):
        assert a.m.shape == b.m.shape, "Matrix sizes must be equal."
        return Matrix(m=np.dot(a.m, b.m))
