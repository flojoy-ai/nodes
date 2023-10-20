import math

import pandas as pd

from PYTHON.utils.mecademic_state.mecademic_calculations import getCirclePositions
from flojoy import flojoy, TextBlob, DataFrame
from typing import Optional

@flojoy(deps={"mecademicpy": "1.4.0"})
def CALCULATE_CIRCLE_MOVE(
        center_X: Optional[float] = 0.0,
        center_Y: Optional[float] = 0.0,
        center_Z: Optional[float] = 0.0,
        radius: Optional[float] = 0.0,
        revolutions: Optional[float] = 1.0,
        point_duration: Optional[int] = 500,
) -> DataFrame:
    """
    The Move circle node moves in a circle relative to a reference plane.

    Parameters:
    -------
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
    point_duration: Optional[int]
        The duration of each point in milliseconds. If not specified, the default value of 500 is used.
    Returns
    -------
    dataframe
        A dataframe of keyframes to move to.

    """
    positions = getCirclePositions(radius, revolutions, center_X, center_Y, center_Z)

    df = pd.DataFrame(positions, columns=["x", "y", "z", "alpha", "beta", "gamma", "duration"])
    for i in range(0, len(positions)):
        df.loc[i, "x"] = positions[i][0]
        df.loc[i, "y"] = positions[i][1]
        df.loc[i, "z"] = positions[i][2]
        df.loc[i, "alpha"] = 0
        df.loc[i, "beta"] = 0
        df.loc[i, "gamma"] = 0
        df.loc[i, "duration"] = point_duration

    return df
