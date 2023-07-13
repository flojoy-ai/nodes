from flojoy import OrderedPair, flojoy
import scipy.signal


@flojoy(node_type='default')
def CUBIC(
	default: OrderedPair,
	) -> OrderedPair:
	'''
		A cubic B-spline.
		
		This is a special case of `bspline`, and equivalent to ``bspline(x, 3)``.
		
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
		y=scipy.signal.cubic(
			x=default.y,
			)
	)
	return result
