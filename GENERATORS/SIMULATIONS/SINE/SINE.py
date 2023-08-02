import numpy as np
from flojoy import flojoy, OrderedPair, Vector
from typing import Literal


@flojoy
def SINE(
    default: OrderedPair | Vector,
    amplitude: float = 1,
    frequency: float = 1,
    offset: float = 0,
    phase: float = 0,
    waveform: Literal["sine", "square", "triangle", "sawtooth"] = "sine",
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
