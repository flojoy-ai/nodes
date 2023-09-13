from flojoy import flojoy, node_initialization, NodeInitContainer, DataContainer, Surface, Image, OrderedPair
from typing import Optional


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
    input = init_container.get()
    s, i = input.x, input.y

    if not ConnHandle.extra.IsConnected():
        raise ValueError("Robot connection failed.")

    ConnHandle.extra.MovePose(x=s.x, y=s.y, z=s.z, alpha=i.a, beta=i.b, gamma=i.g)
    return ConnHandle


@node_initialization(for_node=MOVE_POSE)
def init(
    x: float,
    y: float,
    z: float,
    a: Optional[float],
    b: Optional[float],
    g: Optional[float],
) -> OrderedPair:
    return OrderedPair(
        x=Surface(x=x, y=y, z=z),
        y=Image(a=a, b=b, g=g)
    )
