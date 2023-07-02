from flojoy import DataContainer, flojoy
import numpy.linalg


@flojoy
def QR(default: DataContainer, mode: str = "reduced"):
    """

            Compute the qr factorization of a matrix.

            Factor the matrix `a` as *qr*, where `q` is orthonormal and `r` is
            upper-triangular.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    a : array_like, shape (..., M, N)
            An array-like object with the dimensionality of at least 2.
    mode : {'reduced', 'complete', 'r', 'raw'}, optional
            If K = min(M, N), then

    * 'reduced'  : returns q, r with dimensions
            (..., M, K), (..., K, N) (default)
    * 'complete' : returns q, r with dimensions (..., M, M), (..., M, N)
    * 'r'        : returns r only with dimensions (..., K, N)
    * 'raw'      : returns h, tau with dimensions (..., N, M), (..., K,)

            The options 'reduced', 'complete, and 'raw' are new in numpy 1.8,
            see the notes for more information. The default is 'reduced', and to
            maintain backward compatibility with earlier versions of numpy both
            it and the old default 'full' can be omitted. Note that array h
            returned in 'raw' mode is transposed for calling Fortran. The
            'economic' mode is deprecated.  The modes 'full' and 'economic' may
            be passed using only the first letter for backwards compatibility,
            but all others must be spelled out. See the Notes for more
            explanation.

    """
    return DataContainer(
        x=dc[0].y,
        y=numpy.linalg.qr(
            a=dc[0].y, mode=str(params["mode"]) if params["mode"] != "" else None
        ),
    )
