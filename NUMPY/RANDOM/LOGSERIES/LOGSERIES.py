import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def LOGSERIES(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from a Logarithmic Series distribution.

    Samples are drawn from a logarithmic series distribution with specified
    shape parameter, 0 <= dc[0].y <= 1.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    p : float or array_like of floats
        Shape parameter for the distribution.  Must be in the range (0, 1).
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``p`` is a scalar.  Otherwise,
        ``np.array(p).size`` samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized logarithmic series distribution.

    See Also
    --------
    scipy.stats.logser : probability density function, distribution or
        cumulative density function, etc.
    random.Generator.logseries: which should be used for new code.

    Notes
    -----
    The probability density for the Log Series distribution is

    .. math:: P(k) = \frac{-p^k}{k \ln(1-p)},

    where p = probability.

    The log series distribution is frequently used to represent species
    richness and occurrence, first proposed by Fisher, Corbet, and
    Williams in 1943 [2].  It may also be used to model the numbers of
    occupants seen in cars [3].

    References
    ----------
    .. [1] Buzas, Martin A.; Culver, Stephen J.,  Understanding regional
            species diversity through the log series distribution of
            occurrences: BIODIVERSITY RESEARCH Diversity & Distributions,
            Volume 5, Number 5, September 1999 , pp. 187-195(9).
    .. [2] Fisher, R.A,, A.S. Corbet, and C.B. Williams. 1943. The
            relation between the number of species and the number of
            individuals in a random sample of an animal population.
            Journal of Animal Ecology, 12:42-58.
    .. [3] D. J. Hand, F. Daly, D. Lunn, E. Ostrowski, A Handbook of Small
            Data Sets, CRC Press, 1994.
    .. [4] Wikipedia, "Logarithmic distribution",
            https://en.wikipedia.org/wiki/Logarithmic_distribution

    Examples
    --------
    Draw samples from the distribution:

    >>> a = .6
    >>> s = np.random.logseries(a, 10000)
    >>> import matplotlib.pyplot as plt
    >>> count, bins, ignored = plt.hist(s)

    #   plot against distribution

    >>> def logseries(k, p):
    ...     return -p**k/(k*np.log(1-p))
    >>> plt.plot(bins, logseries(bins, a)*count.max()/
    ...          logseries(bins, a).max(), 'r')
    >>> plt.show()


    """
    # Enforce strict typing
    size: str = params.get("size", 'dc[0].y.shape')
    p: float = params.get("loc", 0.5)

    # Check that dc[0].y is in the range [0, 1]
    if not 0 <= p <= 1:
        raise ValueError("dc[0].y must be in the range [0, 1].")

    # Draw samples from the logarithmic series distribution
    out = np.random.logseries(p=float(p), size=eval(size))

    # Return a DataContainer instance
    return DataContainer(x=dc[0].y, y=out)
