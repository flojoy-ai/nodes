import numpy as np
from flojoy import flojoy, DataContainer
from scipy import signal


@flojoy
def BASIC_OSCILLATOR(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The BASIC_OSCILLATOR node is a combination of LINSPACE and SINE node.
    It is useful for generating signals as it will generate a waveform with
    sample rate and the time in seconds as parameters.
    Parameters
    ----------
    sample_rate: int
        How many samples taken during a second
    time: int
        The total amount of time of the signal

    Returns
    -------
        x: time domain
        y: generated signal
    """
    sample_rate: int = params["sample_rate"]  # Hz
    time: int = params["time"]  # in seconds

    samples = sample_rate * time
    x = np.linspace(0, time, samples)

    waveform = params["waveform"]
    A = params["amplitude"]
    F = params["frequency"]
    Y0 = params["offset"]
    PHASE = params["phase"]

    if waveform == "sine":
        y = Y0 + A * np.sin(2 * np.pi * F * x + PHASE)
    elif waveform == "square":
        y = Y0 + A * signal.square(2 * np.pi * F * x / 10 + PHASE)
    elif waveform == "triangle":
        y = Y0 + A * signal.sawtooth(2 * np.pi * F * x / 10 + PHASE, 0.5)
    elif waveform == "sawtooth":
        y = Y0 + A * signal.sawtooth(2 * np.pi * F / 10 * x + PHASE)

    return DataContainer(x=x, y=y)
