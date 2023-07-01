from flojoy import DataContainer, flojoy, DefaultParams
import scipy.signal


@flojoy
def CUBIC(default: DataContainer, default_params: DefaultParams):
    """
            A cubic B-spline.

            This is a special case of `bspline`, and equivalent to ``bspline(x, 3)``.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    x : array_like
            a knot vector
    """
    return DataContainer(x=dc[0].y, y=scipy.signal.cubic(x=dc[0].y))
