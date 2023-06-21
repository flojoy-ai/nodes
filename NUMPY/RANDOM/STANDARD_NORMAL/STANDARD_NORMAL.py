import numpy as np
from flojoy import flojoy, DataContainer
from typing import Optional, Union, Tuple, List
@flojoy


def STANDARD_NORMAL(dc: list, params: dict) -> DataContainer:
    """
    Draw random samples from a normal (Gaussian) distribution.
    
    The probability density function of the normal distribution, first
    derived by De Moivre and 200 years later by both Gauss and Laplace
    independently [2]_, is often called the bell curve because of
    its characteristic shape (see the example below).
    
    
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
    out : float or ndarray
        A floating-point array of shape ``size`` of drawn samples, or a
        single sample if ``size`` was not specified.

    See Also
    --------
    normal :
        Equivalent function with additional ``loc`` and ``scale`` arguments
        for setting the mean and standard deviation.
    random.Generator.standard_normal: which should be used for new code.

    Notes
    -----
    For random samples from :math:`N(\mu, \sigma^2)`, use one of::

        mu + sigma * np.random.standard_normal(size=...)
        np.random.normal(mu, sigma, size=...)

    Examples
    --------
    >>> np.random.standard_normal()
    2.1923875335537315 #random

    >>> s = np.random.standard_normal(8000)
    >>> s
    array([ 0.6888893 ,  0.78096262, -0.89086505, ...,  0.49876311,  # random
            -0.38672696, -0.4685006 ])                                # random
    >>> s.shape
    (8000,)
    >>> s = np.random.standard_normal(size=(3, 4, 2))
    >>> s.shape
    (3, 4, 2)

    Two-by-four array of samples from :math:`N(3, 6.25)`:

    >>> 3 + 2.5 * np.random.standard_normal(size=(2, 4))
    array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
            [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random

    
    """
    size = params.get("size", 'dc[0].y.shape')
    out = np.random.standard_normal(size=eval(size))
    
    return DataContainer(x=dc[0].y, y=out)