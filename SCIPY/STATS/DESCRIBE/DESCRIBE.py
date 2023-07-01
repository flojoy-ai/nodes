from flojoy import DataContainer, flojoy, DefaultParams
import scipy.stats


@flojoy
def DESCRIBE(
    default: DataContainer,
    default_params: DefaultParams,
    axis: int = 0,
    ddof: int = 1,
    bias: bool = True,
    nan_policy: str = "propagate",
):
    """
            Compute several descriptive statistics of the passed array.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

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
    """
    return DataContainer(
        x=dc[0].y,
        y=scipy.stats.describe(
            a=dc[0].y,
            axis=int(params["axis"]) if params["axis"] != "" else None,
            ddof=int(params["ddof"]) if params["ddof"] != "" else None,
            bias=bool(params["bias"]) if params["bias"] != "" else None,
            nan_policy=str(params["nan_policy"])
            if params["nan_policy"] != ""
            else None,
        ),
    )
