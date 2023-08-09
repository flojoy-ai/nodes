from flojoy import flojoy, Image
import cv2
import numpy as np
from typing import Literal


@flojoy
def IMAGE_SMOOTHING(
    default: Image,
    kernel: int = 5,
    smoothing_type: Literal["average", "gaussian", "median", "bilateral"] = "average",
) -> Image:
    """
    Apply image smoothing operation on the input `DataContainer` class,
    specifically for the 'Image' type,
    represented by the RGB(A) channels.

    Note: for "gaussian" and "median" type, you are only allowed odd number for kernel value.

    Args:
    dc_inputs (list[DataContainer]): List of DataContainer objects containing
    image channels.
    params (dict): Additional parameters for image smoothing.

    Params:
    kernel: The strength of the smoothing. A large value will lead
    to stronger smoothing. smoothing_type: The type of smoothing to use
    (https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html).

    Returns:
    DataContainer: A `DataContainer` class of type 'Image' representing the
    output image with image smoothing results.

    Raises:
    Exception: If an error occurs during smoothing.
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
        match smoothing_type:
            case "average":
                image = cv2.blur(rgba_image, (kernel, kernel))
            case "gaussian":
                assert kernel & 1, "Kernel must be odd for 'gaussian' smoothing."
                image = cv2.GaussianBlur(rgba_image, (kernel, kernel), 0)
            case "median":
                assert kernel & 1, "Kernel must be odd for 'median' smoothing."
                image = cv2.medianBlur(rgba_image, kernel)
            case "bilateral":
                rgba_image = cv2.cvtColor(rgba_image, cv2.COLOR_BGRA2BGR)
                image = cv2.bilateralFilter(rgba_image, kernel, kernel * 5, kernel * 5)
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
