from flojoy import TextBlob, flojoy
from PYTHON.utils.mecademic_state.mecademic_state import add_handle, init_handle_map


@flojoy(deps={"mecademicpy": "1.4.0"})
def CONNECT(ip_address: str) -> TextBlob:
    """
    The CONNECT node establishes a connection to the Mecademic robot arm via its API.

    Parameters
    ----------
    ip_address : str
        The IP address of the robot arm.

    Returns
    -------
    String
       The IP address of the robot arm.
    """
    init_handle_map(allow_reinit=True)
    add_handle(ip_address)
    return TextBlob(text_blob=ip_address)
