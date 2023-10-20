from flojoy import flojoy, TextBlob
from typing import Optional
from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle


@flojoy(deps={"mecademicpy": "1.4.0"})
def SET_TRF(ip_address: TextBlob, rf_x: Optional[float] = 0.0, rf_y: Optional[float] = 0.0, rf_z: Optional[float] = 0.0, rf_a: Optional[float] = 0.0, rf_b: Optional[float] = 0.0, rf_g: Optional[float] = 0.0) -> TextBlob:
    """
     The SET_TRF node sets the robot arm's reference frame.

     Inputs
     ------
     ip_address
         The IP address of the robot arm.

     Parameters
     ------
    rfX: Optional[float]
        The X coordinate of the reference plane. If not specified, the default value of 0.0 is used.
    rfY: Optional[float]
        The Y coordinate of the reference plane. If not specified, the default value of 0.0 is used.
    rfZ: Optional[float]
        The Z coordinate of the reference plane. If not specified, the default value of 0.0 is used.
    rfAlpha: Optional[float]
        The alpha angle of the reference plane. If not specified, the default value of 0.0 is used.
    rfBeta: Optional[float]
        The beta angle of the reference plane. If not specified, the default value of 0.0 is used.
    rfGamma: Optional[float]
        The gamma angle of the reference plane. If not specified, the default value of 0.0 is used.

    Returns
     -------
     ip_address
         The IP address of the robot arm.

    """
    robot = query_for_handle(ip_address)
    robot.SetTRF(rf_x, rf_y, rf_z, rf_a, rf_b, rf_g)
    return ip_address
