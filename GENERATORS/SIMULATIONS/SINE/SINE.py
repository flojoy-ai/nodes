import numpy as np
from flojoy import flojoy, OrderedPair


@flojoy
def SINE(
    default,
    amplitude: float = 1,
    frequency: float = 1,
    offset: float = 0,
    phase: float = 0,
    waveform: str = "sine",
) -> OrderedPair:
    A = amplitude
    F = frequency
    Y0 = offset

    if isinstance(default, OrderedPair):
        x = default.y
    else:
        x = default.v

    y = np.ndarray(x.shape)
    if waveform == "sine":
        y = Y0 + A * np.sin(2 * np.pi * F * x + phase)

    return OrderedPair(x=x, y=y)
