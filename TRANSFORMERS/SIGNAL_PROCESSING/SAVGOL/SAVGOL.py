import scipy
from flojoy import flojoy, OrderedPair
import warnings


@flojoy
def SAVGOL(
    default: OrderedPair, window_length: int = 50, poly_order: int = 1
) -> OrderedPair:
    """Apply a Savitzky-Golay filter to an input signal, it's generally used for smoothing data
    The default behaviour is implementing a 3-point moving average of the data.

    Parameters
    ----------
    window_length: int
        the length of the filter window, must be less than or equal to size of the input
    poly_order: int
        the order of the polynomial used to fit the samples, must be less than or equal to size of window_length

    Returns
    -------
    OrderedPair
        x: time axis
        y: filtered signal
    """
    signal = default.y
    if window_length >= len(default.x):
        warnings.warn(
            "Polynomial order is greater than the window size. Using p=w-1..."
        )
        poly_order = len(default.x) - 1

    if poly_order >= window_length:
        warnings.warn(
            "Polynomial order is greater than the window size. Using p=w-1..."
        )
        poly_order = window_length - 1

    filtered = scipy.signal.savgol_filter(signal, window_length, poly_order)
    return OrderedPair(x=default.x, y=filtered)
