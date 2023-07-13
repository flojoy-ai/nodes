from flojoy import OrderedPair, flojoy
import numpy.linalg


@flojoy(node_type='default')
def TENSORINV(
	default: OrderedPair,
	ind: int = 2,
	) -> OrderedPair:
	'''
		
		Compute the 'inverse' of an N-dimensional array.
		
		The result is an inverse for `a` relative to the tensordot operation
		``tensordot(a, b, ind)``, i. e., up to floating-point accuracy,
		``tensordot(tensorinv(a), a, ind)`` is the "identity" tensor for the
		tensordot operation.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : array_like
		Tensor to 'invert'. Its shape must be 'square', i. e.,
	``prod(a.shape[:ind]) == prod(a.shape[ind:])``.
	ind : int, optional
		Number of first indices that are involved in the inverse sum.
		Must be a positive integer, default is 2.
			'''
	result = OrderedPair(
		x=default.x,
		y=numpy.linalg.tensorinv(
			a=default.y,
			ind=ind,
		)
	)
	return result
