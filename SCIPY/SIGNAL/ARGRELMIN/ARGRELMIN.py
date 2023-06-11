from flojoy import DataContainer, flojoy
import scipy.signal


@flojoy
def ARGRELMIN(dc, params):
    """

            Calculate the relative minima of `data`.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    data : ndarray
            Array in which to find the relative minima.
    axis : int, optional
            Axis over which to select from `data`. Default is 0.
    order : int, optional
            How many points on each side to use for the comparison
            to consider ``comparator(n, n+x)`` to be True.
    mode : str, optional
            How the edges of the vector are treated.
            Available options are 'wrap' (wrap around) or 'clip' (treat overflow
            as the same as the last (or first) element).
            Default 'clip'. See numpy.take.
    """
    return DataContainer(
        x=dc[0].y,
        y=scipy.signal.argrelmin(
            data=dc[0].y,
            axis=(int(params["axis"]) if params["axis"] != "" else None),
            order=(int(params["order"]) if params["order"] != "" else None),
            mode=(str(params["mode"]) if params["mode"] != "" else None),
        ),
    )
