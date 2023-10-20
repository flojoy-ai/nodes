from flojoy import flojoy, TextBlob, DataFrame
from typing import Optional

from PYTHON.utils.mecademic_state.mecademic_calculations import calculateLimitingMaxVel
from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle


@flojoy(deps={"mecademicpy": "1.4.0"})
def MOVE_KEYFRAMES_LIN(
        ip_address: TextBlob,
        keyframes: DataFrame,
        trfX: Optional[float] = 0.0,
        trfY: Optional[float] = 0.0,
        trfZ: Optional[float] = 0.0,
        trfAlpha: Optional[float] = 0.0,
        trfBeta: Optional[float] = 0.0,
        trfGamma: Optional[float] = 0.0,
) -> TextBlob:
    """
    The MOVE_KEYFRAMES node LINEARLY RELATIVE TO A REFERENCE FRAME moves the robot's tool according to a set of 3d animation style keyframes.

    Inputs
    ------
    ip_address: TextBlob
        The IP address of the robot arm.
    keyframes: DataFrame
        A dataframe containing the keyframes to move to. The dataframe must have the following columns:
        x, y, z, alpha, beta, gamma, duration. The duration column is the time in seconds to move to the next keyframe.
    trfX: Optional[float]
        The X coordinate of the reference frame. If not specified, the default value of 0.0 is used.
    trfY: Optional[float]
        The Y coordinate of the reference frame. If not specified, the default value of 0.0 is used.
    trfZ: Optional[float]
        The Z coordinate of the reference frame. If not specified, the default value of 0.0 is used.
    trfAlpha: Optional[float]
        The alpha angle of the reference frame. If not specified, the default value of 0.0 is used.
    trfBeta: Optional[float]
        The beta angle of the reference frame. If not specified, the default value of 0.0 is used.
    trfGamma: Optional[float]
        The gamma angle of the reference frame. If not specified, the default value of 0.0 is used.

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

    # set reference frame
    robot.SetTRF(trfX, trfY, trfZ, trfAlpha, trfBeta, trfGamma)


    # Data validation
    required_columns = ["x", "y", "z", "alpha", "beta", "gamma", "duration"]
    for column in required_columns:
        if column not in keyframes.columns:
            raise ValueError(f"Keyframes dataframe must have a {column} column")
    # check that all values are numeric
    for column in keyframes.columns:
        if keyframes[column].dtype != "float64":
            raise ValueError(f"Keyframes dataframe column {column} must be numeric")

    # Move execution
    for index, row in keyframes.iterrows():
        vel = calculateLimitingMaxVel(robot.GetJoints(), [row["x"], row["y"], row["z"], row["alpha"], row["beta"], row["gamma"]], row["duration"])
        robot.SetJointVel(vel)
        robot.MoveLinRelTRF(row["x"], row["y"], row["z"], row["alpha"], row["beta"], row["gamma"])
        robot.WaitIdle(row["duration"])
    return ip_address
