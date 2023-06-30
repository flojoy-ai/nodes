from flojoy import DataContainer, flojoy, DefaultParams
import scipy.signal

@flojoy
def HILBERT(default: DataContainer, default_parmas: DefaultParams, N: int=None, axis: int=-1):
    """

            Compute the analytic signal, using the Hilbert transform.

            The transformation is done along the last axis by default.

    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
    The parameters of the function in this Flojoy wrapper are given below.
    -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

    Parameters
    ----------
    x : array_like
            Signal data.  Must be real.
    N : int, optional
    Number of Fourier components.  Default: ``x.shape[axis]``
    axis : int, optional
    Axis along which to do the transformation.  Default: -1.
    """
    return DataContainer(x=dc[0].y, y=scipy.signal.hilbert(x=dc[0].y, N=int(params['N']) if params['N'] != '' else None, axis=int(params['axis']) if params['axis'] != '' else None))