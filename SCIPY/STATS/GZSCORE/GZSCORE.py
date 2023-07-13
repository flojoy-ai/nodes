from flojoy import OrderedPair, flojoy
import scipy.stats


@flojoy(node_type='default')
def GZSCORE(
	default: OrderedPair,
	axis: int = 0,
	ddof: int = 0,
	nan_policy: str = 'propagate',
	) -> OrderedPair:
	'''
		
		Compute the geometric standard score.
		
		Compute the geometric z score of each strictly positive value in the
		sample, relative to the geometric mean and standard deviation.
	Mathematically the geometric z score can be evaluated as::
		
		gzscore = log(a/gmu) / log(gsigma)
		
		where ``gmu`` (resp. ``gsigma``) is the geometric mean (resp. standard
		deviation).
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : array_like
		Sample data.
	axis : int or None, optional
		Axis along which to operate. Default is 0. If None, compute over
		the whole array `a`.
	ddof : int, optional
		Degrees of freedom correction in the calculation of the
		standard deviation. Default is 0.
	nan_policy : {'propagate', 'raise', 'omit'}, optional
		Defines how to handle when input contains nan. 'propagate' returns nan,
		'raise' throws an error, 'omit' performs the calculations ignoring nan
		values. Default is 'propagate'.  Note that when the value is 'omit',
		nans in the input also propagate to the output, but they do not affect
		the geometric z scores computed for the non-nan values.
			'''
	result = OrderedPair(
		x=default.x,
		y=scipy.stats.gzscore(
			a=default.y,
			axis=axis,
			ddof=ddof,
			nan_policy=nan_policy,
		)
	)
	return result
