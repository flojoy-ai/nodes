from flojoy import DataContainer, flojoy, DefaultParams
import scipy.stats


@flojoy
def KURTOSISTEST(
    default: DataContainer,
    default_params: DefaultParams,
    axis: int = 0,
    nan_policy: str = "propagate",
    alternative: str = "two-sided",
):
    """
            Test whether a dataset has normal kurtosis.

            This function tests the null hypothesis that the kurtosis
            of the population from which the sample was drawn is that
            of the normal distribution.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
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
    """
    return DataContainer(
        x=dc[0].y,
        y=scipy.stats.kurtosistest(
            a=dc[0].y,
            axis=int(params["axis"]) if params["axis"] != "" else None,
            nan_policy=str(params["nan_policy"])
            if params["nan_policy"] != ""
            else None,
            alternative=str(params["alternative"])
            if params["alternative"] != ""
            else None,
        ),
    )
