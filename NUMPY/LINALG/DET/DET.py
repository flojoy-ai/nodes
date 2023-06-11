from flojoy import DataContainer, flojoy
import numpy.linalg

@flojoy
def DET(dc, params):
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
	return DataContainer(
		x=dc[0].y,
		y=numpy.linalg.det(
			a=dc[0].y,
			)
	)

