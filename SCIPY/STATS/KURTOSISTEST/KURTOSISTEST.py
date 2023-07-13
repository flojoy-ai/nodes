from flojoy import OrderedPair, flojoy
import scipy.stats


@flojoy(node_type='default')
def KURTOSISTEST(
	default: OrderedPair,
	axis: int = 0,
	nan_policy: str = 'propagate',
	alternative: str = 'two-sided',
	) -> OrderedPair:
	'''
		Test whether a dataset has normal kurtosis.
		
		This function tests the null hypothesis that the kurtosis
		of the population from which the sample was drawn is that
		of the normal distribution.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : array
		Array of the sample data.
	axis : int or None, optional
		Axis along which to compute test. Default is 0. If None,
		compute over the whole array `a`.
	nan_policy : {'propagate', 'raise', 'omit'}, optional
		Defines how to handle when input contains nan.
	The following options are available (default is 'propagate'):
		
	* 'propagate': returns nan
	* 'raise': throws an error
	* 'omit': performs the calculations ignoring nan values
		
	alternative : {'two-sided', 'less', 'greater'}, optional
		Defines the alternative hypothesis.
	The following options are available (default is 'two-sided'):
		
	* 'two-sided': the kurtosis of the distribution underlying the sample
		is different from that of the normal distribution
	* 'less': the kurtosis of the distribution underlying the sample
		is less than that of the normal distribution
	* 'greater': the kurtosis of the distribution underlying the sample
		is greater than that of the normal distribution
		
	.. versionadded:: 1.7.0
			'''
	result = OrderedPair(
		x=default.x,
		y=scipy.stats.kurtosistest(
			a=default.y,
			axis=axis,
			nan_policy=nan_policy,
			alternative=alternative,
		)
	)
	return result
