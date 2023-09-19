from flojoy import flojoy, Bytes, TextBlob
import mecademicpy.robot as mdr

from PYTHON.utils.mecademic_state.state_mocktest import query_for_handle
from PYTHON.utils.mecademic_utils import check_connection


@flojoy(deps={"mecademicpy": "1.4.0"})
def ACTIVATE(ip: TextBlob, simulator: bool = False) -> TextBlob:
    """
    The ACTIVATE node activates the robot arm.

    Inputs
    ------
    ip
        The IP address of the robot arm.

    Parameters
    ------
    simulator
        Whether to activate the simulator or not. Defaults to False.

    Returns
    -------
    ip
        The IP address of the robot arm.

    """
    # handle: mdr.Robot = query_for_handle(ip)
    handle = query_for_handle(ip)
    # check_connection(handle)
    if simulator:
        handle.ActivateSim()
    else:
        handle.ActivateRobot()
    handle.WaitActivated()
    return ip
