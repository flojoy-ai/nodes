from flojoy import OrderedPair, flojoy
import scipy.signal


@flojoy(node_type='default')
def GAUSS_SPLINE(
	default: OrderedPair,
	n: int,
	) -> OrderedPair:
	'''
		Gaussian approximation to B-spline basis function of order n.
		
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
	result = OrderedPair(
		x=default.x,
		y=scipy.signal.gauss_spline(
			x=default.y,
			n=n,
		)
	)
	return result
