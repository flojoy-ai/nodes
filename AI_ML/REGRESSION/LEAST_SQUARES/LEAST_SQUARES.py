import numpy as np
import traceback
from flojoy import flojoy, DataContainer


@flojoy
def LEAST_SQUARES(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The LEAST_SQUARE node computes the coefficients that minimizes the distance between the
    inputs 'DataContainer' class, specifically the 'matrix' type and the regression.


    Parameters
    ----------
    None

    Returns
    -------
    ordered pair
        x: input matrix (data points)
        y: fitted line computed with returned regression weights
    """

    x: np.ndarray = np.eye(3)
    y: np.ndarray = np.eye(3)
    a: np.ndarray = np.eye(3)

    if len(dc_inputs) == 0 or len(dc_inputs) > 2:
        raise ValueError(
            f"To compute least squares, LEAST_SQUARES node requires one or two inputs, {len(dc_inputs)} was given!"
        )
    
    if (len(dc_inputs) == 1 and dc_inputs[0].type == "ordered_pair"):
        x = np.array(dc_inputs[0].y)
        y = np.array(dc_inputs[1].y)

        try:
            a = np.vstack([x, np.ones(len(x))]).T
            p = np.linalg.lstsq(a, y, rcond=None)[0]
        except np.linalg.LinAlgError:
            raise ValueError("Least Square Computation failed.")

        slope,intercept = p[0:-1], p[-1]
        res = slope * x + intercept
        # res = np.ndarray.flatten(res)

        # line types only accept 1D array
        return DataContainer(type="ordered_pair", x=x, y=res)
        

    if dc_inputs[0].type == "ordered_pair" and dc_inputs[1].type == "ordered_pair":
        x = np.array(dc_inputs[0].y)
        y = np.array(dc_inputs[1].y)

        try:
            a = np.vstack([x, np.ones(len(x))]).T
            p = np.linalg.lstsq(a, y, rcond=None)[0]
        except np.linalg.LinAlgError:
            raise ValueError("Least Square Computation failed.")

        slope,intercept = p[0:-1], p[-1]
        res = slope * x + intercept
        # res = np.ndarray.flatten(res)

        # line types only accept 1D array
        return DataContainer(type="ordered_pair", x=x, y=res)

    elif dc_inputs[0].type == "matrix" and dc_inputs[1].type == "matrix":
        x = np.array(dc_inputs[0].m)
        y = np.array(dc_inputs[1].m)

        try:
            a = np.vstack([x, np.ones(len(x))]).T
            p = np.linalg.lstsq(a, y, rcond=None)[0]
        except np.linalg.LinAlgError:
            raise ValueError("Least Square Computation failed.")

        slope,intercept = p[0:-1], p[-1]
        res = slope * x + intercept
        # res = np.ndarray.flatten(res)

        # line types only accept 1D array
        # res = np.array(p, dtype=float) * np.array(x, dtype=float)
        return DataContainer(type="matrix", m=res)

    else:
        raise ValueError(
            f"unsupported DataContainer type passed to LEAST_SQUARES node: '{dc_inputs[0].type}'"
        )

