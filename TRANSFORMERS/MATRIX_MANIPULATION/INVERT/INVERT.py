import numpy as np
from typing import Union
from flojoy import flojoy, OrderedPair, Matrix


@flojoy
def INVERT(default: Union[OrderedPair, Matrix], rcond: float = 1.0) -> Union[OrderedPair, Matrix]:
    """Takes 2 inputs, one matrix and one rcond if not square matrix.
    Inverts them (or pseudo invert) and returns the result.
    If the entered value is a scalar it returns the multiplciative
    inverse 1/x"""
    print(f"INVERT params: {params}")
    a = np.eye(3)
    b: float = rcond

    if (
            default.type == "ordered_pair"
        ):  # v[0] is a DataContainer object with type attribute
            print("Performing simple inversion")
            a = default.y  # scalar valued
            return OrderedPair(x=a, y=1 / a)
    elif default.type == "matrix":
            a = default.m
            if not a.shape[0] == a.shape[1]:
                print("Not square matrix! Using pseudoinversion...")
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
    else:
            raise ValueError("Incorrect input type.")
