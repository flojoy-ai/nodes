from scipy import fft
from flojoy import flojoy, DataFrame, Matrix, Image, Grayscale
from typing import Literal
from PIL import Image as PillowImage
import pandas as pd
import numpy as np


def extrapolate(x):
    return (x - x.min()) / (x.max() - x.min())


@flojoy
def TWO_DIMENSIONAL_FFT(
    default: Grayscale | DataFrame | Image | Matrix,
    real_signal: bool = True,
    color: Literal["red", "green", "blue", "grayscale"] = "red",
) -> Matrix | DataFrame | Image:
    """The TWO_DIMENSIONAL_FFT node performs a two-dimensional fourier transform on the input matrix.
    With the FFT algorithm, the input matrix will undergo a change of basis
    from the space domain into the frequency domain.
    grayscale, dataframe, image or matrix

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
    match default.type:
        case "grayscale" | "matrix":
            input = default.m
            fourier = fft.rfft2(input) if real_signal else fft.fft2(input)
            if default.type == "matrix":
                fourier = fourier.real
                return Matrix(m=fourier)
        case "dataframe":
            input: pd.DataFrame = pd.DataFrame(default.m)
            fourier = fft.rfft2(input) if real_signal else fft.fft2(input)
            fourier = fourier.real
            result = pd.DataFrame(columns=fourier.columns, index=fourier.index)
            return DataFrame(df=result)
        case "image":
            red = default.r
            green = default.g
            blue = default.b
            alpha = default.a
            if color == "grayscale":
                if alpha is None:
                    rgba_image = np.stack((red, green, blue), axis=2)
                else:
                    rgba_image = np.stack((red, green, blue, alpha), axis=2)
                try:
                    image = PillowImage.fromarray(rgba_image)
                except TypeError:
                    image = PillowImage.fromarray((rgba_image * 255).astype(np.uint8))
                image = image.convert("L")
                grayscale = np.array(image)
                fourier = fft.rfft2(grayscale) if real_signal else fft.fft2(grayscale)
            else:
                fourier = (
                    fft.rfft2(locals()[color], axes=[0, 1])
                    if real_signal
                    else fft.fft2(locals()[color], axes=[0, 1])
                )

    fourier = np.log10(np.abs(fourier))
    fourier = extrapolate(fourier)
    return Image(r=fourier, g=fourier, b=fourier, a=None)
