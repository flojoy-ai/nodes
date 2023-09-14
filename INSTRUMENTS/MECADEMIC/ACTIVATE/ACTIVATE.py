from flojoy import flojoy, MecademicConnHandle
from PYTHON.utils.mecademic_utils import check_connection


@flojoy(deps={"mecademicpy": "1.4.0"})
def ACTIVATE(conn_handle: MecademicConnHandle) -> MecademicConnHandle:
    """
    The ACTIVATE node activates the robot arm.

    Inputs
    ------
    conn_handle
        A handle to the robot arm object.

    Returns
    -------
    MecademicConnHandle
        Containing a handle to the activated robot arm object.

    """
    check_connection(conn_handle.robot)
    conn_handle.robot.Activate()
    return conn_handle
