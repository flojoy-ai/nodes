from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import scipy.stats


@flojoy
def NORMALTEST(
    default: OrderedPair | Matrix,
    axis: int = 0,
    nan_policy: str = "propagate",
    select_return: Literal["statistic", "pvalue"] = "statistic",
) -> OrderedPair | Matrix | Scalar:
    """The NORMALTEST node is based on a numpy or scipy function.
    The description of that function is as follows:

            Test whether a sample differs from a normal distribution.

            This function tests the null hypothesis that a sample comes
            from a normal distribution.  It is based on D'Agostino and
            Pearson's [1]_, [2]_ test that combines skew and kurtosis to
            produce an omnibus test of normality.

    Parameters
    ----------
    select_return : This function has returns multiple Objects:
            ['statistic', 'pvalue']. Select the desired one to return.
            See the respective function docs for descriptors.
    a : array_like
            The array containing the sample to be tested.
    axis : int or None, optional
            Axis along which to compute test. Default is 0. If None,
            compute over the whole array `a`.
    nan_policy : {'propagate', 'raise', 'omit'}, optional
            Defines how to handle when input contains nan.
    The following options are available (default is 'propagate'):

    * 'propagate': returns nan
    * 'raise': throws an error
    * 'omit': performs the calculations ignoring nan values

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = OrderedPair(
        x=default.x,
        y=scipy.stats.normaltest(
            a=default.y,
            axis=axis,
            nan_policy=nan_policy,
        ),
    )

    return result
