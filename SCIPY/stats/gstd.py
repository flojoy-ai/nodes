from flojoy import DataContainer, flojoy
import scipy.stats

@flojoy
def GSTD(dc, params):
	'''
		
		Calculate the geometric standard deviation of an array.
		
		The geometric standard deviation describes the spread of a set of numbers
		where the geometric mean is preferred. It is a multiplicative factor, and
		so a dimensionless quantity.
		
		It is defined as the exponent of the standard deviation of ``log(a)``.
		Mathematically the population geometric standard deviation can be
	evaluated as::
		
		gstd = exp(std(log(a)))
		
	.. versionadded:: 1.3.0
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : array_like
		An array like object containing the sample data.
	axis : int, tuple or None, optional
		Axis along which to operate. Default is 0. If None, compute over
		the whole array `a`.
	ddof : int, optional
		Degree of freedom correction in the calculation of the
		geometric standard deviation. Default is 1.
			'''
	return DataContainer(
		x=dc[0].y,
		y=scipy.stats.gstd(
			a=dc[0].y,
			axis=(int(params['axis']) if params['axis'] != '' else None),
			ddof=(int(params['ddof']) if params['ddof'] != '' else None),
		)
	)

