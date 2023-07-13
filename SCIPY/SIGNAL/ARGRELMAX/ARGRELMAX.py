from flojoy import OrderedPair, flojoy
import scipy.signal


@flojoy(node_type='default')
def ARGRELMAX(
	default: OrderedPair,
	axis: int = 0,
	order: int = 1,
	mode: str = 'clip',
	) -> OrderedPair:
	'''
		
		Calculate the relative maxima of `data`.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	data : ndarray
		Array in which to find the relative maxima.
	axis : int, optional
		Axis over which to select from `data`. Default is 0.
	order : int, optional
		How many points on each side to use for the comparison
		to consider ``comparator(n, n+x)`` to be True.
	mode : str, optional
		How the edges of the vector are treated.
		Available options are 'wrap' (wrap around) or 'clip' (treat overflow
		as the same as the last (or first) element).
		Default 'clip'. See `numpy.take`.
			'''
	result = OrderedPair(
		x=default.x,
		y=scipy.signal.argrelmax(
			data=default.y,
			axis=axis,
			order=order,
			mode=mode,
		)
	)
	return result
