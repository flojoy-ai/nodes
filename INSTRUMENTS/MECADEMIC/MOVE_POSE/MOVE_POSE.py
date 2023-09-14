from flojoy import flojoy, MecademicConnHandle
from typing import Optional
from PYTHON.utils.mecademic_utils import check_connection


@flojoy(deps={"mecademicpy": "1.4.0"})
def MOVE_POSE(
    conn_handle: MecademicConnHandle,
    x: float,
    y: float,
    z: float,
    alpha: Optional[float] = 0,
    beta: Optional[float] = 0,
    gamma: Optional[float] = 0,
) -> MecademicConnHandle:
    """
    The MOVE_POSE node linearly moves the robot's tool to an absolute Cartesian position.

    Inputs
    ------
    conn_handle
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
    conn_handle
        A handle to the robot arm object after it has been moved.

    """
    check_connection(conn_handle.robot)
    conn_handle.robot.MovePose(x=x, y=y, z=z, alpha=alpha, beta=beta, gamma=gamma)
    return conn_handle
