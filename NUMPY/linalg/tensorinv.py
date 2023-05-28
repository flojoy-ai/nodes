from flojoy import DataContainer, flojoy
import numpy.linalg

@flojoy
def TENSORINV(dc, params):
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
	return DataContainer(
		m=numpy.linalg.tensorinv(
			a=dc[0].y,
			ind=(int(params['ind']) if params['ind'] != '' else None),
		)
	)

