import numpy as np
from scipy import fft, signal
from flojoy import flojoy, DataContainer


@flojoy
def IFFT(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The IFFT performs the Inverse Discrete Fourier Transform on the input signal.
    With the IFFT algorith, the input signal will be transformed from the
    frequency domain back into the time domain.

    Parameters
    ----------
    real_signal: boolean
        whether the input signal is real (true) or complex (false)
    linspace_start: float
        the start of the initial linspace
    linspace_end: float
        the end of the initial linspace

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
    dc = dc_inputs[0]
    if dc.type != "ordered_pair":
        raise ValueError(
            f"unsupported DataContainer type passed to FFT node: '{dc.type}'"
        )

    real: bool = params["real_signal"]
    start: float = params["linspace_start"]
    end: float = params["linspace_end"]
    window_type = params["window_type"]

    fourier = fft.ifftshift(dc.y)
    frequency = dc.x

    N = 2 * (len(frequency) - 1)  # step of linspace
    x_time = np.linspace(start, end, N)

    result = fft.irfft(fourier) if real else fft.ifft(fourier)
    result = (
        result.real
        if window_type == "none"
        else result.real / signal.get_window(window_type, N)
    )
    return DataContainer(x=x_time, y=result)
