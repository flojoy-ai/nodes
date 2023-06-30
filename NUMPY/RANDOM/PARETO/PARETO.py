import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def PARETO(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from a Pareto II or Lomax distribution with specified shape.

    The Lomax or Pareto II distribution is a shifted Pareto
    distribution. The classical Pareto distribution can be obtained
    from the Lomax distribution by adding 1 and multiplying by the
    scale parameter m.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    a : float or array_like of floats
        Shape of the distribution. Must be positive.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``a`` is a scalar.  Otherwise,
        ``np.array(a).size`` samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized Pareto distribution.

    See Also
    --------
    scipy.stats.lomax : probability density function, distribution or
        cumulative density function, etc.
    scipy.stats.genpareto : probability density function, distribution or
        cumulative density function, etc.
    random.Generator.pareto: which should be used for new code.

    Notes
    -----
    The probability density for the Pareto distribution is

    .. math:: p(x) = \frac{am^a}{x^{a+1}}

    where :math:`a` is the shape and :math:`m` the scale.

    The Pareto distribution, named after the Italian economist
    Vilfredo Pareto, is a power law probability distribution
    useful in many real world problems.  Outside the field of
    economics it is generally referred to as the Bradford
    distribution. Pareto developed the distribution to describe
    the distribution of wealth in an economy.  It has also found
    use in insurance, web page access statistics, oil field sizes,
    and many other problems, including the download frequency for
    projects in Sourceforge [1]_.  It is one of the so-called
    "fat-tailed" distributions.

    References
    ----------
    .. [1] Francis Hunt and Paul Johnson, On the Pareto Distribution of
            Sourceforge projects.
    .. [2] Pareto, V. (1896). Course of Political Economy. Lausanne.
    .. [3] Reiss, R.D., Thomas, M.(2001), Statistical Analysis of Extreme
            Values, Birkhauser Verlag, Basel, pp 23-30.
    .. [4] Wikipedia, "Pareto distribution",
            https://en.wikipedia.org/wiki/Pareto_distribution

    Examples
    --------
    Draw samples from the distribution:

    >>> a, m = 3., 2.  # shape and mode
    >>> s = (np.random.pareto(a, 1000) + 1) * m

    Display the histogram of the samples, along with the probability
    density function:

    >>> import matplotlib.pyplot as plt
    >>> count, bins, _ = plt.hist(s, 100, density=True)
    >>> fit = a*m**a / bins**(a+1)
    >>> plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='r')
    >>> plt.show()


    """
    # Strictly type all internal variables
    size: str = params.get("size", "dc[0].y.shape")
    a = params.get("a", 1.0)

    # Draw samples from the Pareto II or Lomax distribution
    out = np.random.pareto(a=float(a), size=eval(size))
    return DataContainer(x=dc[0].y, y=out)
