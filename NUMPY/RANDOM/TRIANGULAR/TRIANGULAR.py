import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List
@flojoy


def TRIANGULAR(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from the triangular distribution over the interval [left, right].
    
    The triangular distribution is a continuous probability distribution with lower limit left, peak at mode, and upper limit right. Unlike the other distributions, these parameters directly define the shape of the distribution.
    
    
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    left : float or array_like of floats
        Lower limit.
    mode : float or array_like of floats
        The value where the peak of the distribution occurs.
        The value must fulfill the condition ``left <= mode <= right``.
    right : float or array_like of floats
        Upper limit, must be larger than `left`.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``left``, ``mode``, and ``right``
        are all scalars.  Otherwise, ``np.broadcast(left, mode, right).size``
        samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized triangular distribution.

    See Also
    --------
    random.Generator.triangular: which should be used for new code.

    Notes
    -----
    The probability density function for the triangular distribution is

    .. math:: P(x;l, m, r) = \begin{cases}
                \frac{2(x-l)}{(r-l)(m-l)}& \text{for $l \leq x \leq m$},\\
                \frac{2(r-x)}{(r-l)(r-m)}& \text{for $m \leq x \leq r$},\\
                0& \text{otherwise}.
                \end{cases}

    The triangular distribution is often used in ill-defined
    problems where the underlying distribution is not known, but
    some knowledge of the limits and mode exists. Often it is used
    in simulations.

    References
    ----------
    .. [1] Wikipedia, "Triangular distribution"
            https://en.wikipedia.org/wiki/Triangular_distribution

    Examples
    --------
    Draw values from the distribution and plot the histogram:

    >>> import matplotlib.pyplot as plt
    >>> h = plt.hist(np.random.triangular(-3, 0, 8, 100000), bins=200,
    ...              density=True)
    >>> plt.show()

    """
    left: float = params.get('left', 0.0)
    mode: float = params.get('mode', 0.0)
    right: float = params.get('right', 1.0)
    size = params.get("size", 'dc[0].y.shape')
    
    out = np.random.triangular(float(left), float(mode), float(right), size=eval(size))
    return DataContainer(x=dc[0].y, y=out)