from flojoy import OrderedPair, flojoy
import numpy.linalg


@flojoy(node_type="default")
def DET(
    default: OrderedPair,
) -> OrderedPair:
    """The DET node is based on a numpy or scipy function.
    The description of that function is as follows:


            Compute the determinant of an array.

    Parameters
    ----------
    a : (..., M, M) array_like
            Input array to compute determinants for.

    Returns
    ----------
    DataContainer:
            type 'ordered pair'"""
    result = OrderedPair(
        x=default.x,
        y=numpy.linalg.det(
            a=default.y,
        ),
    )
    return result
