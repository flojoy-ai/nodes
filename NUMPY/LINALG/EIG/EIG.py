from flojoy import OrderedPair, flojoy
import numpy.linalg


@flojoy(node_type='default')
def EIG(
	default: OrderedPair,
	) -> OrderedPair:
	'''
		
		Compute the eigenvalues and right eigenvectors of a square array.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : (..., M, M) array
		Matrices for which the eigenvalues and right eigenvectors will
		be computed
			'''
	result = OrderedPair(
		x=default.x,
		y=numpy.linalg.eig(
			a=default.y,
			)
	)
	return result
