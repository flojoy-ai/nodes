from flojoy import DataContainer, flojoy
import scipy.signal

@flojoy
def KAISER_BETA(dc, params):
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
	return DataContainer(
		x=dc[0].y,
		y=scipy.signal.kaiser_beta(
			a=dc[0].y,
			)
	)

