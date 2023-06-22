from scipy import signal
from flojoy import flojoy, DataContainer
import numpy as np


@flojoy
def FIR(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The FIR node Apply a low-pass FIR filter to an input vector.
    The filter is designed with the window method.
    This filter takes a few inputs: the sample_rate (will be passed as a parameter
    if the target node is not connected), the window type of the filter, the cutoff frequency.
    and lastly the number of taps (or length) of the filter.

    Parameters
    ----------
    sample_rate: int
        The amount of samples during a second
    filter_type: select
        How the filter behaves
    window: select
        The window function used in the FIR
    cutoff_low: float
        The frequency cutoff to filter out the lower frequencies
    cutoff_high: float
        The frequency cutoff to filter out the upper frequencies
    taps: int
        The length of the filter

    Returns
        x: time domain
        y: filtered signal
    ------
    """

    sample_rate: int = params["sample_rate"]  # Hz
    filter_type: str = params["filter_type"]
    window_type: str = params["window"]
    cutoff_low: float = params["cutoff_low"]
    cutoff_high: float = params["cutoff_high"]
    n_taps: int = params["taps"]


    try:
        times = dc_inputs[0].x
        input_signal = dc_inputs[0].y  # this is the value of the signal
    except IndexError:  # nothing input
        # lets create some default behaviour for testing
        nsamples: int = 400
        times = np.arange(nsamples) / sample_rate
        test_x = (
            np.cos(2 * np.pi * 0.5 * times)
            + 0.2 * np.sin(2 * np.pi * 2.5 * times + 0.1)
            + 0.2 * np.sin(2 * np.pi * 15.3 * times)
            + 0.1 * np.sin(2 * np.pi * 16.7 * times + 0.1)
            + 0.1 * np.sin(2 * np.pi * 23.45 * times + 0.8)
        )
        input_signal = test_x
    if input_signal.size < n_taps * 3:
        raise ValueError("length of the data should be three times longer than taps")
    elif n_taps % 2 == 0:  # in the case where the passband contains the Nyquist frequency
        n_taps = n_taps + 1

    # create the filter with the parameter inputs
    if filter_type == "bandpass" or filter_type == "bandstop":
        fil = signal.firwin(
            numtaps=n_taps,
            cutoff=[cutoff_low, cutoff_high],
            fs=sample_rate,
            pass_zero=filter_type,
            window=window_type,
        )
    elif filter_type == "lowpass":
        fil = signal.firwin(
            numtaps=n_taps,
            cutoff=cutoff_high,
            fs=sample_rate,
            pass_zero=filter_type,
            window=window_type,
        )
    else:
        fil = signal.firwin(
            numtaps=n_taps,
            cutoff=cutoff_low,
            fs=sample_rate,
            pass_zero=filter_type,
            window=window_type,
        )

    # ... and then apply it to the signal
    filtered_x = signal.filtfilt(fil, 1.0, input_signal)
    return DataContainer(x=times, y=filtered_x)
