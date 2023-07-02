from flojoy import DataContainer, flojoy
import numpy.linalg


@flojoy
def EIGVALSH(default: DataContainer, UPLO: str = "L"):
    """

            Compute the eigenvalues of a complex Hermitian or real symmetric matrix.

    Main difference from eigh: the eigenvectors are not computed.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    a : (..., M, M) array_like
            A complex- or real-valued matrix whose eigenvalues are to be
            computed.
    UPLO : {'L', 'U'}, optional
            Specifies whether the calculation is done with the lower triangular
            part of `a` ('L', default) or the upper triangular part ('U').
            Irrespective of this value only the real parts of the diagonal will
            be considered in the computation to preserve the notion of a Hermitian
            matrix. It therefore follows that the imaginary part of the diagonal
            will always be treated as zero.
    """
    return DataContainer(
        x=dc[0].y,
        y=numpy.linalg.eigvalsh(
            a=dc[0].y, UPLO=str(params["UPLO"]) if params["UPLO"] != "" else None
        ),
    )
