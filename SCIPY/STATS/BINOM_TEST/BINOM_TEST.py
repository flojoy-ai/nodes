from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np


import scipy.stats


@flojoy(node_type='default')
def BINOM_TEST(
	default: OrderedPair | Matrix,
	n: int,
	p: float = 0.5,
	alternative: str = 'two-sided',
	) -> OrderedPair | Matrix | Scalar:
	'''The BINOM_TEST node is based on a numpy or scipy function.
	The description of that function is as follows:

		Perform a test that the probability of success is p.
		
	Note: `binom_test` is deprecated; it is recommended that `binomtest`
		be used instead.
		
		This is an exact, two-sided test of the null hypothesis
		that the probability of success in a Bernoulli experiment
		is `p`.
		
	Parameters
	----------
	x : int or array_like
		The number of successes, or if x has length 2, it is the
		number of successes and the number of failures.
	n : int
		The number of trials.  This is ignored if x gives both the
		number of successes and failures.
	p : float, optional
		The hypothesized probability of success.  ``0 <= p <= 1``. The
		default value is ``p = 0.5``.
	alternative : {'two-sided', 'greater', 'less'}, optional
		Indicates the alternative hypothesis. The default value is
		'two-sided'.

	Returns
	----------
	DataContainer:
		type 'ordered pair', 'scalar', or 'matrix'
	'''

	result = OrderedPair(
		m=scipy.stats.binom_test(
			x=default.y,
			n=n,
			p=p,
			alternative=alternative,
		))

	return result
