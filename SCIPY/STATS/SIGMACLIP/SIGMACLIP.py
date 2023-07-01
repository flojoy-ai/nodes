from flojoy import DataContainer, flojoy, DefaultParams
import scipy.stats


@flojoy
def SIGMACLIP(
    default: DataContainer,
    default_params: DefaultParams,
    low: float = 4.0,
    high: float = 4.0,
):
    """
            Perform iterative sigma-clipping of array elements.

            Starting from the full sample, all elements outside the critical range are
            removed, i.e. all elements of the input array `c` that satisfy either of
    the following conditions::

            c < mean(c) - std(c)*low
            c > mean(c) + std(c)*high

            The iteration continues with the updated sample until no
            elements are outside the (updated) range.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    a : array_like
            Data array, will be raveled if not 1-D.
    low : float, optional
            Lower bound factor of sigma clipping. Default is 4.
    high : float, optional
            Upper bound factor of sigma clipping. Default is 4.
    """
    return DataContainer(
        x=dc[0].y,
        y=scipy.stats.sigmaclip(
            a=dc[0].y,
            low=float(params["low"]) if params["low"] != "" else None,
            high=float(params["high"]) if params["high"] != "" else None,
        ),
    )
