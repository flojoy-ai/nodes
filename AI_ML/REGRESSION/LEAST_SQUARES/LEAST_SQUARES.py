import numpy as np
import traceback
from flojoy import flojoy, DataContainer


@flojoy
def LEAST_SQUARES(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The LEAST_SQUARE node computes the coefficients that minimizes the distance between the 
    inputs 'DataContainer' class, specifically the 'matrix' type and the regression.


    Parameters
    ----------
    dc_inputs (list[DataContainer]: List of DataContainer objects containing
            a coefficient matrix and dependent variable)
            params (dict): Additional parameters for least squares method (not used in this function)

    Returns
    -------
    ordered pair
        x: input matrix (data points)
        y: fitted line computed with returned regression weights
    """
    x : np.ndarray = np.eye(3)
    y : np.ndarray = np.eye(3)
    a : np.ndarray = np.eye(3)
    
    if (len(dc_inputs) < 0): 
            raise ValueError(
            f"To compute least squares, LEAST_SQUARES node requires two inputs, {len(dc_inputs)} was given!"
    )

    if (dc_inputs[0].type == "ordered_pair"):
        x = np.array(dc_inputs[0].y)
        y = np.array(dc_inputs[1].y)

        if x.shape[0] != y.shape[0]:
            print("matrix dimensions do not match.")

        else:
            try:
                a = np.vstack([x, np.ones(len(x))]).T
                res = np.linalg.lstsq(a, y, rcond=None)[0]
            except np.linalg.LinAlgError:
                raise ValueError("Least Square Computation failed.")

    elif (dc_inputs[0].typpe == "matrix"):
        x = np.array(dc_inputs[0].m)
        y = np.array(dc_inputs[1].m)

        if x.shape[0] != y.shape[0]:
            print("matrix dimensions do not match.")

        else:
            try:
                a = np.vstack([x, np.ones(len(x))]).T
                res = np.linalg.lstsq(a, y, rcond=None)[0]
            except np.linalg.LinAlgError:
                raise ValueError("Least Square Computation failed.")  
    else:
        raise ValueError(
            f"unsupported DataContainer type passed to LEAST_SQUARES node: '{dc_inputs[0].type}'"
        )

    return DataContainer(type="matrix", m=res)
