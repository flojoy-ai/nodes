import traceback
from flojoy import flojoy, Image
import numpy as np
import os
import requests

from utils.object_detection.object_detection import detect_object


@flojoy(deps={"opencv-python": "4.8.0.76"})
def OBJECT_DETECTION(default: Image) -> Image:
    """The OBJECT_DETECTION node detects objects in the input image, and returns an 'image' DataContainer with those objects highlighted.

    Inputs
    ------
    default : Image

    Returns
    -------
    Image
    """

    r = default.r
    g = default.g
    b = default.b
    a = default.a

    path = os.path.join(
        os.path.abspath(os.getcwd()), "PYTHON/utils/object_detection/yolov3.weights"
    )
    exists = os.path.exists(path)

    if not exists:
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
        return Image(r=red_channel, g=green_channel, b=blue_channel, a=alpha_channel)

    except Exception:
        print(traceback.format_exc())
        raise
