from flojoy import OrderedPair, flojoy
import numpy.linalg


@flojoy(node_type='default')
def EIGVALS(
	default: OrderedPair,
	) -> OrderedPair:
	'''
		
		Compute the eigenvalues of a general matrix.
		
	Main difference between `eigvals` and `eig`: the eigenvectors aren't
		returned.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : (..., M, M) array_like
		A complex- or real-valued matrix whose eigenvalues will be computed.
			'''
	result = OrderedPair(
		x=default.x,
		y=numpy.linalg.eigvals(
			a=default.y,
			)
	)
	return result
