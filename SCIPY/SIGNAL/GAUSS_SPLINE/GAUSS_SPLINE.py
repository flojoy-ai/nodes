from flojoy import DataContainer, flojoy
import scipy.signal


@flojoy
def GAUSS_SPLINE(default: DataContainer, n: int = None):
    """
            Gaussian approximation to B-spline basis function of order n.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    x : array_like
            a knot vector
    n : int
            The order of the spline. Must be non-negative, i.e., n >= 0
    """
    return DataContainer(
        x=dc[0].y,
        y=scipy.signal.gauss_spline(
            x=dc[0].y, n=int(params["n"]) if params["n"] != "" else None
        ),
    )
