from flojoy import OrderedPair, flojoy
import scipy.stats


@flojoy(node_type="default")
def SHAPIRO(
    default: OrderedPair,
) -> OrderedPair:
    """The SHAPIRO node is based on a numpy or scipy function.
    The description of that function is as follows:

            Perform the Shapiro-Wilk test for normality.

            The Shapiro-Wilk test tests the null hypothesis that the
            data was drawn from a normal distribution.

    Parameters
    ----------
    x : array_like
            Array of sample data.

    Returns
    ----------
    DataContainer:
            type 'ordered pair'"""
    result = OrderedPair(
        x=default.x,
        y=scipy.stats.shapiro(
            x=default.y,
        ),
    )
    return result
