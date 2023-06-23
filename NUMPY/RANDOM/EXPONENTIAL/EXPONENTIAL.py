import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def EXPONENTIAL(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from an exponential distribution.

    Its probability density function is

    .. math:: f(x; \\frac{1}{\\beta}) = \\frac{1}{\\beta} \exp(-\\frac{x}{\\beta}),

    for ``x > 0`` and 0 elsewhere. :math:`\\beta` is the scale parameter,
    which is the inverse of the rate parameter :math:`\\lambda = 1/\\beta`.
    The rate parameter is an alternative, widely used parameterization
    of the exponential distribution [3]_.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    scale : float or array_like of floats
        The scale parameter, :math:`\beta = 1/\lambda`. Must be
        non-negative.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``scale`` is a scalar.  Otherwise,
        ``np.array(scale).size`` samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized exponential distribution.

    See Also
    --------
    random.Generator.exponential: which should be used for new code.

    References
    ----------
    .. [1] Peyton Z. Peebles Jr., "Probability, Random Variables and
            Random Signal Principles", 4th ed, 2001, p. 57.
    .. [2] Wikipedia, "Poisson process",
            https://en.wikipedia.org/wiki/Poisson_process
    .. [3] Wikipedia, "Exponential distribution",
            https://en.wikipedia.org/wiki/Exponential_distribution


    """
    # Strictly type all internal variables
    beta: float = params.get("beta", 1.0)

    # Calculate and return the exponential distribution
    out = (1.0 / float(beta)) * np.exp(-dc[0].y / float(beta))
    return DataContainer(x=dc[0].y, y=out)
