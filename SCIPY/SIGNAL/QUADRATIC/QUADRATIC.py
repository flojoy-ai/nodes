from flojoy import DataContainer, flojoy
import scipy.signal


@flojoy
def QUADRATIC(
    default: DataContainer,
):
    """
            A quadratic B-spline.

            This is a special case of `bspline`, and equivalent to ``bspline(x, 2)``.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    x : array_like
            a knot vector
    """
    return DataContainer(x=dc[0].y, y=scipy.signal.quadratic(x=dc[0].y))
