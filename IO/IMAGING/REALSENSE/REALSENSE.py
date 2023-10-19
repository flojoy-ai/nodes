import numpy as np
import cv2
from flojoy import CameraConnection, DataContainer, flojoy, OrderedTriple
from typing import Optional
import pyrealsense2 as rs

decimate = rs.decimation_filter(4)


@flojoy(inject_connection=True)
def REALSENSE(connection: CameraConnection,
              default: Optional[DataContainer] = None) -> OrderedTriple:
    pipeline = connection.get_handle()

    frames = pipeline.wait_for_frames()
    depth = frames.get_depth_frame()
    depth = decimate.process(depth)

    depth_sensor = pipeline.get_active_profile().get_device(
    ).first_depth_sensor()
    depth_scale = depth_sensor.get_depth_scale()

    depth_image = np.asanyarray(depth.get_data())

    depth_colormap = cv2.applyColorMap(
        cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
    depth_colormap = cv2.cvtColor(depth_colormap, cv2.COLOR_BGR2RGBA)
    colors = depth_colormap.reshape(-1, 4).astype(np.float32) / 255.0

    x = np.arange(depth_image.shape[1])
    y = np.arange(depth_image.shape[0])
    xx, yy = np.meshgrid(x, y)
    zz = depth_image * depth_scale * 100

    return OrderedTriple(x=xx.reshape(-1),
                         y=yy.reshape(-1),
                         z=zz.reshape(-1),
                         extra={"colors": colors})
