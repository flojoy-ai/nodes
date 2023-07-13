from flojoy import OrderedPair, flojoy
import scipy.stats


@flojoy(node_type='default')
def BAYES_MVS(
	default: OrderedPair,
	alpha: float = 0.9,
	) -> OrderedPair:
	'''
		
		Bayesian confidence intervals for the mean, var, and std.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	data : array_like
		Input data, if multi-dimensional it is flattened to 1-D by `bayes_mvs`.
		Requires 2 or more data points.
	alpha : float, optional
		Probability that the returned confidence interval contains
		the true parameter.
			'''
	result = OrderedPair(
		x=default.x,
		y=scipy.stats.bayes_mvs(
			data=default.y,
			alpha=alpha,
		)
	)
	return result
