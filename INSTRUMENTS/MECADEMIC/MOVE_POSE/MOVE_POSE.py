from flojoy import flojoy, Bytes
from typing import Optional


@flojoy(deps={"mecademicpy": "1.4.0"})
def MOVE_POSE(
    ConnHandle: Bytes, # TODO: use explicit generic type for robot in the Bytes IE Bytes[MecademicRobotHandle]
    x: float,
    y: float,
    z: float,
    alpha: Optional[float] = 0,
    beta: Optional[float] = 0,
    gamma: Optional[float] = 0,
) -> Bytes:
    """
    The MOVE_POSE node linearly moves the robot's tool to an absolute Cartesian position.

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
    alpha : float, optional
        The alpha coordinate (rotation in radians about the x axis) of the position to move to.
    beta : float, optional
        The beta coordinate   (rotation in radians about the y axis) of the position to move to.
    gamma : float, optional
        The gamma coordinate (rotation in radians about the z axis) of the position to move to.

    Returns
    -------
    ConnHandle
        A handle to the robot arm object after it has been moved.

    """
    if not ConnHandle.robot.IsConnected():
        raise ValueError("Robot connection failed.")

    ConnHandle.robot.MovePose(x=x, y=y, z=z, alpha=alpha, beta=beta, gamma=gamma)
    return ConnHandle
