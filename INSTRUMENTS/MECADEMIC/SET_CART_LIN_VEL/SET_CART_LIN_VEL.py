from flojoy import flojoy, Bytes
from PYTHON.utils.mecademic_utils import check_connection


@flojoy(deps={"mecademicpy": "1.4.0"})
def SET_CART_LIN_VEL(conn_handle: Bytes, v: float) -> Bytes:
    """
    The SET_CART_LIN_VEL node sets the robot arm's linear velocity in Cartesian coordinates.

    Inputs
    ------
    conn_handle : Bytes
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
    check_connection(conn_handle.b)
    conn_handle.b.SetCartLinVel(v)
    return conn_handle
