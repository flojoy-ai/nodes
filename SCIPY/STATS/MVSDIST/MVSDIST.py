from flojoy import DataContainer, flojoy
import scipy.stats


@flojoy
def MVSDIST(
    default: DataContainer,
):
    """

            'Frozen' distributions for mean, variance, and standard deviation of data.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    data : array_like
            Input array. Converted to 1-D using ravel.
            Requires 2 or more data-points.
    """
    return DataContainer(x=dc[0].y, y=scipy.stats.mvsdist(data=dc[0].y))
