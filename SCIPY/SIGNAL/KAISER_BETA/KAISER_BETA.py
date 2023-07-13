from flojoy import OrderedPair, flojoy
import scipy.signal


@flojoy(node_type="default")
def KAISER_BETA(
    default: OrderedPair,
) -> OrderedPair:
    """The KAISER_BETA node is based on a numpy or scipy function.
    The description of that function is as follows:

            Compute the Kaiser parameter `beta`, given the attenuation `a`.

    Parameters
    ----------
    a : float
            The desired attenuation in the stopband and maximum ripple in
            the passband, in dB.  This should be a *positive* number.

    Returns
    ----------
    DataContainer:
            type 'ordered pair'"""
    result = OrderedPair(
        x=default.x,
        y=scipy.signal.kaiser_beta(
            a=default.y,
        ),
    )
    return result
