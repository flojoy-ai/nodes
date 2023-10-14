from flojoy import flojoy, TextBlob
from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle


@flojoy(deps={"mecademicpy": "1.4.0"})
def ACTIVATE(ip_address: TextBlob, simulator: bool = False) -> TextBlob:
    """
    The ACTIVATE node activates the robot arm.

    Inputs
    ------
    ip_address: TextBlob
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
    handle = query_for_handle(ip_address)
    if simulator:
        handle.ActivateSim()
    else:
        handle.ActivateRobot()
    handle.WaitActivated()
    return ip_address
