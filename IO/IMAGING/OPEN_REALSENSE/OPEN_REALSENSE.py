from flojoy import CameraDevice, flojoy, OrderedTriple, DataContainer
from flojoy.connection_manager import DeviceConnectionManager
from typing import Literal, Optional

import pyrealsense2 as rs


@flojoy(deps={"pyrealsense2": "2.54.2.5684"})
def OPEN_REALSENSE(
        device: CameraDevice,
        width: int = 640,
        height: int = 480,
        rs_format: Literal["z16", "xyz32f"] = 'z16',
        framerate: int = 30,
        default: Optional[DataContainer] = None) -> Optional[DataContainer]:
    pipeline = rs.pipeline()
    config = rs.config()

    match rs_format:
        case "z16":
            fmt = rs.format.z16
        case "xyz32f":
            fmt = rs.format.xyz32f

    config.enable_stream(rs.stream.depth, width, height, fmt, framerate)

    pipeline.start(config)

    DeviceConnectionManager.register_connection(device, pipeline)

    return None
