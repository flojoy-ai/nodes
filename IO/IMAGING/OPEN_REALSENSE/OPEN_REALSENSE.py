from flojoy import CameraDevice, flojoy, OrderedTriple, DataContainer
from flojoy.connection_manager import DeviceConnectionManager
from typing import Optional

import pyrealsense2 as rs


@flojoy(deps={"pyrealsense2": "2.54.2.5684"})
def OPEN_REALSENSE(
        device: CameraDevice,
        default: Optional[DataContainer] = None) -> Optional[DataContainer]:
    pipeline = rs.pipeline()
    config = rs.config()
    pipeline_wrapper = rs.pipeline_wrapper(pipeline)
    pipeline_profile = config.resolve(pipeline_wrapper)

    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

    pipeline.start(config)

    DeviceConnectionManager.register_connection(device, pipeline)

    return None
