from flojoy import DataContainer, flojoy
import scipy.stats


@flojoy
def TMAX(
    default: DataContainer,
    upperlimit: float = None,
    axis: int = 0,
    inclusive: bool = True,
    nan_policy: str = "propagate",
):
    """
            Compute the trimmed maximum.

            This function computes the maximum value of an array along a given axis,
            while ignoring values larger than a specified upper limit.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    a : array_like
            Array of values.
    upperlimit : None or float, optional
            Values in the input array greater than the given limit will be ignored.
            When upperlimit is None, then all values are used. The default value
            is None.
    axis : int or None, optional
            Axis along which to operate. Default is 0. If None, compute over the
            whole array `a`.
    inclusive : {True, False}, optional
            This flag determines whether values exactly equal to the upper limit
            are included.  The default value is True.
    nan_policy : {'propagate', 'raise', 'omit'}, optional
            Defines how to handle when input contains nan.
    The following options are available (default is 'propagate'):

    * 'propagate': returns nan
    * 'raise': throws an error
    * 'omit': performs the calculations ignoring nan values
    """
    return DataContainer(
        x=dc[0].y,
        y=scipy.stats.tmax(
            a=dc[0].y,
            upperlimit=None or float(params["upperlimit"])
            if params["upperlimit"] != ""
            else None,
            axis=int(params["axis"]) if params["axis"] != "" else None,
            inclusive=bool(params["inclusive"]) if params["inclusive"] != "" else None,
            nan_policy=str(params["nan_policy"])
            if params["nan_policy"] != ""
            else None,
        ),
    )
