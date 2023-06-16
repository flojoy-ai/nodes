from scipy import fft
from flojoy import flojoy, DataContainer
from PIL import Image
import pandas as pd
import numpy as np

# ## Helper functions to rescale a frequency-image to [0, 255] and save
# remmax = lambda x: x / x.max()
# remmin = lambda x: x - np.amin(x, axis=(0, 1), keepdims=True)
# touint8 = lambda x: (remmax(remmin(x)) * (256 - 1e-4)).astype(int)

def touint8(x):
    min = x.min()
    max = x.max()
    return (x - min) / (max - min) * 255

@flojoy
def TWO_DIMENSIONAL_FFT(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The TWO_DIMENSIONAL_FFT node performs a two-dimensional fourier transform on the input matrix.
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
            f"TWO_DIMENSIONAL_FFT node requires 1 input, but {len(dc_inputs)} was given! "
        )
    dc = dc_inputs[0]
    if dc.type != "grayscale" and dc.type != "dataframe" and dc.type != "image":
        raise ValueError(
            f"unsupported DataContainer type passed to TWO_DIMENSIONAL_FFT node: '{dc.type}'"
        )
    real = params["real_signal"]
    color = params["color"]
    match dc.type:
        case "greyscale":
            input = dc.m
            fourier = fft.rfft2(input) if real else fft.fft2(input)
            fourier = np.log10(np.abs(fourier))
            return DataContainer(type="grayscale", m=fourier)
        case "dataframe":
            input = pd.DataFrame(dc.m)
            fourier = fft.rfft2(input).real if real else fft.fft2(input).real
            result = pd.DataFrame(columns=fourier.columns, index=fourier.index)
            return DataContainer(type="dataframe", m=result)
        case "image":
            red = dc.r
            green = dc.g
            blue = dc.b
            alpha = dc.a
            print(red)
            if color != "grayscale":
                fourier = fft.rfft2(locals()[color], axes=[0, 1]) if real else fft.fft2(locals()[color], axes=[0, 1])
            else:
                if alpha is None:
                    rgba_image = np.stack((red, green, blue), axis=2)
                else:
                    rgba_image = np.stack((red, green, blue, alpha), axis=2)
                image = Image.fromarray(rgba_image)
                image = image.convert("L")
                grayscale = np.array(image)
                fourier = fft.rfft2(grayscale) if real else fft.fft2(grayscale)
            fourier = np.log10(np.abs(fourier))
            fourier = touint8(fourier)
            return DataContainer(type="grayscale", m=fourier)
