from scipy import signal, fft
from flojoy import flojoy, DataContainer


@flojoy
def FFT(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The FFT node Performs a Discrete Fourier Transform on the input vector.
    Through the FFT algorithm, the input vector will be transformed
    from the time domain into the frequency domain which will be an ordered pair of arrays.
    The user can specify a window type to be applied to the output with the 'window' parameter.
    The 'real' parameter will be used to determine if the input signal is real or not.

    Parameters
    ---------
    window: Selection of window types, optional
    real_signal: boolean

    Returns
    -------

    """
    if len(dc_inputs) != 1:
        raise ValueError(
            f"FFT node requires one input signal, but {len(dc_inputs)} was given!"
        )
    window_type: str = params["window_type"]  # Type of window function
    real: bool = params["real_signal"]
    signal_value = dc_inputs[0].y
    N = dc_inputs[0].x  # Number of samples

   # First to avoid spectral leakage, we need to apply a
   # window function to the signal
    fourier = fft.rfft(signal_value) if real else fft.fft(signal_value)
    if window_type:
        window = signal.get_window(window_type, N)
        result = fourier * window
    else:
        result = fourier

    return DataContainer(x=N, y=result)




