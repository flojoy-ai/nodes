from typing import Optional
from flojoy import SerialConnection, flojoy, DataContainer, OrderedTriple
from TauLidarCommon.frame import FrameType, Frame
from TauLidarCamera.camera import Camera

import numpy as np


@flojoy(deps={"TauLidarCamera": "0.0.5"}, inject_connection=True)
def TAU_LIDAR(
    connection: SerialConnection, default: Optional[DataContainer] = None
) -> OrderedTriple:
    camera = connection.get_handle()
    frame: Frame | None = camera.readFrame(FrameType.DISTANCE)
    if frame is None:
        raise IOError("Failed to read frame from LiDAR Camera")

    points = frame.points_3d
    x = np.zeros(len(points))
    y = np.zeros(len(points))
    z = np.zeros(len(points))
    colors = np.zeros((len(points), 4))

    for i, p in enumerate(frame.points_3d):
        x[i] = p[0] * 100
        y[i] = p[1] * 100
        z[i] = p[2] * 100
        colors[i] = np.array([p[3] / 255, p[4] / 255, p[5] / 255, 1])

    return OrderedTriple(x=x, y=y, z=z, extra={"colors": colors})
