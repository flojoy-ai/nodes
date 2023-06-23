import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def GUMBEL(dc: list, params: dict) -> DataContainer:
    """Draw samples from a Gumbel distribution.

    Draw samples from a Gumbel distribution with specified location and scale.
    The Gumbel distribution is a type of extreme value distribution. It may be
    used to model the maximum value of a collection of samples of various
    distributions.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    loc : float or array_like of floats, optional
        The location of the mode of the distribution. Default is 0.
    scale : float or array_like of floats, optional
        The scale parameter of the distribution. Default is 1. Must be non-
        negative.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``loc`` and ``scale`` are both scalars.
        Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized Gumbel distribution.

    See Also
    --------
    scipy.stats.gumbel_l
    scipy.stats.gumbel_r
    scipy.stats.genextreme
    weibull
    random.Generator.gumbel: which should be used for new code.

    Notes
    -----
    The Gumbel (or Smallest Extreme Value (SEV) or the Smallest Extreme
    Value Type I) distribution is one of a class of Generalized Extreme
    Value (GEV) distributions used in modeling extreme value problems.
    The Gumbel is a special case of the Extreme Value Type I distribution
    for maximums from distributions with "exponential-like" tails.

    The probability density for the Gumbel distribution is

    .. math:: p(x) = \frac{e^{-(x - \mu)/ \beta}}{\beta} e^{ -e^{-(x - \mu)/
                \beta}},

    where :math:`\mu` is the mode, a location parameter, and
    :math:`\beta` is the scale parameter.

    The Gumbel (named for German mathematician Emil Julius Gumbel) was used
    very early in the hydrology literature, for modeling the occurrence of
    flood events. It is also used for modeling maximum wind speed and
    rainfall rates.  It is a "fat-tailed" distribution - the probability of
    an event in the tail of the distribution is larger than if one used a
    Gaussian, hence the surprisingly frequent occurrence of 100-year
    floods. Floods were initially modeled as a Gaussian process, which
    underestimated the frequency of extreme events.

    It is one of a class of extreme value distributions, the Generalized
    Extreme Value (GEV) distributions, which also includes the Weibull and
    Frechet.

    The function has a mean of :math:`\mu + 0.57721\beta` and a variance
    of :math:`\frac{\pi^2}{6}\beta^2`.

    References
    ----------
    .. [1] Gumbel, E. J., "Statistics of Extremes,"
            New York: Columbia University Press, 1958.
    .. [2] Reiss, R.-D. and Thomas, M., "Statistical Analysis of Extreme
            Values from Insurance, Finance, Hydrology and Other Fields,"
            Basel: Birkhauser Verlag, 2001.

    Examples
    --------
    Draw samples from the distribution:

    >>> mu, beta = 0, 0.1 # location and scale
    >>> s = np.random.gumbel(mu, beta, 1000)

    Display the histogram of the samples, along with
    the probability density function:

    >>> import matplotlib.pyplot as plt
    >>> count, bins, ignored = plt.hist(s, 30, density=True)
    >>> plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
    ...          * np.exp( -np.exp( -(bins - mu) /beta) ),
    ...          linewidth=2, color='r')
    >>> plt.show()

    Show how an extreme value distribution can arise from a Gaussian process
    and compare to a Gaussian:

    >>> means = []
    >>> maxima = []
    >>> for i in range(0,1000) :
    ...    a = np.random.normal(mu, beta, 1000)
    ...    means.append(a.mean())
    ...    maxima.append(a.max())
    >>> count, bins, ignored = plt.hist(maxima, 30, density=True)
    >>> beta = np.std(maxima) * np.sqrt(6) / np.pi
    >>> mu = np.mean(maxima) - 0.57721*beta
    >>> plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)
    ...          * np.exp(-np.exp(-(bins - mu)/beta)),
    ...          linewidth=2, color='r')
    >>> plt.plot(bins, 1/(beta * np.sqrt(2 * np.pi))
    ...          * np.exp(-(bins - mu)**2 / (2 * beta**2)),
    ...          linewidth=2, color='g')
    >>> plt.show()
    """
    loc: float = params.get("loc", 0.0)
    scale: float = params.get("scale", 1.0)
    size: str = params.get("size", "dc[0].y.shape")
    return DataContainer(
        x=dc[0].y,
        y=np.random.gumbel(loc=float(loc), scale=float(scale), size=eval(size)),
    )
