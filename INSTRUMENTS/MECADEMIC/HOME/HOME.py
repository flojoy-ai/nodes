from flojoy import flojoy, Bytes

from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle
from PYTHON.utils.mecademic_utils import check_connection
import mecademicpy.robot as mdr


@flojoy(deps={"mecademicpy": "1.4.0"})
def HOME(ip_address: str) -> str:
    """
    The HOME node homes the robot arm. This node is required to be run before any other robot arm movement. It is recommended to run this node immediately after "ACTIVATE".

    Inputs
    ------
    ip_address
        The IP address of the robot arm.

    Returns
    -------
    ip_address
        The IP address of the robot arm.
    """
    robot: mdr.Robot = query_for_handle(ip_address)
    check_connection(robot)
    robot.Home()
    robot.WaitHomed()
    return ip_address
