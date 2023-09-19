import cv2
from flojoy import CameraDevice, flojoy, DataContainer, Stateful
from flojoy.connection_manager import DeviceConnectionManager
from typing import Optional, Literal


@flojoy(deps={"opencv-python-headless": "4.7.0.72"})
def OPEN_WEBCAM(
    camera: Optional[CameraDevice] = None,
    default: Optional[DataContainer] = None,
) -> Stateful:
    if not camera:
        raise ValueError("No camera selected")

    cam = cv2.VideoCapture(camera.get_id())
    DeviceConnectionManager.register_connection(camera, cam)

    return Stateful(obj=cam)
