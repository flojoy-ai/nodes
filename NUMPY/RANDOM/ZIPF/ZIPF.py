import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def ZIPF(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from a Zipf distribution.

    Samples are drawn from a Zipf distribution with specified parameters
    a (distribution shape) and N (number of elements to draw).


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    a : float or array_like of floats
        Distribution parameter. Must be greater than 1.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``a`` is a scalar. Otherwise,
        ``np.array(a).size`` samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized Zipf distribution.

    See Also
    --------
    scipy.stats.zipf : probability density function, distribution, or
        cumulative density function, etc.
    random.Generator.zipf: which should be used for new code.

    Notes
    -----
    The probability density for the Zipf distribution is

    .. math:: p(k) = \frac{k^{-a}}{\zeta(a)},

    for integers :math:`k \geq 1`, where :math:`\zeta` is the Riemann Zeta
    function.

    It is named for the American linguist George Kingsley Zipf, who noted
    that the frequency of any word in a sample of a language is inversely
    proportional to its rank in the frequency table.

    References
    ----------
    .. [1] Zipf, G. K., "Selected Studies of the Principle of Relative
            Frequency in Language," Cambridge, MA: Harvard Univ. Press,
            1932.

    Examples
    --------
    Draw samples from the distribution:

    >>> a = 4.0
    >>> n = 20000
    >>> s = np.random.zipf(a, n)

    Display the histogram of the samples, along with
    the expected histogram based on the probability
    density function:

    >>> import matplotlib.pyplot as plt
    >>> from scipy.special import zeta  # doctest: +SKIP

    `bincount` provides a fast histogram for small integers.

    >>> count = np.bincount(s)
    >>> k = np.arange(1, s.max() + 1)

    >>> plt.bar(k, count[1:], alpha=0.5, label='sample count')
    >>> plt.plot(k, n*(k**-a)/zeta(a), 'k.-', alpha=0.5,
    ...          label='expected count')   # doctest: +SKIP
    >>> plt.semilogy()
    >>> plt.grid(alpha=0.4)
    >>> plt.legend()
    >>> plt.title(f'Zipf sample, a={a}, size={n}')
    >>> plt.show()


    """
    a = params.get("a", 0.0)
    size = params.get("size", "dc[0].y.shape")

    out = np.random.zipf(float(a), size=eval(size))

    return DataContainer(x=dc[0].y, y=out)
