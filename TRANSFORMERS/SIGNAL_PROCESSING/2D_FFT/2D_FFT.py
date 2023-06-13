from scipy import fft
from flojoy import flojoy, DataContainer
import pandas as pd

@flojoy
def TWO_DIMENSION_FFT(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The 2D_FFT node performs a two-dimensional fourier transform on the input matrix.
    With the FFT algorithm, the input matrix will undergo a change of basis
    from the space domain into the frequency domain.

    Parameters
    ----------
        real_input: boolean
            true if the input matrix is consists of only real numbers, false otherwise

    Returns
    -------
        grayscale
    """
    if len(dc_inputs) != 1:
        raise ValueError(
            f"2D_FFT node requires 1 input, but {len(dc_inputs)} was given! "
        )
    dc = dc_inputs[0]
    if dc.type != "grayscale" or "dataframe" or "image":
        raise ValueError(
            f"unsupported DataContainer type passed to 2D_FFT node: '{dc.type}'"
        )
    real = params["real_signal"]
    if dc.type == "greyscale":
        input = dc.m
        result = fft.rfft2(input) if real else fft.fft2(input).real
    elif dc.type == "dataframe":
        input = pd.DataFrame(dc.m)
        fourier = fft.rfft2(input) if real else fft.fft2(input)
        result = pd.DataFrame(columns=fourier.columns, index=fourier.index)
    elif dc.type == "image":
        input = dc.a
        result = fft.rfft2(input) if real else fft.fft2(input).real
    return DataContainer(type="grayscale", m=result)