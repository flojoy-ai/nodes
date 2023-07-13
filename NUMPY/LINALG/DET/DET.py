from flojoy import OrderedPair, flojoy
import numpy.linalg


@flojoy(node_type='default')
def DET(
	default: OrderedPair,
	) -> OrderedPair:
	'''
		
		Compute the determinant of an array.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : (..., M, M) array_like
		Input array to compute determinants for.
			'''
	result = OrderedPair(
		x=default.x,
		y=numpy.linalg.det(
			a=default.y,
			)
	)
	return result
