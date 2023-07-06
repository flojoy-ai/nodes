from flojoy import flojoy, Image, DefaultParams
import cv2
import numpy as np
from PIL import ImageFilter, Image as PILImage


@flojoy
def EDGE_DETECTION(default: Image, params: DefaultParams) -> Image:
    """The EDGE_DETECTION node detects edges in the image passed to it.
    This is done through the the Pillow image filter FIND_EDGES.
    Note that the image is converted to greyscale during this processing.

    Parameters
    ----------
    None

    Returns
    -------
    image
        The image with detected edges in white.
    """
    r = default.r
    g = default.g
    b = default.b
    a = default.a

    if a is not None:
        rgba_image = np.stack((r, g, b, a), axis=2)

    else:
        rgba_image = np.stack((r, g, b), axis=2)

    try:
        image = PILImage.fromarray(rgba_image)
        image = image.convert("L")
        image = image.filter(ImageFilter.FIND_EDGES)
        image = image.convert("RGB")
        image = np.array(image)

        try:
            r, g, b, a = cv2.split(image)
        except:
            r, g, b = cv2.split(image)
        if a is None:
            a = None
        return Image(
            r=r,
            g=g,
            b=b,
            a=a,
        )
    except Exception as e:
        raise e
