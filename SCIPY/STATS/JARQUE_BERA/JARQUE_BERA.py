from flojoy import DataContainer, flojoy
import scipy.stats


@flojoy
def JARQUE_BERA(dc, params):
    """
            Perform the Jarque-Bera goodness of fit test on sample data.

            The Jarque-Bera test tests whether the sample data has the skewness and
            kurtosis matching a normal distribution.

            Note that this test only works for a large enough number of data samples
            (>2000) as the test statistic asymptotically has a Chi-squared distribution
            with 2 degrees of freedom.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    x : array_like
            Observations of a random variable.
    """
    return DataContainer(
        x=dc[0].y,
        y=scipy.stats.jarque_bera(
            x=dc[0].y,
        ),
    )
