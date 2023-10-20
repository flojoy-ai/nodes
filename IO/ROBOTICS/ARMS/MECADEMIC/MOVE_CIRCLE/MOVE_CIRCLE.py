import math

from flojoy import flojoy, TextBlob
from typing import Optional

from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle

def getCirclePositions(radius, revolutions, center_X, center_Y, center_Z):
    positions = []
    for i in range(0, 360 * revolutions):
        angle = i * math.pi / 180
        positions.append(
            [
                center_X + radius * math.cos(angle),
                center_Y + radius * math.sin(angle),
                center_Z,
            ]
        )
    return positions


@flojoy(deps={"mecademicpy": "1.4.0"})
def MOVE_CIRCLE(
        ip_address: TextBlob,
        rfX: Optional[float] = 0.0,
        rfY: Optional[float] = 0.0,
        rfZ: Optional[float] = 0.0,
        rfAlpha: Optional[float] = 0.0,
        rfBeta: Optional[float] = 0.0,
        rfGamma: Optional[float] = 0.0,
        center_X: Optional[float] = 0.0,
        center_Y: Optional[float] = 0.0,
        center_Z: Optional[float] = 0.0,
        radius: Optional[float] = 0.0,
        revolutions: Optional[float] = 1.0,
) -> TextBlob:
    """
    The Move circle node moves in a circle relative to a reference plane.

    Inputs
    ------
    ip_address: TextBlob
        The IP address of the robot arm.

    Parameters:
    -------
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
    center_X: Optional[float]
        The X coordinate of the center of the circle. If not specified, the default value of 0.0 is used.
    center_Y: Optional[float]
        The Y coordinate of the center of the circle. If not specified, the default value of 0.0 is used.
    center_Z: Optional[float]
        The Z coordinate of the center of the circle. If not specified, the default value of 0.0 is used.
    radius: Optional[float]
        The radius of the circle. If not specified, the default value of 0.0 is used.
    revolutions: Optional[float]
        The number of revolutions to make. If not specified, the default value of 1.0 is used.
    Returns
    -------
    ip_address
        The IP address of the robot arm.

    """
    robot = query_for_handle(ip_address)

    # set reference frame
    robot.SetTRF(rfX, rfY, rfZ, rfAlpha, rfBeta, rfGamma)
    robot.MoveLin(center_X, center_Y, center_Z)
    positions = getCirclePositions(radius, revolutions, center_X, center_Y, center_Z)
    for position in positions:
        robot.MoveLin(position[0], position[1], position[2])
    robot.MoveLin(center_X, center_Y, center_Z)

    return ip_address
