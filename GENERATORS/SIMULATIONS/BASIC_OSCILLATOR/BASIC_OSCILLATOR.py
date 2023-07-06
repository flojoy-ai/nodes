import numpy as np
from flojoy import flojoy, OrderedPair
from scipy import signal
from typing import Literal


@flojoy(node_type="default")
def BASIC_OSCILLATOR(
    sample_rate: int = 100,
    time: int = 10,
    waveform: Literal["sine", "square", "triangle", "sawtooth"] = "sine",
    amplitude: float = 1,
    frequency: float = 1,
    offset: float = 0,
    phase: float = 0,
) -> OrderedPair:
    """The BASIC_OSCILLATOR node is a combination of LINSPACE and SINE node.
    It is useful for generating signals as it will generate a waveform with
    sample rate and the time in seconds as parameters.
    Parameters
    ----------
    sample_rate: int
        How many samples taken during a second
    time: int
        The total amount of time of the signal
    waveform: select
    amplitude: float
    frequency: float
    offset: float
    phase: float

    Returns
    -------
        x: time domain
        y: generated signal

    """
    samples = sample_rate * time
    x = np.linspace(0, time, samples)

    if waveform == "sine":
        y = offset + amplitude * np.sin(2 * np.pi * frequency * x + phase)
    elif waveform == "square":
        y = offset + amplitude * signal.square(2 * np.pi * frequency * x / 10 + phase)
    elif waveform == "triangle":
        y = offset + amplitude * signal.sawtooth(
            2 * np.pi * frequency * x / 10 + phase, 0.5
        )
    elif waveform == "sawtooth":
        y = offset + amplitude * signal.sawtooth(2 * np.pi * frequency / 10 * x + phase)

    return OrderedPair(x=x, y=y)
