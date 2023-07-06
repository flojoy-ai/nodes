import scipy
from flojoy import flojoy, OrderedPair
import warnings


@flojoy
def SAVGOL(
    default: OrderedPair, window_length: int = 3, poly_order: int = 1
) -> OrderedPair:
    """Apply a Savitzky-Golay filter to an input signal, it's generally used for smoothing data
    The default behaviour is implementing a 3-point moving average of the data."""
    signal = default.y
    if poly_order >= window_length:
        warnings.warn(
            "Polynomial order is greater than the window size. Using p=w-1..."
        )
        poly_order = window_length - 1
    filtered = scipy.signal.savgol_filter(signal, window_length, poly_order)
    return OrderedPair(x=signal, y=filtered)
