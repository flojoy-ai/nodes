from flojoy import DataContainer, flojoy, DefaultParams
import numpy.linalg


@flojoy
def SVD(
    default: DataContainer,
    default_params: DefaultParams,
    full_matrices: bool = True,
    compute_uv: bool = True,
    hermitian: bool = False,
):
    """

            Singular Value Decomposition.

            When `a` is a 2D array, and ``full_matrices=False``, then it is
            factorized as ``u @ np.diag(s) @ vh = (u * s) @ vh``, where
            `u` and the Hermitian transpose of `vh` are 2D arrays with
            orthonormal columns and `s` is a 1D array of `a`'s singular
            values. When `a` is higher-dimensional, SVD is applied in
            stacked mode as explained below.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    a : (..., M, N) array_like
            A real or complex array with ``a.ndim >= 2``.
    full_matrices : bool, optional
            If True (default), `u` and `vh` have the shapes ``(..., M, M)`` and
            ``(..., N, N)``, respectively.  Otherwise, the shapes are
            ``(..., M, K)`` and ``(..., K, N)``, respectively, where
            ``K = min(M, N)``.
    compute_uv : bool, optional
            Whether or not to compute `u` and `vh` in addition to `s`.  True
            by default.
    hermitian : bool, optional
            If True, `a` is assumed to be Hermitian (symmetric if real-valued),
            enabling a more efficient method for finding singular values.
            Defaults to False.

    .. versionadded:: 1.17.0
    """
    return DataContainer(
        x=dc[0].y,
        y=numpy.linalg.svd(
            a=dc[0].y,
            full_matrices=bool(params["full_matrices"])
            if params["full_matrices"] != ""
            else None,
            compute_uv=bool(params["compute_uv"])
            if params["compute_uv"] != ""
            else None,
            hermitian=bool(params["hermitian"]) if params["hermitian"] != "" else None,
        ),
    )
