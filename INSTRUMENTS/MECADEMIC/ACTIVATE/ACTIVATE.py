from flojoy import flojoy, Bytes
import mecademicpy.robot as mdr

from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle
from PYTHON.utils.mecademic_utils import check_connection


@flojoy(deps={"mecademicpy": "1.4.0"})
def ACTIVATE(ip_address: str, simulator: bool = False) -> str:
    """
    The ACTIVATE node activates the robot arm.

    Inputs
    ------
    ip_address
        The IP address of the robot arm.

    Parameters
    ------
    simulator
        Whether to activate the simulator or not. Defaults to False.

    Returns
    -------
    ip_address
        The IP address of the robot arm.

    """
    handle: mdr.Robot = query_for_handle(ip_address)
    check_connection(handle)
    if simulator:
        handle.ActivateSim()
    else:
        handle.ActivateRobot()
    handle.WaitActivated()
    return ip_address
