from scipy import fft
from flojoy import flojoy, DataContainer
import pandas as pd


@flojoy
def IFFT(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The IFFT performs the Inverse Discrete Fourier Transform on the input signal.
    With the IFFT algorith, the input signal will be transformed from the
    frequency domain back into the time domain.

    Parameters
    ----------
    real_signal: boolean
        whether the input signal is real (true) or complex (false)

    Returns
    -------
    ordered_pair
        x = time
        y = reconstructed signal
    """
    if len(dc_inputs) != 1:
        raise ValueError(
            f"FFT node requires 1 input signal, but {len(dc_inputs)} was given!"
        )
    if dc_inputs[0].type != "dataframe":
        raise ValueError(
            f"unsupported DataContainer type passed to FFT node: '{dc.type}'"
        )
    dc: pd.DataFrame = dc_inputs[0].m
    real: bool = params["real_signal"]

    x = dc["x"].to_numpy()
    realValue = dc["real"].to_numpy()
    imagValue = dc["imag"].to_numpy()

    fourier = realValue + 1j * imagValue

    result = fft.irfft(fourier) if real else fft.ifft(fourier, len(x))
    result = result.real
    return DataContainer(x=x, y=result)
