from flojoy import DataContainer, flojoy
import scipy.stats

@flojoy
def TRIMBOTH(dc, params):
	'''
		Slice off a proportion of items from both ends of an array.
		
		Slice off the passed proportion of items from both ends of the passed
		array (i.e., with `proportiontocut` = 0.1, slices leftmost 10% **and**
		rightmost 10% of scores). The trimmed values are the lowest and
		highest ones.
		Slice off less if proportion results in a non-integer slice index (i.e.
		conservatively slices off `proportiontocut`).
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : array_like
		Data to trim.
	proportiontocut : float
		Proportion (in range 0-1) of total data set to trim of each end.
	axis : int or None, optional
		Axis along which to trim data. Default is 0. If None, compute over
		the whole array `a`.
			'''
	return DataContainer(
		x=dc[0].y,
		y=scipy.stats.trimboth(
			a=dc[0].y,
			proportiontocut=(float(params['proportiontocut']) if params['proportiontocut'] != '' else None),
			axis=(int(params['axis']) if params['axis'] != '' else None),
		)
	)

