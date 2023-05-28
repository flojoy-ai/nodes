from flojoy import DataContainer, flojoy
import numpy.linalg

@flojoy
def CHOLESKY(dc, params):
	'''
		
		Cholesky decomposition.
		
		Return the Cholesky decomposition, `L * L.H`, of the square matrix `a`,
		where `L` is lower-triangular and .H is the conjugate transpose operator
		(which is the ordinary transpose if `a` is real-valued).  `a` must be
		Hermitian (symmetric if real-valued) and positive-definite. No
		checking is performed to verify whether `a` is Hermitian or not.
		In addition, only the lower-triangular and diagonal elements of `a`
		are used. Only `L` is actually returned.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : (..., M, M) array_like
		Hermitian (symmetric if all elements are real), positive-definite
		input matrix.
			'''
	return DataContainer(
		m=numpy.linalg.cholesky(
			a=dc[0].y,
			)
	)

