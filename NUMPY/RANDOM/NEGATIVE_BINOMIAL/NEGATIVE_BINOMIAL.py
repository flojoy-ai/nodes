import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def NEGATIVE_BINOMIAL(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from a negative binomial distribution.

    Samples are drawn from a negative binomial distribution with specified
    parameters, `n` successes and `p` probability of success where `n` is an
    integer > 0 and `p` is in the interval [0, 1].


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    n : float or array_like of floats
        Parameter of the distribution, > 0.
    p : float or array_like of floats
        Parameter of the distribution, >= 0 and <=1.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``n`` and ``p`` are both scalars.
        Otherwise, ``np.broadcast(n, p).size`` samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized negative binomial distribution,
        where each sample is equal to N, the number of failures that
        occurred before a total of n successes was reached.

    See Also
    --------
    random.Generator.negative_binomial: which should be used for new code.

    Notes
    -----
    The probability mass function of the negative binomial distribution is

    .. math:: P(N;n,p) = \frac{\Gamma(N+n)}{N!\Gamma(n)}p^{n}(1-p)^{N},

    where :math:`n` is the number of successes, :math:`p` is the
    probability of success, :math:`N+n` is the number of trials, and
    :math:`\Gamma` is the gamma function. When :math:`n` is an integer,
    :math:`\frac{\Gamma(N+n)}{N!\Gamma(n)} = \binom{N+n-1}{N}`, which is
    the more common form of this term in the the pmf. The negative
    binomial distribution gives the probability of N failures given n
    successes, with a success on the last trial.

    If one throws a die repeatedly until the third time a "1" appears,
    then the probability distribution of the number of non-"1"s that
    appear before the third "1" is a negative binomial distribution.

    References
    ----------
    .. [1] Weisstein, Eric W. "Negative Binomial Distribution." From
            MathWorld--A Wolfram Web Resource.
            http://mathworld.wolfram.com/NegativeBinomialDistribution.html
    .. [2] Wikipedia, "Negative binomial distribution",
            https://en.wikipedia.org/wiki/Negative_binomial_distribution

    Examples
    --------
    Draw samples from the distribution:

    A real world example. A company drills wild-cat oil
    exploration wells, each with an estimated probability of
    success of 0.1.  What is the probability of having one success
    for each successive well, that is what is the probability of a
    single success after drilling 5 wells, after 6 wells, etc.?

    >>> s = np.random.negative_binomial(1, 0.1, 100000)
    >>> for i in range(1, 11): # doctest: +SKIP
    ...    probability = sum(s<i) / 100000.
    ...    print(i, "wells drilled, probability of one success =", probability)


    """
    n: int = params.get("n", 1)
    p: float = params.get("p", 0.5)
    size: str = params.get("size", "dc[0].y.shape")

    out = np.random.negative_binomial(int(n), float(p), size=eval(size))
    return DataContainer(x=dc[0].y, y=out)
