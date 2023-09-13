from flojoy import flojoy, node_initialization, NodeInitContainer, DataContainer, Surface, Image
from typing import Optional, TypedDict


class SurfaceAndImageReturnOutput(TypedDict):
    surface: Surface
    image: Image


@flojoy
def MOVE_POSE(
    ConnHandle: DataContainer,
    init_container: NodeInitContainer
) -> DataContainer:
    """
    The MOVE_POSE node linearly moves the robot's tool to an absolute Cartesian position.
    
    Inputs
    ------
    ConnHandle
        A handle to the robot arm object.
        
    Returns
    -------
    ConnHandle
        A handle to the robot arm object after it has been moved.
        
    """
    surface_and_image = init_container.get()
    a, b = surface_and_image.surface, surface_and_image.image

    if not ConnHandle.extra.IsConnected():
        raise ValueError("Robot connection failed.")

    ConnHandle.extra.MovePose(x=a.x, y=a.y, z=a.z, alpha=b.a, beta=b.b, gamma=b.g)
    return ConnHandle


@node_initialization(for_node=MOVE_POSE)
def init(
    x: float,
    y: float,
    z: float,
    a: Optional[float],
    b: Optional[float],
    g: Optional[float],
) -> SurfaceAndImageReturnOutput:
    return SurfaceAndImageReturnOutput(
        surface=Surface(x=x, y=y, z=z),
        image=Image(a=a, b=b, g=g)
    )
