from flojoy import DataContainer, flojoy, DefaultParams
import scipy.stats


@flojoy
def SHAPIRO(default: DataContainer, default_params: DefaultParams):
    """
            Perform the Shapiro-Wilk test for normality.

            The Shapiro-Wilk test tests the null hypothesis that the
            data was drawn from a normal distribution.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    x : array_like
            Array of sample data.
    """
    return DataContainer(x=dc[0].y, y=scipy.stats.shapiro(x=dc[0].y))
