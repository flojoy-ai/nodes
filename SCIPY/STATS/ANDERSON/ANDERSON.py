from flojoy import DataContainer, flojoy, DefaultParams
import scipy.stats

@flojoy
def ANDERSON(default: DataContainer, default_parmas: DefaultParams, dist: str='norm'):
    """
            Anderson-Darling test for data coming from a particular distribution.

            The Anderson-Darling test tests the null hypothesis that a sample is
            drawn from a population that follows a particular distribution.
            For the Anderson-Darling test, the critical values depend on
            which distribution is being tested against.  This function works
            for normal, exponential, logistic, or Gumbel (Extreme Value
            Type I) distributions.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    x : array_like
            Array of sample data.
    dist : {'norm', 'expon', 'logistic', 'gumbel', 'gumbel_l', 'gumbel_r', 'extreme1'}, optional
            The type of distribution to test against.  The default is 'norm'.
            The names 'extreme1', 'gumbel_l' and 'gumbel' are synonyms for the
            same distribution.
    """
    return DataContainer(x=dc[0].y, y=scipy.stats.anderson(x=dc[0].y, dist=str(params['dist']) if params['dist'] != '' else None))