from flojoy import OrderedPair, flojoy
import numpy.linalg


@flojoy(node_type='default')
def MATRIX_POWER(
	default: OrderedPair,
	n: int,
	) -> OrderedPair:
	'''
		
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
			'''
	result = OrderedPair(
		x=default.x,
		y=numpy.linalg.matrix_power(
			a=default.y,
			n=n,
		)
	)
	return result
