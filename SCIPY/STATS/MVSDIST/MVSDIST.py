from flojoy import OrderedPair, flojoy
import scipy.stats


@flojoy(node_type="default")
def MVSDIST(
    default: OrderedPair,
) -> OrderedPair:
    """The MVSDIST node is based on a numpy or scipy function.
    The description of that function is as follows:


            'Frozen' distributions for mean, variance, and standard deviation of data.

    Parameters
    ----------
    data : array_like
            Input array. Converted to 1-D using ravel.
            Requires 2 or more data-points.

    Returns
    ----------
    DataContainer:
            type 'ordered pair'"""
    result = OrderedPair(
        x=default.x,
        y=scipy.stats.mvsdist(
            data=default.y,
        ),
    )
    return result
