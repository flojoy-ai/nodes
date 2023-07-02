from scipy import signal
from flojoy import flojoy, DataContainer
import numpy as np


@flojoy
def FIR(
    default: DataContainer,
    sample_rate: float = 100,
    transition_width: float = 5.0,
    stop_band_attenuation: float = 60,
    cutoff_freq: float = 10.0,
) -> DataContainer:
    """Apply a low-pass FIR filter to an input vector. This
    filter takes a few inputs: the sample_rate (will be passed as a parameter
    if the target node is not connected), the desired width of the
    transition to the stop band and the corresponding attentuation, and
    lastly the cutoff frequency."""
    sample_rate: float = params["sample_rate"]
    transition_width: float = params["transition_width"]
    stop_band_attenuation: float = params["stop_band_attenuation"]
    cutoff_freq: float = params["cutoff_freq"]
    print(
        f"FIR params: {[sample_rate, transition_width, stop_band_attenuation, cutoff_freq]}"
    )
    try:
        times = dc_inputs[1].y
        x = dc_inputs[0].y
    except IndexError:
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
    nyq_rate: float = sample_rate / 2.0
    transition_width: float = transition_width / nyq_rate
    (N, beta) = signal.kaiserord(stop_band_attenuation, transition_width)
    taps = signal.firwin(N, cutoff_freq / nyq_rate, window=("kaiser", beta))
    filtered_x = signal.lfilter(taps, 1.0, x)
    phase_delay: float = 0.5 * (N - 1) / sample_rate
    times = times[N - 1 :] - phase_delay
    filtered_x = filtered_x[N - 1 :]
    return DataContainer(x=times, y=filtered_x)
