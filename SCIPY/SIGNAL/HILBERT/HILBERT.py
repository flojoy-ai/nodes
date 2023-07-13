from flojoy import OrderedPair, flojoy
import scipy.signal


@flojoy(node_type="default")
def HILBERT(
    default: OrderedPair,
    N: int,
    axis: int = -1,
) -> OrderedPair:
    """The HILBERT node is based on a numpy or scipy function.
    The description of that function is as follows:


            Compute the analytic signal, using the Hilbert transform.

            The transformation is done along the last axis by default.

    Parameters
    ----------
    x : array_like
            Signal data.  Must be real.
    N : int, optional
    Number of Fourier components.  Default: ``x.shape[axis]``
    axis : int, optional
    Axis along which to do the transformation.  Default: -1.

    Returns
    ----------
    DataContainer:
            type 'ordered pair'"""
    result = OrderedPair(
        x=default.x,
        y=scipy.signal.hilbert(
            x=default.y,
            N=N,
            axis=axis,
        ),
    )
    return result
