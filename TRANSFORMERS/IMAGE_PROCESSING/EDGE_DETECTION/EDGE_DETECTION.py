from flojoy import flojoy, DataContainer
import cv2
import numpy as np
from PIL import ImageFilter, Image


@flojoy
def EDGE_DETECTION(
    default: DataContainer,
) -> DataContainer:
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
    dc_input = dc_inputs[0]
    if dc_input.type != "image":
        raise ValueError(
            f"unsupported DataContainer type passed to EDGE_DETECTION node: '{dc_input.type}'"
        )
    r = dc_input.r
    g = dc_input.g
    b = dc_input.b
    a = dc_input.a
    if a is not None:
        rgba_image = np.stack((r, g, b, a), axis=2)
    else:
        rgba_image = np.stack((r, g, b), axis=2)
    try:
        image = Image.fromarray(rgba_image)
        image = image.convert("L")
        image = image.filter(ImageFilter.FIND_EDGES)
        image = image.convert("RGB")
        image = np.array(image)
        try:
            (r, g, b, a) = cv2.split(image)
        except:
            (r, g, b) = cv2.split(image)
        if a is None:
            a = None
        return DataContainer(type="image", r=r, g=g, b=b, a=a)
    except Exception as e:
        raise e
