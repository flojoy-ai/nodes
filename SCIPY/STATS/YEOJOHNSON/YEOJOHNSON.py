from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np


import scipy.stats


@flojoy(node_type="default")
def YEOJOHNSON(
    default: OrderedPair | Matrix,
    lmbda: float,
) -> OrderedPair | Matrix | Scalar:
    """The YEOJOHNSON node is based on a numpy or scipy function.
    The description of that function is as follows:

            Return a dataset transformed by a Yeo-Johnson power transformation.

    Parameters
    ----------
    x : ndarray
            Input array.  Should be 1-dimensional.
    lmbda : float, optional
            If ``lmbda`` is ``None``, find the lambda that maximizes the
            log-likelihood function and return it as the second output argument.
            Otherwise the transformation is done for the given value.

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = OrderedPair(
        m=scipy.stats.yeojohnson(
            x=default.y,
            lmbda=lmbda,
        )
    )

    return result
