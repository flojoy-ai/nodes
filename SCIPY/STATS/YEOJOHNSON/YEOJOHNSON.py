from flojoy import DataContainer, flojoy
import scipy.stats


@flojoy
def YEOJOHNSON(default: DataContainer, lmbda: float = None):
    """
            Return a dataset transformed by a Yeo-Johnson power transformation.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    x : ndarray
            Input array.  Should be 1-dimensional.
    lmbda : float, optional
            If ``lmbda`` is ``None``, find the lambda that maximizes the
            log-likelihood function and return it as the second output argument.
            Otherwise the transformation is done for the given value.
    """
    return DataContainer(
        x=dc[0].y,
        y=scipy.stats.yeojohnson(
            x=dc[0].y, lmbda=float(params["lmbda"]) if params["lmbda"] != "" else None
        ),
    )
