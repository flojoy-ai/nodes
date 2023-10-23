import numpy as np
import cv2
from flojoy import CameraConnection, DataContainer, flojoy, OrderedTriple, node_initialization, NodeInitContainer
from typing import Optional
import pyrealsense2 as rs

# decimate = rs.decimation_filter(4)
# spatial = rs.spatial_filter()
# spatial.set_option(rs.option.filter_magnitude, 2)
# spatial.set_option(rs.option.filter_smooth_alpha, 0.8)
# spatial.set_option(rs.option.filter_smooth_delta, 10)
# spatial.set_option(rs.option.holes_fill, 3)
# temporal = rs.temporal_filter()


@flojoy(inject_connection=True)
def REALSENSE(connection: CameraConnection,
              init_container: NodeInitContainer,
              default: Optional[DataContainer] = None) -> OrderedTriple:
    pipeline = connection.get_handle()
    filters = init_container.get()

    frames = pipeline.wait_for_frames()
    depth = frames.get_depth_frame()
    if filters is not None:
        for filter in filters:
            depth = filter.process(depth)

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


@node_initialization(for_node=REALSENSE)
def init_filters(decimate_filter: bool = True,
                 decimate_size: int = 4,
                 temporal_filter: bool = True,
                 spatial_filter: bool = True,
                 spatial_filter_magnitude: int = 2,
                 spatial_filter_smooth_alpha: float = 0.8,
                 spatial_filter_smooth_delta: int = 20):
    filters = []
    if decimate_filter:
        filters.append(rs.decimation_filter(decimate_size))
    if spatial_filter:
        spatial = rs.spatial_filter()
        spatial.set_option(rs.option.filter_magnitude,
                           spatial_filter_magnitude)
        spatial.set_option(rs.option.filter_smooth_alpha,
                           spatial_filter_smooth_alpha)
        spatial.set_option(rs.option.filter_smooth_delta,
                           spatial_filter_smooth_delta)
        spatial.set_option(rs.option.holes_fill, 3)
        filters.append(spatial)
    if temporal_filter:
        filters.append(rs.temporal_filter())

    return filters
