from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import scipy.stats


@flojoy(node_type="default")
def DESCRIBE(
    default: OrderedPair | Matrix,
    axis: int = 0,
    ddof: int = 1,
    bias: bool = True,
    nan_policy: str = "propagate",
    select_return: Literal["nobs", "mean", "variance", "skewness", "kurtosis"] = "nobs",
) -> OrderedPair | Matrix | Scalar:
    """The DESCRIBE node is based on a numpy or scipy function.
    The description of that function is as follows:

            Compute several descriptive statistics of the passed array.

    Parameters
    ----------
    select_return : This function has returns multiple Objects:
            ['nobs', 'mean', 'variance', 'skewness', 'kurtosis']. Select the desired one to return.
            See the respective function docs for descriptors.
    a : array_like
            Input data.
    axis : int or None, optional
            Axis along which statistics are calculated. Default is 0.
            If None, compute over the whole array `a`.
    ddof : int, optional
            Delta degrees of freedom (only for variance).  Default is 1.
    bias : bool, optional
            If False, then the skewness and kurtosis calculations are corrected
            for statistical bias.
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
        m=scipy.stats.describe(
            a=default.y,
            axis=axis,
            ddof=ddof,
            bias=bias,
            nan_policy=nan_policy,
        )
    )

    return result
