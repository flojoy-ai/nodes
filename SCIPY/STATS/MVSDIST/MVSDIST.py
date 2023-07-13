from flojoy import OrderedPair, flojoy
import scipy.stats


@flojoy(node_type='default')
def MVSDIST(
	default: OrderedPair,
	) -> OrderedPair:
	'''
		
		'Frozen' distributions for mean, variance, and standard deviation of data.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	data : array_like
		Input array. Converted to 1-D using ravel.
		Requires 2 or more data-points.
			'''
	result = OrderedPair(
		x=default.x,
		y=scipy.stats.mvsdist(
			data=default.y,
			)
	)
	return result
