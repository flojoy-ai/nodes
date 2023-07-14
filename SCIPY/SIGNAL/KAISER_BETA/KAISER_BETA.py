from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np


import scipy.signal


@flojoy(node_type='default')
def KAISER_BETA(
	default: OrderedPair | Matrix,
	) -> OrderedPair | Matrix | Scalar:
	'''The KAISER_BETA node is based on a numpy or scipy function.
	The description of that function is as follows:

		Compute the Kaiser parameter `beta`, given the attenuation `a`.
		
	Parameters
	----------
	a : float
		The desired attenuation in the stopband and maximum ripple in
		the passband, in dB.  This should be a *positive* number.

	Returns
	----------
	DataContainer:
		type 'ordered pair', 'scalar', or 'matrix'
	'''

	result = OrderedPair(
		m=scipy.signal.kaiser_beta(
			a=default.y,
			))

	return result
