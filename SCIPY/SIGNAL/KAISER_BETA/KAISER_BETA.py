from flojoy import OrderedPair, flojoy
import scipy.signal


@flojoy(node_type='default')
def KAISER_BETA(
	default: OrderedPair,
	) -> OrderedPair:
	'''
		Compute the Kaiser parameter `beta`, given the attenuation `a`.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : float
		The desired attenuation in the stopband and maximum ripple in
		the passband, in dB.  This should be a *positive* number.
			'''
	result = OrderedPair(
		x=default.x,
		y=scipy.signal.kaiser_beta(
			a=default.y,
			)
	)
	return result
