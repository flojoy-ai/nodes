from flojoy import DataContainer, flojoy, DefaultParams
import scipy.stats


@flojoy
def SEM(
    default: DataContainer,
    default_params: DefaultParams,
    axis: int = 0,
    ddof: int = 1,
    nan_policy: str = "propagate",
):
    """
            Compute standard error of the mean.

            Calculate the standard error of the mean (or standard error of
            measurement) of the values in the input array.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    a : array_like
            An array containing the values for which the standard error is
            returned.
    axis : int or None, optional
            Axis along which to operate. Default is 0. If None, compute over
            the whole array `a`.
    ddof : int, optional
            Delta degrees-of-freedom. How many degrees of freedom to adjust
            for bias in limited samples relative to the population estimate
            of variance. Defaults to 1.
    nan_policy : {'propagate', 'raise', 'omit'}, optional
            Defines how to handle when input contains nan.
    The following options are available (default is 'propagate'):

    * 'propagate': returns nan
    * 'raise': throws an error
    * 'omit': performs the calculations ignoring nan values
    """
    return DataContainer(
        x=dc[0].y,
        y=scipy.stats.sem(
            a=dc[0].y,
            axis=int(params["axis"]) if params["axis"] != "" else None,
            ddof=int(params["ddof"]) if params["ddof"] != "" else None,
            nan_policy=str(params["nan_policy"])
            if params["nan_policy"] != ""
            else None,
        ),
    )
