from flojoy import flojoy, DataContainer
import cv2
import numpy as np


@flojoy
def IMAGE_SMOOTHING(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """
    Apply image smoothing operation on the input `DataContainer` class, specifically for the 'image' type,
    represented by the RGB(A) channels.
    """
    dc_input = dc_inputs[0]
    if dc_input.type != "image":
        raise ValueError(
            f"unsupported DataContainer type passed to IMAGE_SMOOTHING node: '{dc_input.type}'"
        )
    r = dc_input.r
    g = dc_input.g
    b = dc_input.b
    a = dc_input.a
    kernel = int(params.get("kernel", 5))
    smoothing_type = params.get("smoothing_type", "average")

    if a is not None:
        rgba_image = np.stack((r, g, b, a), axis=2)
    else:
        rgba_image = np.stack((r, g, b), axis=2)

    try:
        match smoothing_type:
            case "average":
                image = cv2.blur(rgba_image, (kernel, kernel))
            case "gaussian":
                image = cv2.GaussianBlur(rgba_image, (kernel, kernel), 0)
            case "median":
                image = cv2.medianBlur(rgba_image, kernel)
            case "bilateral":
                image = cv2.bilateralFilter(rgba_image, kernel, kernel * 5, kernel * 5)
        try:
            r, g, b, a = cv2.split(image)
        except:
            r, g, b = cv2.split(image)
        if a is None:
            a = None
        return DataContainer(
            type="image",
            r=r,
            g=g,
            b=b,
            a=a,
        )
    except Exception as e:
        raise e
