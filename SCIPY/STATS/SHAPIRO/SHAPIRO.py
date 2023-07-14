from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np


import scipy.stats


@flojoy(node_type="default")
def SHAPIRO(
    default: OrderedPair | Matrix,
) -> OrderedPair | Matrix | Scalar:
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
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = OrderedPair(
        m=scipy.stats.shapiro(
            x=default.y,
        )
    )

    return result
