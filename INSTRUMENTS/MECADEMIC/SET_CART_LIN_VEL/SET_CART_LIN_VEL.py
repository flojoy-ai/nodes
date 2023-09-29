from flojoy import flojoy, TextBlob
from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle


@flojoy(deps={"mecademicpy": "1.4.0"})
def SET_CART_LIN_VEL(ip_address: TextBlob, v: float) -> TextBlob:
    """
    The SET_CART_LIN_VEL node sets the robot arm's linear velocity in Cartesian coordinates.

    Inputs
    ------
    ip_address: TextBlob
        The IP address of the robot arm.

    Parameters
    ------
    v : float
        The velocity to be set.

    Returns
    -------
    ip_address
        The IP address of the robot arm.
    """

    robot = query_for_handle(ip_address)
    robot.SetCartLinVel(v)
    return ip_address
