from flojoy import flojoy, DataContainer
import numpy as np
from scipy import integrate
from sympy import parse_expr

@flojoy
def DOUBLE_INTEGRATE(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """
    The INTEGRATE node takes two lists as input and integrates it using the composite
    trapezoidal rule.

    Parameters
    ----------
    None

    Returns
    -------
    numpy array / float
        integrated value in sequence of y array.
    """
    func = params["function"]
    func = parse_expr(func)
    print("=======================================")
    print(func)
    print("=======================================")

    upper_bound_x = params["upper_bound_x"]
    lower_bound_x = params["lower_bound_x"]
    upper_bound_y = params["upper_bound_y"]
    lower_bound_y = params["lower_bound_y"]

    integrate = integrate.dblquad(func, lower_bound_x, upper_bound_x, lower_bound_y, upper_bound_y)
    print("=======================================")
    print(integrate)
    print("=======================================")

    return DataContainer(type="scalar", c=integrate)