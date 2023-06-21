import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def STANDARD_GAMMA(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from a Gamma distribution.

    Samples are drawn from a Gamma distribution with specified parameters,
    shape (sometimes designated "k") and scale (sometimes designated
    "theta"), where both parameters are > 0.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    shape : float or array_like of floats
        Parameter, must be non-negative.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``shape`` is a scalar.  Otherwise,
        ``np.array(shape).size`` samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized standard gamma distribution.

    See Also
    --------
    scipy.stats.gamma : probability density function, distribution or
        cumulative density function, etc.
    random.Generator.standard_gamma: which should be used for new code.

    Notes
    -----
    The probability density for the Gamma distribution is

    .. math:: p(x) = x^{k-1}\frac{e^{-x/\theta}}{\theta^k\Gamma(k)},

    where :math:`k` is the shape and :math:`\theta` the scale,
    and :math:`\Gamma` is the Gamma function.

    The Gamma distribution is often used to model the times to failure of
    electronic components, and arises naturally in processes for which the
    waiting times between Poisson distributed events are relevant.

    References
    ----------
    .. [1] Weisstein, Eric W. "Gamma Distribution." From MathWorld--A
            Wolfram Web Resource.
            http://mathworld.wolfram.com/GammaDistribution.html
    .. [2] Wikipedia, "Gamma distribution",
            https://en.wikipedia.org/wiki/Gamma_distribution

    Examples
    --------
    Draw samples from the distribution:

    >>> shape, scale = 2., 1. # mean and width
    >>> s = np.random.standard_gamma(shape, 1000000)

    Display the histogram of the samples, along with
    the probability density function:

    >>> import matplotlib.pyplot as plt
    >>> import scipy.special as sps  # doctest: +SKIP
    >>> count, bins, ignored = plt.hist(s, 50, density=True)
    >>> y = bins**(shape-1) * ((np.exp(-bins/scale))/  # doctest: +SKIP
    ...                       (sps.gamma(shape) * scale**shape))
    >>> plt.plot(bins, y, linewidth=2, color='r')  # doctest: +SKIP
    >>> plt.show()


    """
    shape: float = params.get("shape", 1.0)
    size = params.get("size", 'dc[0].y.shape')
    out = np.random.standard_cauchy(shape=float(shape), size=eval(size))

    return DataContainer(
        x=dc[0].y, y=out
    )
