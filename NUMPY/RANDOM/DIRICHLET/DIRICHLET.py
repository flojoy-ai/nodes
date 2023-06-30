import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def DIRICHLET(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from the Dirichlet distribution.

    Draw `dc[0].y` samples from a Dirichlet distribution. The Dirichlet
    distribution is a multivariate generalization of the beta distribution.
    It is a distribution over probability vectors, i.e. vectors that sum to
    1.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    alpha : sequence of floats, length k
        Parameter of the distribution (length ``k`` for sample of
        length ``k``).
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        vector of length ``k`` is returned.

    Returns
    -------
    samples : ndarray,
        The drawn samples, of shape ``(size, k)``.

    Raises
    ------
    ValueError
        If any value in ``alpha`` is less than or equal to zero

    See Also
    --------
    random.Generator.dirichlet: which should be used for new code.

    Notes
    -----
    The Dirichlet distribution is a distribution over vectors
    :math:`x` that fulfil the conditions :math:`x_i>0` and
    :math:`\sum_{i=1}^k x_i = 1`.

    The probability density function :math:`p` of a
    Dirichlet-distributed random vector :math:`X` is
    proportional to

    .. math:: p(x) \propto \prod_{i=1}^{k}{x^{\alpha_i-1}_i},

    where :math:`\alpha` is a vector containing the positive
    concentration parameters.

    The method uses the following property for computation: let :math:`Y`
    be a random vector which has components that follow a standard gamma
    distribution, then :math:`X = \frac{1}{\sum_{i=1}^k{Y_i}} Y`
    is Dirichlet-distributed

    References
    ----------
    .. [1] David McKay, "Information Theory, Inference and Learning
            Algorithms," chapter 23,
            http://www.inference.org.uk/mackay/itila/
    .. [2] Wikipedia, "Dirichlet distribution",
            https://en.wikipedia.org/wiki/Dirichlet_distribution

    Examples
    --------
    Taking an example cited in Wikipedia, this distribution can be used if
    one wanted to cut strings (each of initial length 1.0) into K pieces
    with different lengths, where each piece had, on average, a designated
    average length, but allowing some variation in the relative sizes of
    the pieces.

    >>> s = np.random.dirichlet((10, 5, 3), 20).transpose()

    >>> import matplotlib.pyplot as plt
    >>> plt.barh(range(20), s[0])
    >>> plt.barh(range(20), s[1], left=s[0], color='g')
    >>> plt.barh(range(20), s[2], left=s[0]+s[1], color='r')
    >>> plt.title("Lengths of Strings")


    """
    size: str = params.get("size", "dc[0].y.shape")
    out = np.random.dirichlet(alpha=dc[0].y, size=eval(size))
    return DataContainer(x=dc[0].y, y=out)
