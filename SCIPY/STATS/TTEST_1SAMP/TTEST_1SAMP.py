from flojoy import DataContainer, flojoy, DefaultParams
import scipy.stats

@flojoy
def TTEST_1SAMP(default: DataContainer, default_parmas: DefaultParams, popmean: float or array_like=None, axis: int=0, nan_policy: str='propagate', alternative: str='two-sided'):
    """
            Calculate the T-test for the mean of ONE group of scores.

            This is a test for the null hypothesis that the expected value
            (mean) of a sample of independent observations `a` is equal to the given
            population mean, `popmean`.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    a : array_like
            Sample observation.
    popmean : float or array_like
            Expected value in null hypothesis. If array_like, then it must have the
            same shape as `a` excluding the axis dimension.
    axis : int or None, optional
            Axis along which to compute test; default is 0. If None, compute over
            the whole array `a`.
    nan_policy : {'propagate', 'raise', 'omit'}, optional
            Defines how to handle when input contains nan.
    The following options are available (default is 'propagate'):

    * 'propagate': returns nan
    * 'raise': throws an error
    * 'omit': performs the calculations ignoring nan values

    alternative : {'two-sided', 'less', 'greater'}, optional
            Defines the alternative hypothesis.
    The following options are available (default is 'two-sided'):

    * 'two-sided': the mean of the underlying distribution of the sample
            is different than the given population mean (`popmean`)
    * 'less': the mean of the underlying distribution of the sample is
            less than the given population mean (`popmean`)
    * 'greater': the mean of the underlying distribution of the sample is
            greater than the given population mean (`popmean`)

    .. versionadded:: 1.6.0
    """
    return DataContainer(x=dc[0].y, y=scipy.stats.ttest_1samp(a=dc[0].y, popmean=float or array_like(params['popmean']) if params['popmean'] != '' else None, axis=int(params['axis']) if params['axis'] != '' else None, nan_policy=str(params['nan_policy']) if params['nan_policy'] != '' else None, alternative=str(params['alternative']) if params['alternative'] != '' else None))