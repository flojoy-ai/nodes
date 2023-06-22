import scipy
from flojoy import flojoy, DataContainer
import warnings


@flojoy
def SAVGOL(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """ The Savgol Node Applies a Savitzky-Golay filter to an input vector.
    The default behaviour is implementing a 3-point moving average of the data."""
    if len(dc_inputs) != 1:
        raise ValueError(f"SAVGOL node requires 1 input signal")
    dc = dc_inputs[0]
    x = dc.x
    signal = dc.y
    window_length: int = params["wlen"]
    poly_order: int = params["porder"]
    if poly_order >= window_length:
        warnings.warn(
            "Polynomial order is greater than the window size. Using p=w-1..."
        )
        poly_order = window_length - 1
    filtered = scipy.signal.savgol_filter(signal, window_length, poly_order)
    return DataContainer(x=x, y=filtered)
