from flojoy import DataContainer, flojoy
import scipy.stats

@flojoy
def KSTATVAR(dc, params):
	'''
		
		
		
		Return an unbiased estimator of the variance of the k-statistic.
		
		See `kstat` for more details of the k-statistic.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	data : array_like
		Input array. Note that n-D input gets flattened.
	n : int, {1, 2}, optional
		Default is equal to 2.
	axis : int or None, default: None
		If an int, the axis of the input along which to compute the statistic.
		The statistic of each axis-slice (e.g. row) of the input will appear in a
		corresponding element of the output.
		If ``None``, the input will be raveled before computing the statistic.
	nan_policy : {'propagate', 'omit', 'raise'}
		Defines how to handle input NaNs.
		
	- ``propagate``: if a NaN is present in the axis slice (e.g. row) along
		which the  statistic is computed, the corresponding entry of the output
		will be NaN.
	- ``omit``: NaNs will be omitted when performing the calculation.
		If insufficient data remains in the axis slice along which the
		statistic is computed, the corresponding entry of the output will be
		NaN.
	- ``raise``: if a NaN is present, a ``ValueError`` will be raised.
	keepdims : bool, default: False
		If this is set to True, the axes which are reduced are left
		in the result as dimensions with size one. With this option,
		the result will broadcast correctly against the input array.
			'''
	return DataContainer(
		x=dc[0].y,
		y=scipy.stats.kstatvar(
			data=dc[0].y,
			n=(int(params['n']) if params['n'] != '' else None),
			axis=(int or None(params['axis']) if params['axis'] != '' else None),
			nan_policy=(str(params['nan_policy']) if params['nan_policy'] != '' else None),
			keepdims=(bool(params['keepdims']) if params['keepdims'] != '' else None),
		)
	)

