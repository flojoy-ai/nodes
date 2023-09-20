import cv2
from flojoy import CameraDevice, flojoy, DataContainer
from flojoy.connection_manager import DeviceConnectionManager
from typing import Optional, Literal


@flojoy(deps={"opencv-python-headless": "4.7.0.72"})
def OPEN_WEBCAM(
    camera: CameraDevice,
    default: Optional[DataContainer] = None,
) -> Optional[DataContainer]:
    if not camera:
        raise ValueError("No camera selected")

    cam = cv2.VideoCapture(camera.get_id())
    DeviceConnectionManager.register_connection(camera, cam)

    return None
