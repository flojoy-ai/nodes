from typing import Literal
import cv2
import os
from flojoy import flojoy, DataContainer
from PIL import Image
import numpy as np


@flojoy
def CAMERA(
    default: DataContainer,
    camera_ind: int = -1,
    resolution: Literal[
        "default", "640x360", "640x480", "1280x720", "1920x1080"
    ] = "default",
) -> DataContainer:
    """The CAMERA node acquires an image using the selected camera.
    If no camera is detected, an error would be thrown.

    Parameters:
    ----------
    camera_ind : int
        Camera index (i.e. camera identifier)
    resolution : select
        Camera resolution. Choose from a few options.

    Returns:
    ----------
    DataContainer:
        type 'image'
    """
    camera_ind: int = params["camera_ind"]
    resolution: str = params["resolution"]
    try:
        camera = cv2.VideoCapture(camera_ind)
        if resolution != "default":
            resolution = resolution.split("x")
            try:
                camera.set(cv2.CAP_PROP_FRAME_WIDTH, int(resolution[0]))
                camera.set(cv2.CAP_PROP_FRAME_HEIGHT, int(resolution[1]))
            except cv2.error as camera_error:
                print(f"Invalid resolution ({resolution}). Try a lower value.")
                raise camera_error
        if not camera.isOpened():
            raise cv2.error("Failed to open camera")
        (result, BGR_img) = camera.read()
        if not result:
            raise cv2.error("Failed to capture image")
        camera.release()
        del camera
        RGB_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2RGB)
        red_channel = RGB_img[:, :, 0]
        green_channel = RGB_img[:, :, 1]
        blue_channel = RGB_img[:, :, 2]
        if RGB_img.shape[2] == 4:
            alpha_channel = RGB_img[:, :, 3]
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
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "assets", "astronaut.png")
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
