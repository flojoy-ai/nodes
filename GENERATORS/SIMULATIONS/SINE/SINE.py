import numpy as np
from flojoy import flojoy, OrderedPair, ParameterTypes
from scipy import signal


@flojoy
def SINE(
    default: OrderedPair,
    amplitude: ParameterTypes.FLOAT = 1,
    frequency: ParameterTypes.FLOAT = 1,
    offset: ParameterTypes.FLOAT = 0,
    phase: ParameterTypes.FLOAT = 0,
    waveform: ParameterTypes.SELECT["sine", "square", "triangle", "sawtooth"] = "sine",
) -> OrderedPair:
    x = default.y
    A = amplitude
    F = frequency
    Y0 = offset
    if waveform == "sine":
        y = Y0 + A * np.sin(2 * np.pi * F * x + phase)
    elif waveform == "square":
        y = Y0 + A * signal.square(2 * np.pi * F * x / 10 + phase)
    elif waveform == "triangle":
        y = Y0 + A * signal.sawtooth(2 * np.pi * F * x / 10 + phase, 0.5)
    elif waveform == "sawtooth":
        y = Y0 + A * signal.sawtooth(2 * np.pi * F / 10 * x + phase)
    return OrderedPair(x=x, y=y)
