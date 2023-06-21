import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def RANDOM_SAMPLE(dc: list, params: dict) -> DataContainer:
    """
    Random values in a given shape.

    Create an array of the given shape and populate it with
    random samples from a uniform distribution
    over ``[0, 1)``.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.

    Returns
    -------
    out : float or ndarray of floats
        Array of random floats of shape `size` (unless ``size=None``, in which
        case a single float is returned).

    See Also
    --------
    random.Generator.random: which should be used for new code.

    Examples
    --------
    >>> np.random.random_sample()
    0.47108547995356098 # random
    >>> type(np.random.random_sample())
    <class 'float'>
    >>> np.random.random_sample((5,))
    array([ 0.30220482,  0.86820401,  0.1654503 ,  0.11659149,  0.54323428]) # random

    Three-by-two array of random numbers from [-5, 0):

    >>> 5 * np.random.random_sample((3, 2)) - 5
    array([[-3.99149989, -0.52338984], # random
            [-2.99091858, -0.79479508],
            [-1.23204345, -1.75224494]])


    """
    size = params.get("size", 'dc[0].y.shape')
    return DataContainer(
        x=dc[0].y, y=np.random.random_sample(size=eval(size))
    )
