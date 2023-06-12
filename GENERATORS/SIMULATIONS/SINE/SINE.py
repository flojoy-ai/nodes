import numpy as np
from flojoy import flojoy, DataContainer
from scipy import signal


@flojoy
def SINE(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    valid_waveforms = ["sine", "square", "triangle", "sawtooth"]
    x = None
    if dc_inputs.__len__() > 0:
        x = dc_inputs[0].y

    waveform = params["waveform"]
    A = params["amplitude"]
    F = params["frequency"]
    Y0 = params["offset"]
    PHASE = params["phase"]
    if waveform not in valid_waveforms:
        waveform = valid_waveforms[0]
        print("invalid waveform passed as param, using default:", waveform)

    if waveform == "sine":
        y = Y0 + A * np.sin(2 * np.pi * F * x + np.radians(PHASE))
    elif waveform == "square":
        y = Y0 + A * signal.square(2 * np.pi * F * x / 10 + np.radians(PHASE))
    elif waveform == "triangle":
        y = Y0 + A * signal.sawtooth(2 * np.pi * F * x / 10 + np.radians(PHASE), 0.5)
    elif waveform == "sawtooth":
        y = Y0 + A * signal.sawtooth(2 * np.pi * F / 10 * x + np.radians(PHASE))

    return DataContainer(x=x, y=y)
