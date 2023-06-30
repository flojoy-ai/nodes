import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def NONCENTRAL_F(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from the noncentral F distribution.

    Samples are drawn from an F distribution with specified parameters,
    `dfn` and `dfd`, where both parameters should be greater than zero.
    `nonc` is the non-centrality parameter.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    dfnum : float or array_like of floats
        Numerator degrees of freedom, must be > 0.

        .. versionchanged:: 1.14.0
            Earlier NumPy versions required dfnum > 1.
    dfden : float or array_like of floats
        Denominator degrees of freedom, must be > 0.
    nonc : float or array_like of floats
        Non-centrality parameter, the sum of the squares of the numerator
        means, must be >= 0.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``dfnum``, ``dfden``, and ``nonc``
        are all scalars.  Otherwise, ``np.broadcast(dfnum, dfden, nonc).size``
        samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized noncentral Fisher distribution.

    See Also
    --------
    random.Generator.noncentral_f: which should be used for new code.

    Notes
    -----
    When calculating the power of an experiment (power = probability of
    rejecting the null hypothesis when a specific alternative is true) the
    non-central F statistic becomes important.  When the null hypothesis is
    true, the F statistic follows a central F distribution. When the null
    hypothesis is not true, then it follows a non-central F statistic.

    References
    ----------
    .. [1] Weisstein, Eric W. "Noncentral F-Distribution."
            From MathWorld--A Wolfram Web Resource.
            http://mathworld.wolfram.com/NoncentralF-Distribution.html
    .. [2] Wikipedia, "Noncentral F-distribution",
            https://en.wikipedia.org/wiki/Noncentral_F-distribution

    Examples
    --------
    In a study, testing for a specific alternative to the null hypothesis
    requires use of the Noncentral F distribution. We need to calculate the
    area in the tail of the distribution that exceeds the value of the F
    distribution for the null hypothesis.  We'll plot the two probability
    distributions for comparison.

    >>> dfnum = 3 # between group deg of freedom
    >>> dfden = 20 # within groups degrees of freedom
    >>> nonc = 3.0
    >>> nc_vals = np.random.noncentral_f(dfnum, dfden, nonc, 1000000)
    >>> NF = np.histogram(nc_vals, bins=50, density=True)
    >>> c_vals = np.random.f(dfnum, dfden, 1000000)
    >>> F = np.histogram(c_vals, bins=50, density=True)
    >>> import matplotlib.pyplot as plt
    >>> plt.plot(F[1][1:], F[0])
    >>> plt.plot(NF[1][1:], NF[0])
    >>> plt.show()


    """
    dfn = params.get("dfn", None)
    dfd = params.get("dfd", None)
    nonc = params.get("nonc", None)
    size = params.get("size", "dc[0].y.shape")
    if dfn is None or dfd is None or nonc is None:
        raise ValueError("dfn, dfd, and nonc must all be specified.")

    if float(dfn) <= 0 or float(dfd) <= 0 or float(nonc) < 0:
        raise ValueError(
            "float(dfn), float(dfd), and float(nonc) must all be greater than zero."
        )
    out = np.random.noncentral_f(float(dfn), float(dfd), float(nonc), size=eval(size))
    return DataContainer(x=dc[0].y, y=out)
