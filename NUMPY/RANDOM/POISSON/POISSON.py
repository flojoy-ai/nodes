import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def POISSON(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from a Poisson distribution.

    Samples are drawn from a Poisson distribution with specified
    parameters, where both the mean and the variance are equal to
    `dc[0].y`.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    lam : float or array_like of floats
        Expected number of events occurring in a fixed-time interval,
        must be >= 0. A sequence must be broadcastable over the requested
        size.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``lam`` is a scalar. Otherwise,
        ``np.array(lam).size`` samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized Poisson distribution.

    See Also
    --------
    random.Generator.poisson: which should be used for new code.

    Notes
    -----
    The Poisson distribution

    .. math:: f(k; \lambda)=\frac{\lambda^k e^{-\lambda}}{k!}

    For events with an expected separation :math:`\lambda` the Poisson
    distribution :math:`f(k; \lambda)` describes the probability of
    :math:`k` events occurring within the observed
    interval :math:`\lambda`.

    Because the output is limited to the range of the C int64 type, a
    ValueError is raised when `lam` is within 10 sigma of the maximum
    representable value.

    References
    ----------
    .. [1] Weisstein, Eric W. "Poisson Distribution."
            From MathWorld--A Wolfram Web Resource.
            http://mathworld.wolfram.com/PoissonDistribution.html
    .. [2] Wikipedia, "Poisson distribution",
            https://en.wikipedia.org/wiki/Poisson_distribution

    Examples
    --------
    Draw samples from the distribution:

    >>> import numpy as np
    >>> s = np.random.poisson(5, 10000)

    Display histogram of the sample:

    >>> import matplotlib.pyplot as plt
    >>> count, bins, ignored = plt.hist(s, 14, density=True)
    >>> plt.show()

    Draw each 100 values for lambda 100 and 500:

    >>> s = np.random.poisson(lam=(100., 500.), size=(100, 2))

    """
    # Extract optional arguments
    size: str = params.get("size", 'dc[0].y.shape')
    lam: float = params.get("lam", 0.0)

    # Draw samples from the Poisson distribution
    out = np.random.poisson(lam=float(lam), size=eval(size))

    # Return custom class
    return DataContainer(x=dc[0].y, y=out)
