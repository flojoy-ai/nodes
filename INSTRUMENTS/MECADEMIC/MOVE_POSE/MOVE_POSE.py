from flojoy import flojoy, DataContainer, Surface, Image


@flojoy
def MOVE_POSE(
    ConnHandle: DataContainer,
    a: Surface,
    b: Image
) -> DataContainer:
    """
    The MOVE_POSE node linearly moves the robot's tool to an absolute Cartesian position.
    
    Inputs
    ------
    ConnHandle : mdr.Robot
        A handle to the robot arm object.
        
    surface : Surface
        Desired end effector coordinates in mm.
        
    image : Image
        Desired end effector orientation in degrees.
        
    Returns
    -------
    ConnHandle
        A handle to the robot arm object after it has been moved.
        
    """
    if not ConnHandle.extra.IsConnected():
        raise ValueError("Robot connection failed.")

    ConnHandle.extra.MovePose(x=a.x, y=a.y, z=a.z, alpha=b.a, beta=b.b, gamma=b.g)
    return ConnHandle
