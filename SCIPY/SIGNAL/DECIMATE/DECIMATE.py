from flojoy import DataContainer, flojoy
import scipy.signal

@flojoy
def DECIMATE(dc, params):
	'''
		
		Downsample the signal after applying an anti-aliasing filter.
		
		By default, an order 8 Chebyshev type I filter is used. A 30 point FIR
		filter with Hamming window is used if `ftype` is 'fir'.
		
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
	The parameters of the function in this Flojoy wrapper are given below.
	-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

	Parameters
	----------
	x : array_like
		The signal to be downsampled, as an N-dimensional array.
	q : int
		The downsampling factor. When using IIR downsampling, it is recommended
		to call `decimate` multiple times for downsampling factors higher than
		13.
	n : int, optional
		The order of the filter (1 less than the length for 'fir'). Defaults to
		8 for 'iir' and 20 times the downsampling factor for 'fir'.
	ftype : str {'iir', 'fir'} or ``dlti`` instance, optional
		If 'iir' or 'fir', specifies the type of lowpass filter. If an instance
		of an `dlti` object, uses that object to filter before downsampling.
	axis : int, optional
		The axis along which to decimate.
	zero_phase : bool, optional
		Prevent phase shift by filtering with `filtfilt` instead of `lfilter`
		when using an IIR filter, and shifting the outputs back by the filter's
		group delay when using an FIR filter. The default value of ``True`` is
		recommended, since a phase shift is generally not desired.
		
	.. versionadded:: 0.18.0
			'''
	return DataContainer(
		x=dc[0].y,
		y=scipy.signal.decimate(
			x=dc[0].y,
			q=(int(params['q']) if params['q'] != '' else None),
			n=(int(params['n']) if params['n'] != '' else None),
			ftype=(str(params['ftype']) if params['ftype'] != '' else None),
			axis=(int(params['axis']) if params['axis'] != '' else None),
			zero_phase=(bool(params['zero_phase']) if params['zero_phase'] != '' else None),
		)
	)

