from scipy import signal, fft
from flojoy import flojoy, DataContainer


@flojoy
def FFT(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Performs an Discrete Fourier Transform on the input vector.
    Through the FFT algorithm, the input vector will be transformed
    from the time domain into the frequency domain which will be an
    ordered pair of arrays
    """
    if len(dc_inputs) != 1:
        raise ValueError(
            "Expected one input but got something else"
        )
    window_type : str = params["window_type"] # Type of window function
    real : bool = params["real_signal"]
    signal_value = dc_inputs[0].y
    samples = dc_inputs[0].x

   # First to avoid spectral leakage, we need to apply a
   # window function to the signal
    fourier = fft.rfft(signal_value) if real else fft.fft(signal_value)
    if(window_type != "none"):
        window = signal.get_window(window_type, len(signal_value))
        result = fourier * window
    else:
        result = fourier

    return DataContainer(x=samples, y=result)




