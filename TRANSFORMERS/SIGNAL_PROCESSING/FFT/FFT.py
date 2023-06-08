from scipy import signal, fft
from numpy import abs
from flojoy import flojoy, DataContainer


@flojoy
def FFT(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The FFT node Performs a Discrete Fourier Transform on the input vector.
    Through the FFT algorithm, the input vector will be transformed
    from the time domain into the frequency domain which will be an ordered pair of arrays.

    Parameters
    ---------
    window: Selection of window types, optional
        the node will apply a window to the signal to avoid spectral leakage
    real_signal: boolean
        whether the input signal is real or complex
    sample_rate: int
        the sample rate of the real signal, if the input is complex, it will default to 1
        regardless of the input

    Returns
    -------
    ordered_pair
        x: frequency
        y: spectrum of the signal

    """
    if len(dc_inputs) != 1:
        raise ValueError(
            f"FFT node requires one input signal, but {len(dc_inputs)} was given!"
        )
    dc = dc_inputs[0]
    if dc.type != "ordered_pair":
        raise ValueError(
            f"unsupported DataContainer type passed to FFT node: '{dc.type}'"
        )
    window_type: str = params["window_type"]  # Type of window function
    real: bool = params["real_signal"]
    sample_rate: int = params["sample_rate"]

    signal_value = dc.y
    x = dc.x

    if window_type:
        window = signal.get_window(window_type, len(signal_value))
        fourier = (
            fft.rfft(signal_value * window) if real else fft.fft(signal_value * window)
        )
    else:  # no window applied
        fourier = fft.rfft(signal_value) if real else fft.fft(signal_value)
    fourier = fft.fftshift(fourier)
    frequency = fft.rfftfreq(x.shape[-1], 1 / sample_rate) if real else fft.fftfreq(x.shape[-1])
    frequency = fft.fftshift(frequency)

    result = abs(fourier)
    return DataContainer(x=frequency, y=result)
