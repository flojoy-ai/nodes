from flojoy import DataContainer, flojoy
import scipy.stats


@flojoy
def TRIM_MEAN(dc, params):
    """
            Return mean of array after trimming distribution from both tails.

            If `proportiontocut` = 0.1, slices off 'leftmost' and 'rightmost' 10% of
            scores. The input is sorted before slicing. Slices off less if proportion
            results in a non-integer slice index (i.e., conservatively slices off
            `proportiontocut` ).

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    a : array_like
            Input array.
    proportiontocut : float
            Fraction to cut off of both tails of the distribution.
    axis : int or None, optional
            Axis along which the trimmed means are computed. Default is 0.
            If None, compute over the whole array `a`.
    """
    return DataContainer(
        x=dc[0].y,
        y=scipy.stats.trim_mean(
            a=dc[0].y,
            proportiontocut=(
                float(params["proportiontocut"])
                if params["proportiontocut"] != ""
                else None
            ),
            axis=(int(params["axis"]) if params["axis"] != "" else None),
        ),
    )
