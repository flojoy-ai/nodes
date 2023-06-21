import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List


@flojoy
def RANDN(dc: list, params: dict) -> DataContainer:
    """
    Return a sample (or samples) from the "standard normal" distribution.

    If dc[0].y is a float, a single float is returned.
    If dc[0].y is a tuple, a tuple of floats is returned.


    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    Parameters
    ----------
    d0, d1, ..., dn : int, optional
        The dimensions of the returned array, must be non-negative.
        If no argument is given a single Python float is returned.

    Returns
    -------
    Z : ndarray or float
        A ``(d0, d1, ..., dn)``-shaped array of floating-point samples from
        the standard normal distribution, or a single such float if
        no parameters were supplied.

    See Also
    --------
    standard_normal : Similar, but takes a tuple as its argument.
    normal : Also accepts mu and sigma arguments.
    random.Generator.standard_normal: which should be used for new code.

    Notes
    -----
    For random samples from :math:`N(\mu, \sigma^2)`, use:

    ``sigma * np.random.randn(...) + mu``

    Examples
    --------
    >>> np.random.randn()
    2.1923875335537315  # random

    Two-by-four array of samples from N(3, 6.25):

    >>> 3 + 2.5 * np.random.randn(2, 4)
    array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
            [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random


    """
    size = params.get("size", 'dc[0].y.shape')
    return DataContainer(
        x=dc[0].y, y=np.random.randn(size=eval(size))
    )
