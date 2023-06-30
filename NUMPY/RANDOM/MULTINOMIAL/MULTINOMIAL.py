import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def MULTINOMIAL(dc: list, params: dict) -> DataContainer:
    """
    Draw samples from a multinomial distribution.

    The multinomial distribution is a multivariate generalization of the binomial
    distribution. Take an n-dimensional vector `p` of probabilities, and sample
    `n` independent times from each of the `n` categories. The multinomial
    distribution describes the probability of counts among the categories.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    n : int
        Number of experiments.
    pvals : sequence of floats, length p
        Probabilities of each of the ``p`` different outcomes.  These
        must sum to 1 (however, the last element is always assumed to
        account for the remaining probability, as long as
        ``sum(pvals[:-1]) <= 1)``.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    out : ndarray
        The drawn samples, of shape *size*, if that was provided.  If not,
        the shape is ``(N,)``.

        In other words, each entry ``out[i,j,...,:]`` is an N-dimensional
        value drawn from the distribution.

    See Also
    --------
    random.Generator.multinomial: which should be used for new code.

    Examples
    --------
    Throw a dice 20 times:

    >>> np.random.multinomial(20, [1/6.]*6, size=1)
    array([[4, 1, 7, 5, 2, 1]]) # random

    It landed 4 times on 1, once on 2, etc.

    Now, throw the dice 20 times, and 20 times again:

    >>> np.random.multinomial(20, [1/6.]*6, size=2)
    array([[3, 4, 3, 3, 4, 3], # random
            [2, 4, 3, 4, 0, 7]])

    For the first run, we threw 3 times 1, 4 times 2, etc.  For the second,
    we threw 2 times 1, 4 times 2, etc.

    A loaded die is more likely to land on number 6:

    >>> np.random.multinomial(100, [1/7.]*5 + [2/7.])
    array([11, 16, 14, 17, 16, 26]) # random

    The probability inputs should be normalized. As an implementation
    detail, the value of the last entry is ignored and assumed to take
    up any leftover probability mass, but this should not be relied on.
    A biased coin which has twice as much weight on one side as on the
    other should be sampled like so:

    >>> np.random.multinomial(100, [1.0 / 3, 2.0 / 3])  # RIGHT
    array([38, 62]) # random

    not like:

    >>> np.random.multinomial(100, [1.0, 2.0])  # WRONG
    Traceback (most recent call last):
    ValueError: pvals < 0, pvals > 1 or pvals contains NaNs


    """
    n = params.get("n", 1)
    pvals = params.get("pvals", None)
    size = params.get("size", "dc[0].y.shape")
    out = np.random.multinomial(n=n, pvals=eval(pvals), size=eval(size))
    return DataContainer(x=dc[0].y, y=out)
