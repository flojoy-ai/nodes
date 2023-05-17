import cv2
import os
from flojoy import flojoy, DataContainer
from PIL import Image
import numpy as np


@flojoy
def CAMERA(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """
    Takes a picture from a connected camera using OpenCV.
    If no camera is connected, an error would be thrown.
    """
    camera_ind:int = int(params["camera_ind"])
    try:
        camera = cv2.VideoCapture(camera_ind)

        if not camera.isOpened():
            raise cv2.error("Failed to open camera")

        result, frame = camera.read()

        if not result:
            raise cv2.error("Failed to capture image")
        camera.release()
        del camera

        # Split the image channels
        red_channel = frame[:, :, 0]
        green_channel = frame[:, :, 1]
        blue_channel = frame[:, :, 2]

        if frame.shape[2] == 4:
            alpha_channel = frame[:, :, 3]
        else:
            alpha_channel = None

        return DataContainer(
            type="image",
            r=red_channel,
            g=green_channel,
            b=blue_channel,
            a=alpha_channel,
        )

    except cv2.error as camera_error:
        raise camera_error


@flojoy
def CAMERA_MOCK(dc_inputs: list[DataContainer], params: dict):
    print("Running mock version of CAMERA node...")

    # Get the absolute path of the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the asset file
    file_path = os.path.join(
        current_dir, "assets", "astronaut.png"
    )  # Load example image.
    print("File to be loaded: ", file_path)
    f = Image.open(file_path)
    img_array = np.array(f.convert("RGBA"))
    red_channel = img_array[:, :, 0]
    green_channel = img_array[:, :, 1]
    blue_channel = img_array[:, :, 2]
    if img_array.shape[2] == 4:
        alpha_channel = img_array[:, :, 3]
    else:
        alpha_channel = None
    return DataContainer(
        type="image", r=red_channel, g=green_channel, b=blue_channel, a=alpha_channel
    )
