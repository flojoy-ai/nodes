from flojoy import DataContainer, flojoy
import numpy.linalg

@flojoy
def PINV(dc, params):
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
	return DataContainer(
		m=numpy.linalg.pinv(
			a=dc[0].y,
			rcond=(float(params['rcond']) if params['rcond'] != '' else None),
			hermitian=(bool(params['hermitian']) if params['hermitian'] != '' else None),
		)
	)

