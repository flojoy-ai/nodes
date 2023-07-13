from flojoy import OrderedPair, flojoy
import scipy.signal


@flojoy(node_type='default')
def QUADRATIC(
	default: OrderedPair,
	) -> OrderedPair:
	'''
		A quadratic B-spline.
		
		This is a special case of `bspline`, and equivalent to ``bspline(x, 2)``.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	x : array_like
		a knot vector
			'''
	result = OrderedPair(
		x=default.x,
		y=scipy.signal.quadratic(
			x=default.y,
			)
	)
	return result
