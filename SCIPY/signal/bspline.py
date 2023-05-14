from flojoy import DataContainer, flojoy
import scipy.signal

@flojoy
def BSPLINE(dc, params):
	'''
		B-spline basis function of order n.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	x : array_like
		a knot vector
	n : int
		The order of the spline. Must be non-negative, i.e., n >= 0
			'''
	return DataContainer(
		x=dc[0].y,
		y=scipy.signal.bspline(
			x=dc[0].y,
			n=(int(params['n']) if params['n'] != '' else None),
		)
	)

