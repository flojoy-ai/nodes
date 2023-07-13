from flojoy import OrderedPair, flojoy
import numpy.linalg


@flojoy(node_type='default')
def PINV(
	default: OrderedPair,
	rcond: float = 1e-15,
	hermitian: bool = False,
	) -> OrderedPair:
	'''
		
		Compute the (Moore-Penrose) pseudo-inverse of a matrix.
		
		Calculate the generalized inverse of a matrix using its
		singular-value decomposition (SVD) and including all
		*large* singular values.
		
	.. versionchanged:: 1.14
		Can now operate on stacks of matrices
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : (..., M, N) array_like
		Matrix or stack of matrices to be pseudo-inverted.
	rcond : (...) array_like of float
		Cutoff for small singular values.
		Singular values less than or equal to
		``rcond * largest_singular_value`` are set to zero.
		Broadcasts against the stack of matrices.
	hermitian : bool, optional
		If True, `a` is assumed to be Hermitian (symmetric if real-valued),
		enabling a more efficient method for finding singular values.
		Defaults to False.
		
	.. versionadded:: 1.17.0
			'''
	result = OrderedPair(
		x=default.x,
		y=numpy.linalg.pinv(
			a=default.y,
			rcond=rcond,
			hermitian=hermitian,
		)
	)
	return result
