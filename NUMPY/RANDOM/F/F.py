import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def F(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from an F distribution.

    Samples are drawn from an F distribution with specified parameters,
    ndarrays of the same shape as `dc[0].y` are filled with the samples.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    dfnum : float or array_like of floats
        Degrees of freedom in numerator, must be > 0.
    dfden : float or array_like of float
        Degrees of freedom in denominator, must be > 0.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``dfnum`` and ``dfden`` are both scalars.
        Otherwise, ``np.broadcast(dfnum, dfden).size`` samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized Fisher distribution.

    See Also
    --------
    scipy.stats.f : probability density function, distribution or
        cumulative density function, etc.
    random.Generator.f: which should be used for new code.

    Notes
    -----
    The F statistic is used to compare in-group variances to between-group
    variances. Calculating the distribution depends on the sampling, and
    so it is a function of the respective degrees of freedom in the
    problem.  The variable `dfnum` is the number of samples minus one, the
    between-groups degrees of freedom, while `dfden` is the within-groups
    degrees of freedom, the sum of the number of samples in each group
    minus the number of groups.

    References
    ----------
    .. [1] Glantz, Stanton A. "Primer of Biostatistics.", McGraw-Hill,
            Fifth Edition, 2002.
    .. [2] Wikipedia, "F-distribution",
            https://en.wikipedia.org/wiki/F-distribution

    Examples
    --------
    An example from Glantz[1], pp 47-40:

    Two groups, children of diabetics (25 people) and children from people
    without diabetes (25 controls). Fasting blood glucose was measured,
    case group had a mean value of 86.1, controls had a mean value of
    82.2. Standard deviations were 2.09 and 2.49 respectively. Are these
    data consistent with the null hypothesis that the parents diabetic
    status does not affect their children's blood glucose levels?
    Calculating the F statistic from the data gives a value of 36.01.

    Draw samples from the distribution:

    >>> dfnum = 1. # between group degrees of freedom
    >>> dfden = 48. # within groups degrees of freedom
    >>> s = np.random.f(dfnum, dfden, 1000)

    The lower bound for the top 1% of the samples is :

    >>> np.sort(s)[-10]
    7.61988120985 # random

    So there is about a 1% chance that the F statistic will exceed 7.62,
    the measured value is 36, so the null hypothesis is rejected at the 1%
    level.


    """
    dfn = params.get("dfn", None)
    dfd = params.get("dfd", None)
    size = params.get("size", "dc[0].y.shape")
    if dfn is None or dfd is None:
        raise ValueError("dfn and dfd must be specified in params.")
    if not isinstance(dfn, (int, np.integer)) or not isinstance(dfd, (int, np.integer)):
        raise TypeError("dfn and dfd must be integers.")
    out = np.random.f(int(dfn), int(dfd), size=eval(size))
    return DataContainer(x=dc[0].y, y=out)
