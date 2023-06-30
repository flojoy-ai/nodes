import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def RAYLEIGH(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from a Rayleigh distribution.

    The :math:`\chi` and Weibull distributions are generalizations of the
    Rayleigh.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    scale : float or array_like of floats, optional
        Scale, also equals the mode. Must be non-negative. Default is 1.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``scale`` is a scalar.  Otherwise,
        ``np.array(scale).size`` samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized Rayleigh distribution.

    See Also
    --------
    random.Generator.rayleigh: which should be used for new code.

    Notes
    -----
    The probability density function for the Rayleigh distribution is

    .. math:: P(x;scale) = \frac{x}{scale^2}e^{\frac{-x^2}{2 \cdotp scale^2}}

    The Rayleigh distribution would arise, for example, if the East
    and North components of the wind velocity had identical zero-mean
    Gaussian distributions.  Then the wind speed would have a Rayleigh
    distribution.

    References
    ----------
    .. [1] Brighton Webs Ltd., "Rayleigh Distribution,"
            https://web.archive.org/web/20090514091424/http://brighton-webs.co.uk:80/distributions/rayleigh.asp
    .. [2] Wikipedia, "Rayleigh distribution"
            https://en.wikipedia.org/wiki/Rayleigh_distribution

    Examples
    --------
    Draw values from the distribution and plot the histogram

    >>> from matplotlib.pyplot import hist
    >>> values = hist(np.random.rayleigh(3, 100000), bins=200, density=True)

    Wave heights tend to follow a Rayleigh distribution. If the mean wave
    height is 1 meter, what fraction of waves are likely to be larger than 3
    meters?

    >>> meanvalue = 1
    >>> modevalue = np.sqrt(2 / np.pi) * meanvalue
    >>> s = np.random.rayleigh(modevalue, 1000000)

    The percentage of waves larger than 3 meters is:

    >>> 100.*sum(s>3)/1000000.
    0.087300000000000003 # random


    """
    scale = params.get("scale", 1.0)
    size = params.get("size", "dc[0].y.shape")
    out = np.random.rayleigh(scale=float(scale), size=eval(size))
    return DataContainer(x=dc[0].y, y=out)
