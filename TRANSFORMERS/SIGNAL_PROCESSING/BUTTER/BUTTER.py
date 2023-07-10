from scipy import signal
from flojoy import flojoy, OrderedPair
from typing import Literal, Union


@flojoy
def BUTTER(
    default: OrderedPair,
    filter_order: int = 1,
    critical_frequency: int = 1,
    btype: Literal["lowpass", "highpass", "bandpass", "bandstop"] = "lowpass",
    sample_rate: int = 10,
) -> OrderedPair:
    """The BUTTER node applies a butterworth filter to an input signal.
    It is designed to have a frequency response that is as flat as possible in the pass band

    Parameters
    ----------
    filter_order: int
        The intensity of the filter
    critical_frequency: int
        The frequency where the filter takes effect. For lowpass and highpass, takes in a scalar.
        For bandpass and bandstop, takes in array with the length of two
    btype: select
        The type of the filter
    sample_rate: int
        The sample rate of the input signal

    Returns
    -------
    OrderedPair
        x: time domain
        y: filtered signal
    """
    sig = default.y
    order: int = filter_order
    wn: int = critical_frequency  # hz
    btype: str = btype
    fs: int = sample_rate  # hz

    sos = signal.butter(N=order, Wn=wn, btype=btype, fs=fs, output="sos")
    #    sos = signal.butter(10, 15, "hp", fs=1000, output="sos")
    filtered = signal.sosfilt(sos, sig)

    return OrderedPair(x=default.x, y=filtered)
