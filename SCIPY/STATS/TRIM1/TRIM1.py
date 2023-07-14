from flojoy import OrderedPair, flojoy, Matrix, Scalar
import numpy as np


import scipy.stats


@flojoy(node_type='default')
def TRIM1(
	default: OrderedPair | Matrix,
	proportiontocut: float,
	tail: str = 'right',
	axis: int = 0,
	) -> OrderedPair | Matrix | Scalar:
	'''The TRIM1 node is based on a numpy or scipy function.
	The description of that function is as follows:

		Slice off a proportion from ONE end of the passed array distribution.
		
		If `proportiontocut` = 0.1, slices off 'leftmost' or 'rightmost'
		10% of scores. The lowest or highest values are trimmed (depending on
		the tail).
		Slice off less if proportion results in a non-integer slice index
		(i.e. conservatively slices off `proportiontocut` ).
		
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

	Returns
	----------
	DataContainer:
		type 'ordered pair', 'scalar', or 'matrix'
	'''

	result = OrderedPair(
		m=scipy.stats.trim1(
			a=default.y,
			proportiontocut=proportiontocut,
			tail=tail,
			axis=axis,
		))

	return result
