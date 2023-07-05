from scipy import fft
from flojoy import flojoy, OrderedPair, DataFrame
import pandas as pd


@flojoy
def IFFT(input: DataFrame, real_signal: bool) -> OrderedPair:
    """The IFFT performs the Inverse Discrete Fourier Transform on the input signal.
    With the IFFT algorith, the input signal will be transformed from the
    frequency domain back into the time domain.

    Parameters
    ----------
    real_signal: boolean
        whether the input signal is real (true) or complex (false)

    Returns
    -------
    ordered_pair
        x = time
        y = reconstructed signal
    """
    dc: pd.DataFrame = input.m
    real: bool = real_signal

    x = dc["x"].to_numpy()
    realValue = dc["real"].to_numpy()
    imagValue = dc["imag"].to_numpy()

    fourier = realValue + 1j * imagValue

    result = fft.irfft(fourier) if real else fft.ifft(fourier, len(x))
    result = result.real
    return OrderedPair(x=x, y=result)
