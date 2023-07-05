from scipy import signal, fft
from numpy import abs
from flojoy import flojoy, OrderedPair, DataFrame
from pandas import DataFrame as df


@flojoy
def FFT(default: OrderedPair, window_type: str = "none", real: bool = False, sample_rate: int = 1, display: bool = True) -> OrderedPair | DataFrame:
    """The FFT node performs a Discrete Fourier Transform on the input vector.
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
    display: boolean
        whether the output would be graphed, set to false for pure data, true for data that's more suitable to be graphed

    Returns
    -------
    ordered_pair
        x: frequency
        y: spectrum of the signal

    """

    if sample_rate <= 0:
        raise ValueError(f"Sample rate must be greater than 0")

    signal_value = default.y
    x = default.x
    sample_spacing = 1.0 / sample_rate
    # x-axis
    frequency = (
        fft.rfftfreq(x.shape[-1], sample_spacing)
        if real
        else fft.fftfreq(x.shape[-1], sample_spacing)
    )
    frequency = fft.fftshift(frequency)
    if display:
        # y-axis
        if window_type == "none":
            fourier = fft.rfft(signal_value) if real else fft.fft(signal_value)
        else:
            window = signal.get_window(window_type, len(signal_value))
            fourier = (
                fft.rfft(signal_value * window)
                if real
                else fft.fft(signal_value * window)
            )
        fourier = fft.fftshift(fourier)
        fourier = abs(fourier)
        return OrderedPair(x=frequency, y=fourier)

    # for processing
    fourier = fft.rfft(signal_value) if real else fft.fft(signal_value)
    d = {"x": x, "frequency": frequency, "real": fourier.real, "imag": fourier.imag}
    return DataFrame(m=df(data=d))
