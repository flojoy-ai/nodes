from flojoy import DataContainer, flojoy
import scipy.stats

@flojoy
def RANKDATA(dc, params):
	'''
		Assign ranks to data, dealing with ties appropriately.
		
		By default (``axis=None``), the data array is first flattened, and a flat
		array of ranks is returned. Separately reshape the rank array to the
		shape of the data array if desired (see Examples).
		
		Ranks begin at 1.  The `method` argument controls how ranks are assigned
		to equal values.  See [1]_ for further discussion of ranking methods.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	a : array_like
		The array of values to be ranked.
	method : {'average', 'min', 'max', 'dense', 'ordinal'}, optional
		The method used to assign ranks to tied elements.
	The following methods are available (default is 'average'):
		
	* 'average': The average of the ranks that would have been assigned to
		all the tied values is assigned to each value.
	* 'min': The minimum of the ranks that would have been assigned to all
		the tied values is assigned to each value.  (This is also
		referred to as "competition" ranking.)
	* 'max': The maximum of the ranks that would have been assigned to all
		the tied values is assigned to each value.
	* 'dense': Like 'min', but the rank of the next highest element is
		assigned the rank immediately after those assigned to the tied
		elements.
	* 'ordinal': All values are given a distinct rank, corresponding to
		the order that the values occur in `a`.
	axis : {None, int}, optional
		Axis along which to perform the ranking. If ``None``, the data array
		is first flattened.
			'''
	return DataContainer(
		x=dc[0].y,
		y=scipy.stats.rankdata(
			a=dc[0].y,
			method=(str(params['method']) if params['method'] != '' else None),
			axis=(None(params['axis']) if params['axis'] != '' else None),
		)
	)

