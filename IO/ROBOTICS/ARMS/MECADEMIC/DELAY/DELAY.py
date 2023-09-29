from flojoy import flojoy, TextBlob
from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle


@flojoy(deps={"mecademicpy": "1.4.0"})
def DELAY(
    ip_address: TextBlob,
    time: float,
) -> TextBlob:
    """
    The DELAY node delays the action between two nodes.

    Inputs
    ------
    ip_address: TextBlob
        The IP address of the robot arm.

    time: float
        The time of delay in seconds.

    Returns
    -------
    ip_address
        The IP address of the robot arm.

    """
    robot = query_for_handle(ip_address)
    robot.Delay(time)
    robot.WaitIdle()
    return ip_address
