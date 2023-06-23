import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def STANDARD_EXPONENTIAL(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from a standard exponential distribution.

    Its probability density function is

    .. math:: f(x; \lambda) = \lambda e^{-\lambda x}

    for ``x > 0`` and 0 elsewhere. :math:`\lambda` is the rate parameter,
    which is the inverse of the scale parameter :math:`\beta = 1/\lambda`.
    The rate parameter is an alternative, widely used parameterization
    of the exponential distribution [3]_.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    out : float or ndarray
        Drawn samples.

    See Also
    --------
    random.Generator.standard_exponential: which should be used for new code.

    Examples
    --------
    Output a 3x8000 array:

    >>> n = np.random.standard_exponential((3, 8000))


    """
    size = params.get("size", "dc[0].y.shape")
    out = np.random.standard_exponential(size=eval(size))
    return DataContainer(x=dc[0].y, y=out)
