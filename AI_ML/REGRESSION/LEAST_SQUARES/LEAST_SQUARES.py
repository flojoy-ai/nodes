import numpy as np
import traceback
from flojoy import flojoy, OrderedPair, Matrix


@flojoy
def LEAST_SQUARES(
    a: OrderedPair | Matrix, b: OrderedPair | Matrix
) -> OrderedPair | Matrix:
    """The LEAST_SQUARE node computes the coefficients that minimizes the distance between the
    inputs 'Matrix or OrderedPair' class and the regression.


    Parameters
    ----------
    None

    Returns
    -------
    ordered pair
        x: input matrix (data points)
        y: fitted line computed with returned regression weights
    """

    if b is None and a.type == "ordered_pair":
        if (len(a.y)) != 0:
            x = a.y
            y = a.y
        else:
            x = a.x
            y = a.y
        try:
            a = np.vstack([x, np.ones(len(x))]).T
            p = np.linalg.lstsq(a, y, rcond=None)[0]
        except np.linalg.LinAlgError:
            raise ValueError("Least Square Computation failed.")

        slope, intercept = p[0:-1], p[-1]
        res = slope * x + intercept

        return OrderedPair(x=x, y=res)

    if a.type == "ordered_pair" and b.type == "ordered_pair":
        x = a.y
        y = b.y

        try:
            a = np.vstack([x, np.ones(len(x))]).T
            p = np.linalg.lstsq(a, y, rcond=None)[0]
        except np.linalg.LinAlgError:
            raise ValueError("Least Square Computation failed.")

        slope, intercept = p[0:-1], p[-1]
        res = slope * x + intercept

        return OrderedPair(x=x, y=res)

    elif a.type == "matrix" and b.type == "matrix":
        x = a.m
        y = b.m

        try:
            a = np.vstack([x, np.ones(len(x))]).T
            p = np.linalg.lstsq(a, y, rcond=None)[0]
        except np.linalg.LinAlgError:
            raise ValueError("Least Square Computation failed.")

        slope, intercept = p[0:-1], p[-1]
        res = slope * x + intercept

        return Matrix(m=res)
