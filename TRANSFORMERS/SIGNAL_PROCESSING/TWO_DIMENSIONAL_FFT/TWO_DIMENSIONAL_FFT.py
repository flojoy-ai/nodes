from scipy import fft
from flojoy import flojoy, DataContainer
from PIL import Image
import pandas as pd
import numpy as np


def extrapolate(x):
    return (x - x.min()) / (x.max() - x.min())


@flojoy
def TWO_DIMENSIONAL_FFT(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The TWO_DIMENSIONAL_FFT node performs a two-dimensional fourier transform on the input matrix.
    With the FFT algorithm, the input matrix will undergo a change of basis
    from the space domain into the frequency domain.

    Parameters
    ----------
    real_input: boolean
        true if the input matrix is consists of only real numbers, false otherwise
    color: select
        If the input is an RGBA or RGB image, this parameter selects the color channel to perform fft on

    Returns
    -------
    image
        The frequency spectrum of the color channel
    """
    if len(dc_inputs) != 1:
        raise ValueError(
            f"TWO_DIMENSIONAL_FFT node requires 1 input, but {len(dc_inputs)} was given! "
        )
    dc = dc_inputs[0]
    if dc.type not in ["grayscale", "dataframe", "image", "matrix"]:
        raise ValueError(
            f"unsupported DataContainer type passed to TWO_DIMENSIONAL_FFT node: '{dc.type}'"
        )
    real = params["real_signal"]
    color = params["color"]

    match dc.type:
        case "greyscale" | "matrix":
            input = dc.m
            fourier = fft.rfft2(input) if real else fft.fft2(input)
            if dc.type == "matrix":
                fourier = fourier.real
                return DataContainer(type="matrix", m=fourier)
        case "dataframe":
            input = pd.DataFrame(dc.m)
            fourier = fft.rfft2(input) if real else fft.fft2(input)
            fourier = np.log10(np.abs(fourier))
            fourier = extrapolate(fourier)
            result = pd.DataFrame(columns=fourier.columns, index=fourier.index)
            return DataContainer(type="dataframe", m=result)
        case "image":
            red = dc.r
            green = dc.g
            blue = dc.b
            alpha = dc.a
            if color == "grayscale":
                if alpha is None:
                    rgba_image = np.stack((red, green, blue), axis=2)
                else:
                    rgba_image = np.stack((red, green, blue, alpha), axis=2)
                try:
                    image = Image.fromarray(rgba_image)
                except TypeError:
                    image = Image.fromarray((rgba_image * 255).astype(np.uint8))
                image = image.convert("L")
                grayscale = np.array(image)
                fourier = fft.rfft2(grayscale) if real else fft.fft2(grayscale)
            else:
                fourier = (
                    fft.rfft2(locals()[color], axes=[0, 1])
                    if real
                    else fft.fft2(locals()[color], axes=[0, 1])
                )

    fourier = np.log10(np.abs(fourier))
    fourier = extrapolate(fourier)
    return DataContainer(type="image", r=fourier, g=fourier, b=fourier, a=None)
