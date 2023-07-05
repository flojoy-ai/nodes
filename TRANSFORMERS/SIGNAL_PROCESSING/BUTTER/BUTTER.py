from scipy import signal
import numpy as np
from flojoy import flojoy, OrderedPair


@flojoy
def BUTTER(default: OrderedPair) -> OrderedPair:
    """Apply a butterworth filter to an input vector"""

    print("Butterworth inputs:", default)

    sig = default.y

    sos = signal.butter(10, 15, "hp", fs=1000, output="sos")
    filtered = signal.sosfilt(sos, sig)

    return OrderedPair(x=sig, y=filtered)
