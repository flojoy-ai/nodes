from flojoy import OrderedPair, flojoy
import scipy.stats


@flojoy(node_type='default')
def SHAPIRO(
	default: OrderedPair,
	) -> OrderedPair:
	'''
		Perform the Shapiro-Wilk test for normality.
		
		The Shapiro-Wilk test tests the null hypothesis that the
		data was drawn from a normal distribution.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	x : array_like
		Array of sample data.
			'''
	result = OrderedPair(
		x=default.x,
		y=scipy.stats.shapiro(
			x=default.y,
			)
	)
	return result
