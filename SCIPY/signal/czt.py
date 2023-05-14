from flojoy import DataContainer, flojoy
import scipy.signal

@flojoy
def CZT(dc, params):
	'''
		
		Compute the frequency response around a spiral in the Z plane.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	x : array
		The signal to transform.
	m : int, optional
		The number of output points desired.  Default is the length of the
		input data.
	w : complex, optional
		The ratio between points in each step.  This must be precise or the
		accumulated error will degrade the tail of the output sequence.
		Defaults to equally spaced points around the entire unit circle.
	a : complex, optional
		The starting point in the complex plane.  Default is 1+0j.
	axis : int, optional
		Axis over which to compute the FFT. If not given, the last axis is
		used.
			'''
	return DataContainer(
		x=dc[0].y,
		y=scipy.signal.czt(
			x=dc[0].y,
			m=(int(params['m']) if params['m'] != '' else None),
			w=(complex(params['w']) if params['w'] != '' else None),
			a=(complex(params['a']) if params['a'] != '' else None),
			axis=(int(params['axis']) if params['axis'] != '' else None),
		)
	)

