import traceback
from flojoy import flojoy, DataContainer
import numpy as np
import os
import requests

from utils.object_detection.object_detection import detect_object


@flojoy
def OBJECT_DETECTION(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Performs  object detection on the input `DataContainer` class, specifically for the 'image' type,
    represented by the RGB(A) channels.

    Returns:
    ----------
        DataContainer: A `DataContainer` class of type 'image' representing the output image with object detection results.

    Parameters:
    ----------
        None in this node.

    Raises:
    ----------
        Exception: If an error occurs during object detection.
    """
    dc_input: DataContainer = dc_inputs[0]
    if dc_input.type != "image":
        raise ValueError(
            f"unsupported DataContainer type passed to OBJECT_DETECTION node: '{dc_input.type}'"
        )
    r = dc_input.r
    g = dc_input.g
    b = dc_input.b
    a = dc_input.a

    path = os.path.join(
        os.path.abspath(os.getcwd()), "utils/object_detection/yolov3.weights"
    )

    if not path:
        print("Downloading yolov3 weights for object detection.")
        print("Download may take up to a minute.")
        url = "https://pjreddie.com/media/files/yolov3.weights"
        r = requests.get(url, allow_redirects=True)
        open(path, "wb").write(r.content)

    if a is not None:
        nparr = np.stack((r, g, b, a), axis=2)
    else:
        nparr = np.stack((r, g, b), axis=2)
    try:
        img_array = detect_object(nparr)
        red_channel = img_array[:, :, 0]
        green_channel = img_array[:, :, 1]
        blue_channel = img_array[:, :, 2]
        if img_array.shape[2] == 4:
            alpha_channel = img_array[:, :, 3]
        else:
            alpha_channel = None
        return DataContainer(
            type="image",
            r=red_channel,
            g=green_channel,
            b=blue_channel,
            a=alpha_channel,
        )

    except Exception:
        print(traceback.format_exc())
        raise
