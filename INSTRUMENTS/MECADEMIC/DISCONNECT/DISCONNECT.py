from flojoy import flojoy, TextBlob
from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle

@flojoy(deps={"mecademicpy": "1.4.0"})
def DISCONNECT(ip: TextBlob) -> None:
    """
    The DISCONNECT node disconnect the Mecademic robot arm via its API.

    Inputs
    ------
    ip
        The IP address of the robot arm.

    """

    robot = query_for_handle(ip.text_blob)

    robot.WaitIdle()

    robot.DeactivateRobot()
    robot.WaitDeactivated()

    robot.Disconnect()
    robot.WaitSimDeactivated()
    robot.WaitDisconnected()

    return None
