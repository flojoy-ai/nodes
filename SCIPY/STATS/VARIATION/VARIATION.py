from flojoy import OrderedPair, flojoy
import scipy.stats


@flojoy(node_type='default')
def VARIATION(
	default: OrderedPair,
	axis: int = 0,
	nan_policy: str = 'propagate',
	ddof: int = 0,
	keepdims: bool = False,
	) -> OrderedPair:
	'''
		
		Compute the coefficient of variation.
		
		The coefficient of variation is the standard deviation divided by the
	mean.  This function is equivalent to::
		
		np.std(x, axis=axis, ddof=ddof) / np.mean(x)
		
		The default for ``ddof`` is 0, but many definitions of the coefficient
		of variation use the square root of the unbiased sample variance
		for the sample standard deviation, which corresponds to ``ddof=1``.
		
		The function does not take the absolute value of the mean of the data,
		so the return value is negative if the mean is negative.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : array_like
		Input array.
	axis : int or None, optional
		Axis along which to calculate the coefficient of variation.
		Default is 0. If None, compute over the whole array `a`.
	nan_policy : {'propagate', 'raise', 'omit'}, optional
		Defines how to handle when input contains ``nan``.
	The following options are available:
		
	* 'propagate': return ``nan``
	* 'raise': raise an exception
	* 'omit': perform the calculation with ``nan`` values omitted
		
		The default is 'propagate'.
	ddof : int, optional
		Gives the "Delta Degrees Of Freedom" used when computing the
		standard deviation.  The divisor used in the calculation of the
		standard deviation is ``N - ddof``, where ``N`` is the number of
		elements.  `ddof` must be less than ``N``; if it isn't, the result
		will be ``nan`` or ``inf``, depending on ``N`` and the values in
		the array.  By default `ddof` is zero for backwards compatibility,
		but it is recommended to use ``ddof=1`` to ensure that the sample
		standard deviation is computed as the square root of the unbiased
		sample variance.
	keepdims : bool, optional
		If this is set to True, the axes which are reduced are left in the
		result as dimensions with size one. With this option, the result
		will broadcast correctly against the input array.
			'''
	result = OrderedPair(
		x=default.x,
		y=scipy.stats.variation(
			a=default.y,
			axis=axis,
			nan_policy=nan_policy,
			ddof=ddof,
			keepdims=keepdims,
		)
	)
	return result
