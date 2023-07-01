from flojoy import flojoy, DataContainer, DefaultParams
from scipy import integrate
from sympy import parse_expr, lambdify


@flojoy
def DOUBLE_DEFINITE_INTEGRAL(
    default: DataContainer,
    default_params: DefaultParams,
    function: str = "",
    upper_bound_x: float = 0.0,
    lower_bound_x: float = 0.0,
    upper_bound_y: float = 0.0,
    lower_bound_y: float = 0.0,
) -> DataContainer:
    """
    The DEFINITE_INTEGRAL node takes a function, upper, and lower bounds as input.
    It computes double integral of the given function.

    Parameters
    ----------
    function : str
        function that we are integrating
    upper_bound_x : float
        upper bound for x
    lower_bound_x : float
        lower bound for x
    upper_bound_y : float
        upper bound for y
    lower_bound_y : float
        lower bound for y

    Returns
    -------
    DataContainer:
        type 'scalar', c
    """
    func = params["function"]
    func = parse_expr(func)
    symbols = tuple(func.free_symbols)
    f = lambdify(symbols, func)
    result = integrate.nquad(
        f, [(lower_bound_x, upper_bound_x), (lower_bound_y, upper_bound_y)]
    )[0]
    return DataContainer(type="scalar", c=result)
