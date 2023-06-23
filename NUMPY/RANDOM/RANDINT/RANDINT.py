import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def RANDINT(dc: list, params: dict) -> DataContainer:
    """
    Random integers from `low` (inclusive) to `high` (exclusive).

    Return random integers from the "discrete uniform" distribution in the
    "half-open" interval [`low`, `high`). If `high` is None (the default),
    then results are from [0, `low`).


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    low : int or array-like of ints
        Lowest (signed) integers to be drawn from the distribution (unless
        ``high=None``, in which case this parameter is one above the
        *highest* such integer).
    high : int or array-like of ints, optional
        If provided, one above the largest (signed) integer to be drawn
        from the distribution (see above for behavior if ``high=None``).
        If array-like, must contain integer values
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.
    dtype : dtype, optional
        Desired dtype of the result. Byteorder must be native.
        The default value is int.

        .. versionadded:: 1.11.0

    Returns
    -------
    out : int or ndarray of ints
        `size`-shaped array of random integers from the appropriate
        distribution, or a single such random int if `size` not provided.

    See Also
    --------
    random_integers : similar to `randint`, only for the closed
        interval [`low`, `high`], and 1 is the lowest value if `high` is
        omitted.
    random.Generator.integers: which should be used for new code.

    Examples
    --------
    >>> np.random.randint(2, size=10)
    array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0]) # random
    >>> np.random.randint(1, size=10)
    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    Generate a 2 x 4 array of ints between 0 and 4, inclusive:

    >>> np.random.randint(5, size=(2, 4))
    array([[4, 0, 2, 1], # random
            [3, 2, 2, 0]])

    Generate a 1 x 3 array with 3 different upper bounds

    >>> np.random.randint(1, [3, 5, 10])
    array([2, 2, 9]) # random

    Generate a 1 by 3 array with 3 different lower bounds

    >>> np.random.randint([1, 5, 7], 10)
    array([9, 8, 7]) # random

    Generate a 2 by 4 array using broadcasting with dtype of uint8

    >>> np.random.randint([1, 3, 5, 7], [[10], [20]], dtype=np.uint8)
    array([[ 8,  6,  9,  7], # random
            [ 1, 16,  9, 12]], dtype=uint8)

    """
    low = params.get("low", 0)
    high = params.get("high", 100)
    size = params.get("size", "dc[0].y.shape")
    out = np.random.randint(float(low), float(high), size=eval(size))
    return DataContainer(x=dc[0].y, y=out)
