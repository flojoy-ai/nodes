from scipy import signal
from flojoy import flojoy, DataContainer


@flojoy
def BUTTER(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The BUTTER node applies a butterworth filter to an input vector

    Parameters
    ----------
    filter_order: int
        The intensity of the filter
    critical_frequency: array or int
        The frequency where the filter takes effect. For lowpass and highpass, takes in a scalar.
        For bandpass and bandstop, takes in array with the length of two
    btype: select
        The type of the filter
    sample_rate: int
        The sample rate of the input signal

    Returns
    -------
        x: time domain
        y: filtered signal
    """
    if len(dc_inputs) != 1:
        raise ValueError(
            f"BUTTER node requires 1 input signal, but {len(dc_inputs)} was given!"
        )
    dc = dc_inputs[0]
    sig: float = dc.y
    order: int = params["filter_order"]
    Wn: int = params["critical_frequency"]  # hz
    btype: str = params["btype"]
    fs: int = params["sample_rate"]  # hz

    sos = signal.butter(N=order, Wn=Wn, btype=btype, fs=fs, output="sos")
    #    sos = signal.butter(10, 15, "hp", fs=1000, output="sos")
    filtered = signal.sosfilt(sos, sig)

    return DataContainer(x=dc.x, y=filtered)
