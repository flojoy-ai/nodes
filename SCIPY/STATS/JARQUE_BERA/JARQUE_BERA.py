from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import scipy.stats


@flojoy(node_type="default")
def JARQUE_BERA(
    default: OrderedPair | Matrix,
    select_return: Literal["jb_value", "p"] = "jb_value",
) -> OrderedPair | Matrix | Scalar:
    """The JARQUE_BERA node is based on a numpy or scipy function.
    The description of that function is as follows:

            Perform the Jarque-Bera goodness of fit test on sample data.

            The Jarque-Bera test tests whether the sample data has the skewness and
            kurtosis matching a normal distribution.

            Note that this test only works for a large enough number of data samples
            (>2000) as the test statistic asymptotically has a Chi-squared distribution
            with 2 degrees of freedom.

    Parameters
    ----------
    select_return : This function has returns multiple Objects:
            ['jb_value', 'p']. Select the desired one to return.
            See the respective function docs for descriptors.
    x : array_like
            Observations of a random variable.

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = OrderedPair(
        m=scipy.stats.jarque_bera(
            x=default.y,
        )
    )

    return result
