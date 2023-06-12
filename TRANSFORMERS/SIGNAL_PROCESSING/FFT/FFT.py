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
    window: Selection of window types
        the node will apply a window to the signal to avoid spectral leakage
    real_signal: boolean
        whether the input signal is real or complex
    sample_rate: int
        the sample rate of the signal, defaults to 1
    absolute: boolean
        whether the output would be absolute value or not, false if IFFT would be used

    Returns
    -------
    ordered_pair
        x: frequency
        y: spectrum of the signal

    """
    if len(dc_inputs) != 1:
        raise ValueError(
            f"FFT node requires 1 input signal, but {len(dc_inputs)} was given!"
        )
    dc = dc_inputs[0]
    if dc.type != "ordered_pair":
        raise ValueError(
            f"unsupported DataContainer type passed to FFT node: '{dc.type}'"
        )

    window_type: str = params["window_type"]
    real: bool = params["real_signal"]
    sample_rate: int = params["sample_rate"]  # Hz
    absolute: bool = params["absolute"]

    if sample_rate <= 0:
        raise ValueError(f"Sample rate must be greater than 0")

    signal_value = dc.y
    x = dc.x

    if window_type == "none":
        fourier = fft.rfft(signal_value) if real else fft.fft(signal_value)
    else:
        window = signal.get_window(window_type, len(signal_value))
        fourier = (
            fft.rfft(signal_value * window) if real else fft.fft(signal_value * window)
        )

    fourier = fft.fftshift(fourier)
    frequency = fft.rfftfreq(x.shape[-1], 1 / sample_rate)
    frequency = fft.fftshift(frequency)
    result = abs(fourier.real) if absolute else fourier.real

    return DataContainer(x=frequency, y=result)
