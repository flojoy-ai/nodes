from flojoy import flojoy, TextBlob
from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle


@flojoy(deps={"mecademicpy": "1.4.0"})
def HOME(ip_address: TextBlob) -> TextBlob:
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
    robot = query_for_handle(ip_address)
    robot.Home()
    robot.WaitHomed()
    return ip_address
