from flojoy import flojoy, MecademicConnHandle
from PYTHON.utils.mecademic_utils import check_connection


@flojoy(deps={"mecademicpy": "1.4.0"})
def HOME(conn_handle: MecademicConnHandle) -> MecademicConnHandle:
    """
    The HOME node homes the robot arm. This node is required to be run before any other robot arm movement. It is recommended to run this node immediately after "ACTIVATE".

    Inputs
    ------
    conn_handle
        A handle to the robot arm object.

    Returns
    -------
    MecademicConnHandle
        Containing a handle to the robot arm object, which is now homed assuming no errors were encountered.

    """
    check_connection(conn_handle.robot)
    conn_handle.robot.Activate()
    return conn_handle
