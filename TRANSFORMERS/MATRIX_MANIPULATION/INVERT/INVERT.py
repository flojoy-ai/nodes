import numpy as np
from flojoy import flojoy, OrderedPair, Matrix


@flojoy
def INVERT(default: OrderedPair | Matrix, rcond: float = 1.0) -> OrderedPair | Matrix:
    """
    The INVERT node takes two inputs, one matrix and one rcond if not a square matrix, then inverts them (or pseudo invert) and returns the result.

    If the entered value is a scalar, it returns the multiplciative inverse 1/x.
    """

    a = np.eye(3)
    b: float = rcond

    if isinstance(
        default, OrderedPair
    ):  # v[0] is a DataContainer object with type attribute
        a = default.y  # scalar valued
        return OrderedPair(x=a, y=1 / a)
    elif isinstance(default, Matrix):
        a = default.m
        if not a.shape[0] == a.shape[1]:
            assert (
                type(b) == float
            ), "Need scalar value to compare SVDs for pseudoinversion"
            retval = np.linalg.pinv(a, rcond=b, hermitian=False)
        else:
            try:
                retval = np.linalg.inv(a)
            except np.linalg.LinAlgError:
                raise ValueError("Inversion failed! Singular matrix returned...")
        return Matrix(m=retval)
