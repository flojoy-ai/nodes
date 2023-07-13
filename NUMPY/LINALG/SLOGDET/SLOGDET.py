from flojoy import OrderedPair, flojoy
import numpy.linalg


@flojoy(node_type='default')
def SLOGDET(
	default: OrderedPair,
	) -> OrderedPair:
	'''
		
		Compute the sign and (natural) logarithm of the determinant of an array.
		
		If an array has a very small or very large determinant, then a call to
		`det` may overflow or underflow. This routine is more robust against such
		issues, because it computes the logarithm of the determinant rather than
		the determinant itself.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : (..., M, M) array_like
		Input array, has to be a square 2-D array.
			'''
	result = OrderedPair(
		x=default.x,
		y=numpy.linalg.slogdet(
			a=default.y,
			)
	)
	return result
