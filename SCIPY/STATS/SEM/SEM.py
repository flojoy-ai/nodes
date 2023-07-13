from flojoy import OrderedPair, flojoy
import scipy.stats


@flojoy(node_type='default')
def SEM(
	default: OrderedPair,
	axis: int = 0,
	ddof: int = 1,
	nan_policy: str = 'propagate',
	) -> OrderedPair:
	'''
		Compute standard error of the mean.
		
		Calculate the standard error of the mean (or standard error of
		measurement) of the values in the input array.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : array_like
		An array containing the values for which the standard error is
		returned.
	axis : int or None, optional
		Axis along which to operate. Default is 0. If None, compute over
		the whole array `a`.
	ddof : int, optional
		Delta degrees-of-freedom. How many degrees of freedom to adjust
		for bias in limited samples relative to the population estimate
		of variance. Defaults to 1.
	nan_policy : {'propagate', 'raise', 'omit'}, optional
		Defines how to handle when input contains nan.
	The following options are available (default is 'propagate'):
		
	* 'propagate': returns nan
	* 'raise': throws an error
	* 'omit': performs the calculations ignoring nan values
			'''
	result = OrderedPair(
		x=default.x,
		y=scipy.stats.sem(
			a=default.y,
			axis=axis,
			ddof=ddof,
			nan_policy=nan_policy,
		)
	)
	return result
