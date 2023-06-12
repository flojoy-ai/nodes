from flojoy import DataContainer, flojoy
import scipy.stats


@flojoy
def SKEW(dc, params):
    """



            Compute the sample skewness of a data set.

            For normally distributed data, the skewness should be about zero. For
            unimodal continuous distributions, a skewness value greater than zero means
            that there is more weight in the right tail of the distribution. The
            function `skewtest` can be used to determine if the skewness value
            is close enough to zero, statistically speaking.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    a : ndarray
            Input array.
    axis : int or None, default: 0
            If an int, the axis of the input along which to compute the statistic.
            The statistic of each axis-slice (e.g. row) of the input will appear in a
            corresponding element of the output.
            If ``None``, the input will be raveled before computing the statistic.
    bias : bool, optional
            If False, then the calculations are corrected for statistical bias.
    nan_policy : {'propagate', 'omit', 'raise'}
            Defines how to handle input NaNs.

    - ``propagate``: if a NaN is present in the axis slice (e.g. row) along
            which the  statistic is computed, the corresponding entry of the output
            will be NaN.
    - ``omit``: NaNs will be omitted when performing the calculation.
            If insufficient data remains in the axis slice along which the
            statistic is computed, the corresponding entry of the output will be
            NaN.
    - ``raise``: if a NaN is present, a ``ValueError`` will be raised.
    keepdims : bool, default: False
            If this is set to True, the axes which are reduced are left
            in the result as dimensions with size one. With this option,
            the result will broadcast correctly against the input array.
    """
    return DataContainer(
        x=dc[0].y,
        y=scipy.stats.skew(
            a=dc[0].y,
            axis=(int(params["axis"]) if params["axis"] != "" else None),
            bias=(bool(params["bias"]) if params["bias"] != "" else None),
            nan_policy=(
                str(params["nan_policy"]) if params["nan_policy"] != "" else None
            ),
            keepdims=(bool(params["keepdims"]) if params["keepdims"] != "" else None),
        ),
    )
