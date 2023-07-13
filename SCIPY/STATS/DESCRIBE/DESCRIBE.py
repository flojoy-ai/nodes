from flojoy import OrderedPair, flojoy
import scipy.stats


@flojoy(node_type="default")
def DESCRIBE(
    default: OrderedPair,
    axis: int = 0,
    ddof: int = 1,
    bias: bool = True,
    nan_policy: str = "propagate",
) -> OrderedPair:
    """The DESCRIBE node is based on a numpy or scipy function.
    The description of that function is as follows:

            Compute several descriptive statistics of the passed array.

    Parameters
    ----------
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
            type 'ordered pair'"""
    result = OrderedPair(
        x=default.x,
        y=scipy.stats.describe(
            a=default.y,
            axis=axis,
            ddof=ddof,
            bias=bias,
            nan_policy=nan_policy,
        ),
    )
    return result
