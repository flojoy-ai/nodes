from flojoy import OrderedPair, flojoy
import scipy.stats


@flojoy(node_type='default')
def SIGMACLIP(
	default: OrderedPair,
	low: float = 4.0,
	high: float = 4.0,
	) -> OrderedPair:
	'''
		Perform iterative sigma-clipping of array elements.
		
		Starting from the full sample, all elements outside the critical range are
		removed, i.e. all elements of the input array `c` that satisfy either of
	the following conditions::
		
		c < mean(c) - std(c)*low
		c > mean(c) + std(c)*high
		
		The iteration continues with the updated sample until no
		elements are outside the (updated) range.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : array_like
		Data array, will be raveled if not 1-D.
	low : float, optional
		Lower bound factor of sigma clipping. Default is 4.
	high : float, optional
		Upper bound factor of sigma clipping. Default is 4.
			'''
	result = OrderedPair(
		x=default.x,
		y=scipy.stats.sigmaclip(
			a=default.y,
			low=low,
			high=high,
		)
	)
	return result
