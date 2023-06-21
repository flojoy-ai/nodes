from scipy import signal
from flojoy import flojoy, DataContainer
import numpy as np


@flojoy
def FIR(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The FIR node Apply a low-pass FIR filter to an input vector.
    The filter is designed with the window method.
    This filter takes a few inputs: the sample_rate (will be passed as a parameter
    if the target node is not connected), the desired width of the
    transition to the stop band and the corresponding attentuation, and
    lastly the cutoff frequency."""

    sample_rate: int = params["sample_rate"]  # Hz
    filter_type: str = params["type"]

    # slope of the filter from pass to stop
    transition_width: float = params["transition_width"]  # Hz

    # how much db the signal is reduced by
    stop_band_attenuation: float = params["stop_band_attenuation"]  # dB

    # window_type: str = params["window"]
    cutoff_freq: float = params["cutoff_freq"]  # Hz

    if len(dc_inputs) != 1:
        raise ValueError(
            f"FIR node requires 1 input signal"
        )
    dc = dc_inputs[0]

    try:
        times = dc.x  # v[0].x['i']
        input_signal = dc.y  # this is the value of the signal
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
        x = test_x

    # first we need to define the nyquist rate ...
    nyq_rate: float = sample_rate / 2.0
    # ... then the transition width relative to this
    transition_width: float = transition_width / nyq_rate

    # Now compute order and Kaiser param for the fitler
    N, beta = signal.kaiserord(stop_band_attenuation, transition_width)

    # Now we create the filter with the Kaiser window ...
    filter = signal.firwin(times.size, cutoff_freq / nyq_rate, window=('kaiser', beta) ,pass_zero=filter_type, fs=sample_rate)

    # ... and then apply it to the signal
    filtered_x = signal.filtfilt(filter, 1.0, input_signal)

    # Now, there are two considerations to be had. Firstly,
    # there is a phase delay in the signal since we have applied finite
    # taps ...
    # phase_delay: float = 0.5 * (N - 1) / sample_rate
    # # ... and furthermore, the first N-1 samples are 'corrupted' in
    # # the sense that the filter 'sacrifies' them by the imposition
    # # of the initial conditions.
    # times = times[N - 1 :] - phase_delay
    # filtered_x = filtered_x[N - 1 :]

    return DataContainer(x=times, y=filtered_x)
