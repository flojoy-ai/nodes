import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def WALD(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from a Wald, or inverse Gaussian, distribution.

    Samples are drawn from a Wald, or inverse Gaussian, distribution with
    specified mean and scale parameters.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    mean : float or array_like of floats
        Distribution mean, must be > 0.
    scale : float or array_like of floats
        Scale parameter, must be > 0.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``mean`` and ``scale`` are both scalars.
        Otherwise, ``np.broadcast(mean, scale).size`` samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized Wald distribution.

    See Also
    --------
    random.Generator.wald: which should be used for new code.

    Notes
    -----
    The probability density function for the Wald distribution is

    .. math:: P(x;mean,scale) = \sqrt{\frac{scale}{2\pi x^3}}e^
                                \frac{-scale(x-mean)^2}{2\cdotp mean^2x}

    As noted above the inverse Gaussian distribution first arise
    from attempts to model Brownian motion. It is also a
    competitor to the Weibull for use in reliability modeling and
    modeling stock returns and interest rate processes.

    References
    ----------
    .. [1] Brighton Webs Ltd., Wald Distribution,
            https://web.archive.org/web/20090423014010/http://www.brighton-webs.co.uk:80/distributions/wald.asp
    .. [2] Chhikara, Raj S., and Folks, J. Leroy, "The Inverse Gaussian
            Distribution: Theory : Methodology, and Applications", CRC Press,
            1988.
    .. [3] Wikipedia, "Inverse Gaussian distribution"
            https://en.wikipedia.org/wiki/Inverse_Gaussian_distribution

    Examples
    --------
    Draw values from the distribution and plot the histogram:

    >>> import matplotlib.pyplot as plt
    >>> h = plt.hist(np.random.wald(3, 2, 100000), bins=200, density=True)
    >>> plt.show()


    """
    mean: float = params.get("mean", 0.0)
    std: float = params.get("std", 1.0)
    size: str = params.get("size", "dc[0].y.shape")
    return DataContainer(
        x=dc[0].y, y=np.random.wald(float(mean), float(std), size=eval(size))
    )
