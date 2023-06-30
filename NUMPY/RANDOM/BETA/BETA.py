import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def BETA(dc: list, params: dict) -> DataContainer:
    """
        Draw samples from a Beta distribution.

    The Beta distribution is a special case of the Dirichlet distribution,
    and is related to the Gamma distribution.  It has the probability
    distribution function

    .. math:: f(x; a,b) = \frac{1}{B(\alpha, \beta)} x^{\alpha - 1}
                                                (1 - x)^{\beta - 1},

    where the normalisation, B, is the beta function,

    .. math:: B(\alpha, \beta) = \int_0^1 t^{\alpha - 1}
                                            (1 - t)^{\beta - 1} dt.

    It is often seen in Bayesian inference and order statistics.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    a : float or array_like of floats
        Alpha, positive (>0).
    b : float or array_like of floats
        Beta, positive (>0).
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``a`` and ``b`` are both scalars.
        Otherwise, ``np.broadcast(a, b).size`` samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized beta distribution.

    See Also
    --------
    random.Generator.beta: which should be used for new code.

    """
    a: float = params.get("a", None)
    b: float = params.get("b", None)
    size: str = params.get("size", "dc[0].y.shape")

    out = np.random.beta(float(a), float(b), size=eval(size))
    return DataContainer(x=dc[0].y, y=out)
