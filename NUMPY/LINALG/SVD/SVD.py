from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np
from collections import namedtuple
from typing import Literal

import numpy.linalg


@flojoy(node_type="default")
def SVD(
    default: OrderedPair | Matrix,
    full_matrices: bool = True,
    compute_uv: bool = True,
    hermitian: bool = False,
    select_return: Literal["u", "s", "vh"] = "u",
) -> OrderedPair | Matrix | Scalar:
    """The SVD node is based on a numpy or scipy function.
    The description of that function is as follows:


            Singular Value Decomposition.

            When `a` is a 2D array, and ``full_matrices=False``, then it is
            factorized as ``u @ np.diag(s) @ vh = (u * s) @ vh``, where
            `u` and the Hermitian transpose of `vh` are 2D arrays with
            orthonormal columns and `s` is a 1D array of `a`'s singular
            values. When `a` is higher-dimensional, SVD is applied in
            stacked mode as explained below.

    Parameters
    ----------
    select_return : This function has returns multiple Objects:
            ['u', 's', 'vh']. Select the desired one to return.
            See the respective function docs for descriptors.
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

    Returns
    ----------
    DataContainer:
            type 'ordered pair', 'scalar', or 'matrix'
    """

    result = numpy.linalg.svd(
        a=default.m,
        full_matrices=full_matrices,
        compute_uv=compute_uv,
        hermitian=hermitian,
    )

    if type(result) == namedtuple:
        result = result._asdict()
        result = result[select_return]

    if type(result) == np.ndarray:
        result = Matrix(m=result)
    elif type(result) == np.float64:
        result = Scalar(c=result)

    return result
