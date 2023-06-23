import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def NONCENTRAL_CHISQUARE(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from a noncentral chi-square distribution.

    The noncentral :math:`\chi^2` distribution is a generalisation of
    the :math:`\chi^2` distribution. It is used to model the sum of
    independent chi-square variables, each with different degrees of
    freedom, but the same non-centrality parameter.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    df : float or array_like of floats
        Degrees of freedom, must be > 0.

        .. versionchanged:: 1.10.0
            Earlier NumPy versions required dfnum > 1.
    nonc : float or array_like of floats
        Non-centrality, must be non-negative.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``df`` and ``nonc`` are both scalars.
        Otherwise, ``np.broadcast(df, nonc).size`` samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized noncentral chi-square distribution.

    See Also
    --------
    random.Generator.noncentral_chisquare: which should be used for new code.

    Notes
    -----
    The probability density function for the noncentral Chi-square
    distribution is

    .. math:: P(x;df,nonc) = \sum^{\infty}_{i=0}
                            \frac{e^{-nonc/2}(nonc/2)^{i}}{i!}
                            P_{Y_{df+2i}}(x),

    where :math:`Y_{q}` is the Chi-square with q degrees of freedom.

    References
    ----------
    .. [1] Wikipedia, "Noncentral chi-squared distribution"
            https://en.wikipedia.org/wiki/Noncentral_chi-squared_distribution

    Examples
    --------
    Draw values from the distribution and plot the histogram

    >>> import matplotlib.pyplot as plt
    >>> values = plt.hist(np.random.noncentral_chisquare(3, 20, 100000),
    ...                   bins=200, density=True)
    >>> plt.show()

    Draw values from a noncentral chisquare with very small noncentrality,
    and compare to a chisquare.

    >>> plt.figure()
    >>> values = plt.hist(np.random.noncentral_chisquare(3, .0000001, 100000),
    ...                   bins=np.arange(0., 25, .1), density=True)
    >>> values2 = plt.hist(np.random.chisquare(3, 100000),
    ...                    bins=np.arange(0., 25, .1), density=True)
    >>> plt.plot(values[1][0:-1], values[0]-values2[0], 'ob')
    >>> plt.show()

    Demonstrate how large values of non-centrality lead to a more symmetric
    distribution.

    >>> plt.figure()
    >>> values = plt.hist(np.random.noncentral_chisquare(3, 20, 100000),
    ...                   bins=200, density=True)
    >>> plt.show()


    """
    df: float = params.get("df", 2)
    nonc: float = params.get("nonc", 0.0)
    size: tuple = params.get("size", 'dc[0].y.shape')

    if df < 0.0 or nonc < 0.0:
        raise ValueError("df and nonc must be greater than or equal to 0.")

    out = np.random.noncentral_chisquare(float(df), float(nonc), size=eval(size)) 
    return DataContainer(x=dc[0].y, y=out)
