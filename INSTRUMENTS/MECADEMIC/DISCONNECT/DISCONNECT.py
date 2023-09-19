from flojoy import flojoy, TextBlob
from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle

@flojoy(deps={"mecademicpy": "1.4.0"})
def DISCONNECT(ip_address: str) -> None:
    """
    TODO
    The CONNECT node establishes a connection to the Mecademic robot arm via its API.
    Returns
    -------
    String
       The IP address of the robot arm.

    """

    robot = query_for_handle(ip_address)

    robot.WaitIdle()

    robot.DeactivateRobot()
    robot.WaitDeactivated()

    robot.Disconnect()
    robot.WaitSimDeactivated()
    robot.WaitDisconnected()

    return None