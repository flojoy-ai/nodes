from flojoy import OrderedPair, flojoy
import scipy.stats


@flojoy(node_type='default')
def SKEWTEST(
	default: OrderedPair,
	axis: int = 0,
	nan_policy: str = 'propagate',
	alternative: str = 'two-sided',
	) -> OrderedPair:
	'''
		Test whether the skew is different from the normal distribution.
		
		This function tests the null hypothesis that the skewness of
		the population that the sample was drawn from is the same
		as that of a corresponding normal distribution.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : array
		The data to be tested.
	axis : int or None, optional
		Axis along which statistics are calculated. Default is 0.
		If None, compute over the whole array `a`.
	nan_policy : {'propagate', 'raise', 'omit'}, optional
		Defines how to handle when input contains nan.
	The following options are available (default is 'propagate'):
		
	* 'propagate': returns nan
	* 'raise': throws an error
	* 'omit': performs the calculations ignoring nan values
		
	alternative : {'two-sided', 'less', 'greater'}, optional
		Defines the alternative hypothesis. Default is 'two-sided'.
	The following options are available:
		
	* 'two-sided': the skewness of the distribution underlying the sample
		is different from that of the normal distribution (i.e. 0)
	* 'less': the skewness of the distribution underlying the sample
		is less than that of the normal distribution
	* 'greater': the skewness of the distribution underlying the sample
		is greater than that of the normal distribution
		
	.. versionadded:: 1.7.0
			'''
	result = OrderedPair(
		x=default.x,
		y=scipy.stats.skewtest(
			a=default.y,
			axis=axis,
			nan_policy=nan_policy,
			alternative=alternative,
		)
	)
	return result
