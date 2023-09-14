from flojoy import flojoy, Bytes
from typing import Optional


@flojoy
def MOVE_LIN(
    ConnHandle: Bytes,
    x: float,
    y: float,
    z: float,
    a: Optional[float] = 0,
    b: Optional[float] = 0,
    g: Optional[float] = 0,
) -> Bytes:
    """
    The MOVE_LIN node linearly moves the robot's tool to an absolute Cartesian position.

    Inputs
    ------
    ConnHandle
        A handle to the robot arm object.

    Parameters
    ------
    x : float
        The x coordinate of the position to move to
    y : float
        The y coordinate of the position to move to
    z : float
        The z coordinate of the position to move to
    a : float, optional
        The alpha coordinate (rotation in radians about the x axis) of the position to move to.
    b : float, optional
        The beta coordinate   (rotation in radians about the y axis) of the position to move to.
    g : float, optional
        The gamma coordinate (rotation in radians about the z axis) of the position to move to.



    Returns
    -------
    ConnHandle
        A handle to the robot arm object after it has been moved.

    """

    if not ConnHandle.robot.IsConnected():
        raise ValueError("Robot connection failed.")

    ConnHandle.robot.MoveLin(x=x, y=y, z=z, alpha=a, beta=b, gamma=g)
    return ConnHandle
