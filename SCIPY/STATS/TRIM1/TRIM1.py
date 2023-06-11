from flojoy import DataContainer, flojoy
import scipy.stats

@flojoy
def TRIM1(dc, params):
	'''
		Slice off a proportion from ONE end of the passed array distribution.
		
		If `proportiontocut` = 0.1, slices off 'leftmost' or 'rightmost'
		10% of scores. The lowest or highest values are trimmed (depending on
		the tail).
		Slice off less if proportion results in a non-integer slice index
		(i.e. conservatively slices off `proportiontocut` ).
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : array_like
		Input array.
	proportiontocut : float
		Fraction to cut off of 'left' or 'right' of distribution.
	tail : {'left', 'right'}, optional
		Defaults to 'right'.
	axis : int or None, optional
		Axis along which to trim data. Default is 0. If None, compute over
		the whole array `a`.
			'''
	return DataContainer(
		x=dc[0].y,
		y=scipy.stats.trim1(
			a=dc[0].y,
			proportiontocut=(float(params['proportiontocut']) if params['proportiontocut'] != '' else None),
			tail=(str(params['tail']) if params['tail'] != '' else None),
			axis=(int(params['axis']) if params['axis'] != '' else None),
		)
	)

