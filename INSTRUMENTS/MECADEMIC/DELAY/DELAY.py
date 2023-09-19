from flojoy import flojoy, TextBlob
from typing import Optional
from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle


@flojoy(deps={"mecademicpy": "1.4.0"})
def DELAY(
    ip_address: TextBlob,
    time : float,
) -> TextBlob:
    """
    The MOVE_JOINT node linearly moves the robot's tool to an absolute Cartesian position.

    Inputs
    ------
    ip_address: TextBlob
        The IP address of the robot arm.

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
    ip_address
        The IP address of the robot arm.

    """
    robot = query_for_handle(ip_address)
    robot.Delay(time)
    robot.WaitIdle()
    return ip_address
