from flojoy import OrderedPair, flojoy
import numpy.linalg


@flojoy(node_type="default")
def EIGH(
    default: OrderedPair,
    UPLO: str = "L",
) -> OrderedPair:
    """The EIGH node is based on a numpy or scipy function.
    The description of that function is as follows:


            Return the eigenvalues and eigenvectors of a complex Hermitian
            (conjugate symmetric) or a real symmetric matrix.

    Returns
    ----------
    DataContainer:
            type 'ordered pair'"""
    result = OrderedPair(
        x=default.x,
        y=numpy.linalg.eigh(
            a=default.y,
            UPLO=UPLO,
        ),
    )
    return result
