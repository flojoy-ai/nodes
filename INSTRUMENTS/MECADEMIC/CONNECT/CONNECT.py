from flojoy import flojoy

from PYTHON.utils.mecademic_state.mecademic_state import add_handle


@flojoy(deps={"mecademicpy": "1.4.0"})
def CONNECT(ip_address: str) -> str:
    """
    The CONNECT node establishes a connection to the Mecademic robot arm via its API.
    Returns
    -------
    String
       The IP address of the robot arm.
    """
    add_handle(ip_address)
    return ip_address
