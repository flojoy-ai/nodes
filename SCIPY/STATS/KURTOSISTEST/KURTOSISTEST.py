from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import scipy.stats


@flojoy(node_type="default")
def KURTOSISTEST(
    default: OrderedPair | Matrix,
    axis: int = 0,
    nan_policy: str = "propagate",
    alternative: str = "two-sided",
    select_return: Literal["statistic", "pvalue"] = "statistic",
) -> OrderedPair | Matrix | Scalar:
    """The KURTOSISTEST node is based on a numpy or scipy function.
    The description of that function is as follows:

            Test whether a dataset has normal kurtosis.

            This function tests the null hypothesis that the kurtosis
            of the population from which the sample was drawn is that
            of the normal distribution.

    Parameters
    ----------
    select_return : This function has returns multiple Objects:
            ['statistic', 'pvalue']. Select the desired one to return.
            See the respective function docs for descriptors.
    a : array
            Array of the sample data.
    axis : int or None, optional
            Axis along which to compute test. Default is 0. If None,
            compute over the whole array `a`.
    nan_policy : {'propagate', 'raise', 'omit'}, optional
            Defines how to handle when input contains nan.
    The following options are available (default is 'propagate'):

    * 'propagate': returns nan
    * 'raise': throws an error
    * 'omit': performs the calculations ignoring nan values

    alternative : {'two-sided', 'less', 'greater'}, optional
            Defines the alternative hypothesis.
    The following options are available (default is 'two-sided'):

    * 'two-sided': the kurtosis of the distribution underlying the sample
            is different from that of the normal distribution
    * 'less': the kurtosis of the distribution underlying the sample
            is less than that of the normal distribution
    * 'greater': the kurtosis of the distribution underlying the sample
            is greater than that of the normal distribution

    .. versionadded:: 1.7.0

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = OrderedPair(
        x=default.x,
        y=scipy.stats.kurtosistest(
            a=default.y,
            axis=axis,
            nan_policy=nan_policy,
            alternative=alternative,
        ),
    )

    return result
