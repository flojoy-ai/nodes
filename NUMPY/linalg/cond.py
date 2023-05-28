from flojoy import DataContainer, flojoy
import numpy.linalg

@flojoy
def COND(dc, params):
	'''
		
		Compute the condition number of a matrix.
		
		This function is capable of returning the condition number using
		one of seven different norms, depending on the value of `p` (see
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters below).
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	x : (..., M, N) array_like
		The matrix whose condition number is sought.
	p : {None, 1, -1, 2, -2, inf, -inf, 'fro'}, optional
	Order of the norm used in the condition number computation:
		
		=====  ============================
		p      norm for matrices
		=====  ============================
		None   2-norm, computed directly using the ``SVD``
		'fro'  Frobenius norm
		inf    max(sum(abs(x), axis=1))
		-inf   min(sum(abs(x), axis=1))
		1      max(sum(abs(x), axis=0))
		-1     min(sum(abs(x), axis=0))
		2      2-norm (largest sing. value)
		-2     smallest singular value
		=====  ============================
		
		inf means the `numpy.inf` object, and the Frobenius norm is
		the root-of-sum-of-squares norm.
			'''
	return DataContainer(
		m=numpy.linalg.cond(
			x=dc[0].y,
			p=(None(params['p']) if params['p'] != '' else None),
		)
	)

