from flojoy import DataContainer, flojoy, DefaultParams
import numpy.linalg

@flojoy
def MATRIX_POWER(default: DataContainer, default_parmas: DefaultParams, n: int=None):
    """

            Raise a square matrix to the (integer) power `n`.

            For positive integers `n`, the power is computed by repeated matrix
            squarings and matrix multiplications. If ``n == 0``, the identity matrix
            of the same shape as M is returned. If ``n < 0``, the inverse
            is computed and then raised to the ``abs(n)``.

    .. note:: Stacks of object matrices are not currently supported.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    a : (..., M, M) array_like
            Matrix to be "powered".
    n : int
            The exponent can be any integer or long integer, positive,
            negative, or zero.
    """
    return DataContainer(x=dc[0].y, y=numpy.linalg.matrix_power(a=dc[0].y, n=int(params['n']) if params['n'] != '' else None))