import numpy as np
from flojoy import flojoy, OrderedPair, Vector
from scipy import signal
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
    """The SINE node generates periodic signal with a given input

    Parameters
    ----------
    amplitude : float
    frequency : float
    offset : float
    phase : float
    waveform : select

    Returns
    -------
    OrderedPair
        x: input vector
        y: generated signal
    """

    match default:
        case OrderedPair():
            x = default.y
        case _:
            x = default.v

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
    else:
        raise ValueError(f"The select type {waveform} is not supported!")

    return OrderedPair(x=x, y=y)
