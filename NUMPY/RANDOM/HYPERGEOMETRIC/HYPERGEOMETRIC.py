import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def HYPERGEOMETRIC(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from a Hypergeometric distribution.

    Samples are drawn from a Hypergeometric distribution with specified
    parameters, ngood (ways to make a good selection), nbad (ways to make
    a bad selection), and nsample = number of items sampled, which is less
    than or equal to the sum ngood + nbad.  'ngood' and 'nbad' can be
    thought of as representing the number of white and black balls in an
    urn, respectively.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    ngood : int or array_like of ints
        Number of ways to make a good selection.  Must be nonnegative.
    nbad : int or array_like of ints
        Number of ways to make a bad selection.  Must be nonnegative.
    nsample : int or array_like of ints
        Number of items sampled.  Must be at least 1 and at most
        ``ngood + nbad``.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if `ngood`, `nbad`, and `nsample`
        are all scalars.  Otherwise, ``np.broadcast(ngood, nbad, nsample).size``
        samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized hypergeometric distribution. Each
        sample is the number of good items within a randomly selected subset of
        size `nsample` taken from a set of `ngood` good items and `nbad` bad items.

    See Also
    --------
    scipy.stats.hypergeom : probability density function, distribution or
        cumulative density function, etc.
    random.Generator.hypergeometric: which should be used for new code.

    Notes
    -----
    The probability density for the Hypergeometric distribution is

    .. math:: P(x) = \frac{\binom{g}{x}\binom{b}{n-x}}{\binom{g+b}{n}},

    where :math:`0 \le x \le n` and :math:`n-b \le x \le g`

    for P(x) the probability of ``x`` good results in the drawn sample,
    g = `ngood`, b = `nbad`, and n = `nsample`.

    Consider an urn with black and white marbles in it, `ngood` of them
    are black and `nbad` are white. If you draw `nsample` balls without
    replacement, then the hypergeometric distribution describes the
    distribution of black balls in the drawn sample.

    Note that this distribution is very similar to the binomial
    distribution, except that in this case, samples are drawn without
    replacement, whereas in the Binomial case samples are drawn with
    replacement (or the sample space is infinite). As the sample space
    becomes large, this distribution approaches the binomial.

    References
    ----------
    .. [1] Lentner, Marvin, "Elementary Applied Statistics", Bogden
            and Quigley, 1972.
    .. [2] Weisstein, Eric W. "Hypergeometric Distribution." From
            MathWorld--A Wolfram Web Resource.
            http://mathworld.wolfram.com/HypergeometricDistribution.html
    .. [3] Wikipedia, "Hypergeometric distribution",
            https://en.wikipedia.org/wiki/Hypergeometric_distribution

    Examples
    --------
    Draw samples from the distribution:

    >>> ngood, nbad, nsamp = 100, 2, 10
    # number of good, number of bad, and number of samples
    >>> s = np.random.hypergeometric(ngood, nbad, nsamp, 1000)
    >>> from matplotlib.pyplot import hist
    >>> hist(s)
    #   note that it is very unlikely to grab both bad items

    Suppose you have an urn with 15 white and 15 black marbles.
    If you pull 15 marbles at random, how likely is it that
    12 or more of them are one color?

    >>> s = np.random.hypergeometric(15, 15, 15, 100000)
    >>> sum(s>=12)/100000. + sum(s<=3)/100000.
    #   answer = 0.003 ... pretty unlikely!


    """
    # Strictly type all internal variables
    ngood: int = params.get("ngood", 1)
    nbad: int = params.get("nbad", 1)
    nsample: int = params.get("nsample", 2)
    size: str = params.get("size", 'dc[0].y.shape')
    # Return the result of the function
    out = np.random.hypergeometric(ngood=int(ngood), nbad=int(nbad), nsample=int(nsample), size=eval(size))
    return DataContainer(x=dc[0].y, y=out)
