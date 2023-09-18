from flojoy import flojoy, Image, Matrix, DCNpArrayType
from typing import TypedDict
import numpy as np


class IMAGE_CHANNEL_OUTPUTS(TypedDict):
    r: Image
    g: Image
    b: Image
    a: Image


@flojoy
def CHANNEL_SPLIT(default: Image | Matrix) -> IMAGE_CHANNEL_OUTPUTS:
    """The CHANNEL_SPLIT node returns the rgba channels of an image into 4 separate images for direct visualization.

    While the notion of "splitting an image into RGBA channels" is inherently tied to coloured pictures, this function will attempt to make sense of multiple input types.

    Should the input be of type 'Image', then the function will return the RGBA channels.

    Should the input be of type 'Matrix', meaning ideally a 3D 'numpy' array of size (L, M, 3) or (L, M, 4), then the function will return each channel respectively.

    Returns
    -------
    IMAGE_CHANNEL_OUTPUTS
        The images, each channel itself is rendered with alpha=1,
        except the alpha channel itself.
    """

    try:
        if isinstance(default, Image):
            r = default.r
            g = default.g
            b = default.b
            a = default.a

        elif isinstance(default, Matrix):
            r = default.m[..., 0]
            g = default.m[..., 1]
            b = default.m[..., 2]
            a = np.zeros_like(r) if default.m.shape[-1] == 3 else default.m[..., 3]

            if default.m.shape[-1] != 3 or default.m.shape[-1] != 4:
                raise IndexError(
                    "Input array is not of sensible size to split channels"
                )
        else:
            raise TypeError("Unexpected type of the input argument.")

        zeros = np.zeros(r.shape, np.uint8)
        ones = 255 * np.ones(r.shape, np.uint8)

        return IMAGE_CHANNEL_OUTPUTS(
            r=Image(
                r=r,
                g=zeros,
                b=zeros,
                a=ones,
            ),
            g=Image(
                r=zeros,
                g=g,
                b=zeros,
                a=ones,
            ),
            b=Image(
                r=zeros,
                g=zeros,
                b=b,
                a=ones,
            ),
            a=Image(
                r=zeros,
                g=zeros,
                b=zeros,
                a=a,
            ),
        )
    except Exception as e:
        raise e
