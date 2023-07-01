from scipy import signal
import numpy as np
from flojoy import flojoy, DataContainer, DefaultParams


@flojoy
def BUTTER(default: DataContainer, default_params: DefaultParams) -> DataContainer:
    """Apply a butterworth filter to an input vector"""
    print("Butterworth inputs:", dc_inputs)
    sig = dc_inputs[0].y
    sos = signal.butter(10, 15, "hp", fs=1000, output="sos")
    filtered = signal.sosfilt(sos, sig)
    return DataContainer(x=sig, y=filtered)
