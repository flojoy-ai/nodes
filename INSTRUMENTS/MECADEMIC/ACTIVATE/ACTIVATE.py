from flojoy import flojoy, Bytes, TextBlob

from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle


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
