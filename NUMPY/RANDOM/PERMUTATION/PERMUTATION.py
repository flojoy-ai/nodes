import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def PERMUTATION(dc: list, params: dict) -> DataContainer:
    """
    Randomly permute a sequence, or return a permuted range.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    x : int or array_like
        If `x` is an integer, randomly permute ``np.arange(x)``.
        If `x` is an array, make a copy and shuffle the elements
        randomly.

    Returns
    -------
    out : ndarray
        Permuted sequence or array range.

    See Also
    --------
    random.Generator.permutation: which should be used for new code.

    Examples
    --------
    >>> np.random.permutation(10)
    array([1, 7, 4, 3, 0, 9, 2, 5, 8, 6]) # random

    >>> np.random.permutation([1, 4, 9, 12, 15])
    array([15,  1,  9,  4, 12]) # random

    >>> arr = np.arange(9).reshape((3, 3))
    >>> np.random.permutation(arr)
    array([[6, 7, 8], # random
            [0, 1, 2],
            [3, 4, 5]])


    """
    return DataContainer(x=dc[0].y, y=np.random.permutation(dc[0].y))
