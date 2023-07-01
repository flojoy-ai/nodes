from flojoy import DataContainer, flojoy, DefaultParams
import numpy.linalg


@flojoy
def EIGH(default: DataContainer, default_params: DefaultParams, UPLO: str = "L"):
    """

    Return the eigenvalues and eigenvectors of a complex Hermitian
    (conjugate symmetric) or a real symmetric matrix.
    """
    return DataContainer(
        x=dc[0].y,
        y=numpy.linalg.eigh(
            a=dc[0].y, UPLO=str(params["UPLO"]) if params["UPLO"] != "" else None
        ),
    )
