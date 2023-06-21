import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List
@flojoy


def GEOMETRIC(dc: list, params: dict) -> DataContainer:
    """
    Draws samples from the geometric distribution.
    The geometric distribution is a discrete probability distribution of the number
    of Bernoulli trials needed to get one success.
    
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    p : float or array_like of floats
        The probability of success of an individual trial.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``p`` is a scalar.  Otherwise,
        ``np.array(p).size`` samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized geometric distribution.

    See Also
    --------
    random.Generator.geometric: which should be used for new code.

    Examples
    --------
    Draw ten thousand values from the geometric distribution,
    with the probability of an individual success equal to 0.35:

    >>> z = np.random.geometric(p=0.35, size=10000)

    How many trials succeeded after a single run?

    >>> (z == 1).sum() / 10000.
    0.34889999999999999 #random

    """
    p = params.get('p', 0.5)
    size = params.get('size', 'dc[0].y.shape')
    return DataContainer(x=dc[0].y, y=np.random.geometric(float(p), size=eval(size)))