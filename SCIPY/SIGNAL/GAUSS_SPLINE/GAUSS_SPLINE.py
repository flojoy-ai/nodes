from flojoy import OrderedPair, flojoy
import scipy.signal


@flojoy(node_type="default")
def GAUSS_SPLINE(
    default: OrderedPair,
    n: int,
) -> OrderedPair:
    """The GAUSS_SPLINE node is based on a numpy or scipy function.
    The description of that function is as follows:

            Gaussian approximation to B-spline basis function of order n.

    Parameters
    ----------
    x : array_like
            a knot vector
    n : int
            The order of the spline. Must be non-negative, i.e., n >= 0

    Returns
    ----------
    DataContainer:
            type 'ordered pair'"""
    result = OrderedPair(
        x=default.x,
        y=scipy.signal.gauss_spline(
            x=default.y,
            n=n,
        ),
    )
    return result
