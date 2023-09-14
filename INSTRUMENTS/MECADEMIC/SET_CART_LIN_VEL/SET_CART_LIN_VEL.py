from flojoy import flojoy, MecademicConnHandle
from PYTHON.utils.mecademic_utils import check_connection


@flojoy(deps={"mecademicpy": "1.4.0"})
def SET_CART_LIN_VEL(conn_handle: MecademicConnHandle, v: float) -> MecademicConnHandle:
    """
    The SET_CART_LIN_VEL node sets the robot arm's linear velocity in Cartesian coordinates.

    Inputs
    ------
    conn_handle : MecademicConnHandle
        A handle to the robot arm object.

    Parameters
    ------
    v : float
        The linear velocity to be set.

    Returns
    -------
    conn_handle
        A handle to the robot arm object after its linear velocity has been set.

    """
    check_connection(conn_handle.robot)
    conn_handle.robot.SetCartLinVel(v)
    return conn_handle
