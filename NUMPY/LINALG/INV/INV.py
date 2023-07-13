from flojoy import OrderedPair, flojoy
import numpy.linalg


@flojoy(node_type='default')
def INV(
	default: OrderedPair,
	) -> OrderedPair:
	'''
		
		Compute the (multiplicative) inverse of a matrix.
		
		Given a square matrix `a`, return the matrix `ainv` satisfying
		``dot(a, ainv) = dot(ainv, a) = eye(a.shape[0])``.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : (..., M, M) array_like
		Matrix to be inverted.
			'''
	result = OrderedPair(
		x=default.x,
		y=numpy.linalg.inv(
			a=default.y,
			)
	)
	return result
