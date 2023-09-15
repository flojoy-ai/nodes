from flojoy import flojoy, Bytes
from PYTHON.utils.mecademic_utils import check_connection


@flojoy(deps={"mecademicpy": "1.4.0"})
def ACTIVATE(conn_handle: Bytes) -> Bytes:
    """
    The ACTIVATE node activates the robot arm.

    Inputs
    ------
    conn_handle
        A handle to the robot arm object.

    Returns
    -------
    Bytes
        Containing a handle to the activated robot arm object.

    """
    check_connection(conn_handle.b)
    conn_handle.b.Activate()
    return conn_handle
