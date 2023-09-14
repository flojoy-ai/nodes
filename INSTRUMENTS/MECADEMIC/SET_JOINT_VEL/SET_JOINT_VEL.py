from flojoy import flojoy, MecademicConnHandle
from PYTHON.utils.mecademic_utils import check_connection


@flojoy(deps={"mecademicpy": "1.4.0"})
def SET_JOINT_VEL(conn_handle: MecademicConnHandle, v: float) -> MecademicConnHandle:
    """
    The SET_JOINT_VEL node sets the robot arm's angular velocity for its joints.

    Inputs
    ------
    conn_handle : MecademicConnHandle
        A handle to the robot arm object.

    Parameters
    ------
    v : float
        The angular velocity to be set for each joint.

    Returns
    -------
    conn_handle
        A handle to the robot arm object after its joint velocity has been set.

    """
    check_connection(conn_handle.robot)
    conn_handle.robot.SetJointVel(v)
    return conn_handle
