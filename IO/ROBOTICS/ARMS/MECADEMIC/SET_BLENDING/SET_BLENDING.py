from flojoy import flojoy, TextBlob
from typing import Optional

from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle


@flojoy(deps={"mecademicpy": "1.4.0"})
def SET_BLENDING(
        ip_address: TextBlob,
        blending: Optional[float] = 0.0
) -> TextBlob:
    """
    The SET_BLENDING to make the moves of the robot arm smoother.

    Inputs
    ------
    ip_address: TextBlob
        The IP address of the robot arm.

    Parameters:
    -------
    blending: Optional[float]
        The blending factor to use when moving between keyframes. If not specified, the default value of 0.0 is used.

    Returns
    -------
    ip_address
        The IP address of the robot arm.

    """
    robot = query_for_handle(ip_address)
    # Set blending

    robot.SetBlending(min(blending, 100.0))
    return ip_address
