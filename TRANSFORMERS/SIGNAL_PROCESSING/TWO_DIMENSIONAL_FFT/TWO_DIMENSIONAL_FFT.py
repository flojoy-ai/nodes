from scipy import fft
from flojoy import flojoy, DataContainer
import pandas as pd
import numpy as np

## Helper functions to rescale a frequency-image to [0, 255] and save
remmax = lambda x: x / x.max()
remmin = lambda x: x - np.amin(x, axis=(0, 1), keepdims=True)
touint8 = lambda x: (remmax(remmin(x)) * (256 - 1e-4)).astype(int)


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
    match dc.type:
        case "greyscale":
            input = dc.m
            result = fft.rfft2(input).real if real else fft.fft2(input).real
            # result = 20 * np.log10(result)
            return DataContainer(type="grayscale", m=result)
        case "dataframe":
            input = pd.DataFrame(dc.m)
            fourier = fft.rfft2(input).real if real else fft.fft2(input).real
            result = pd.DataFrame(columns=fourier.columns, index=fourier.index)
            return DataContainer(type="dataframe", m=result)
        case "image":
            r = dc.r
            g = dc.g
            b = dc.b
            a = dc.a

            if a is None:
                img = np.stack((r, g, b), axis=2)
            else:
                img = np.stack((r, g, b, a), axis=2)

            result = (
                fft.rfft2(img, axes=[0, 1])
                if real
                else fft.fft2(img, axes=[0, 1])
            )
            result = np.log(np.abs(result))
            result = touint8(result)

            # when result is a 2d array
            red = green = blue = result
            alpha = None
            if len(result.shape) == 3:
                # Color image
                if result.shape[2] == 3:
                    red, green, blue = (
                        result[:, :, 0],
                        result[:, :, 1],
                        result[:, :, 2],
                    )
                elif result.shape[2] == 4:
                    red, green, blue, alpha = (
                        result[:, :, 0],
                        result[:, :, 1],
                        result[:, :, 2],
                        result[:, :, 3],
                    )
            print(f"The red value is {red[0][0]}")
            return DataContainer(
                type="image",
                r=red,
                g=green,
                b=blue,
                a=alpha,
            )
