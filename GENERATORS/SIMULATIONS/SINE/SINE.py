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
    waveform: Literal["sine"] = "sine",
) -> OrderedPair:
    """The SINE node generates a waveform function. With the shape being defined
    by the input.

    Inputs
    ------
    default : OrderedPair|Vector
        Input that defines the x axis values of the function and output.

    Parameters
    ----------
    waveform : select
        The waveform type of the wave.
    amplitude : float
        The amplitude of the wave.
    frequency : float
        The wave frequency in radians/2pi.
    offset : float
        The y axis offset of the function.
    phase : float
        The x axis offset of the function.

    Returns
    -------
    OrderedPair
        x: the input v or x values
        y: the resulting sine function
    """
    A = amplitude
    F = frequency
    Y0 = offset

    if isinstance(default, OrderedPair):
        x = default.y
    else:
        x = default.v


    if waveform == "sine":
        y = Y0 + A * np.sin(2 * np.pi * F * x + phase)

    return OrderedPair(x=x, y=y)
