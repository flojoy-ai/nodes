from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np


import numpy.linalg


@flojoy(node_type='default')
def SLOGDET(
	default: OrderedPair | Matrix,
	) -> OrderedPair | Matrix | Scalar:
	'''The SLOGDET node is based on a numpy or scipy function.
	The description of that function is as follows:

		
		Compute the sign and (natural) logarithm of the determinant of an array.
		
		If an array has a very small or very large determinant, then a call to
		`det` may overflow or underflow. This routine is more robust against such
		issues, because it computes the logarithm of the determinant rather than
		the determinant itself.
		
	Parameters
	----------
	a : (..., M, M) array_like
		Input array, has to be a square 2-D array.

	Returns
	----------
	DataContainer:
		type 'ordered pair', 'scalar', or 'matrix'
	'''

	result = numpy.linalg.slogdet(
			a=default.m,
			)

	if type(result) == np.ndarray:
		result = Matrix(m=result)
	
	elif type(result) == np.float64:
		result = Scalar(c=result)
	
	return result
