from flojoy import flojoy, TextBlob, DataFrame

from PYTHON.utils.mecademic_state.mecademic_calculations import calculateLimitingMaxVel
from PYTHON.utils.mecademic_state.mecademic_state import query_for_handle


@flojoy(deps={"mecademicpy": "1.4.0"})
def MOVE_KEYFRAMES_LIN(
        ip_address: TextBlob,
        keyframes: DataFrame,
) -> TextBlob:
    """
    The MOVE_KEYFRAMES node LINEARLY RELATIVE TO A REFERENCE FRAME moves the robot's tool according to a set of 3d animation style keyframes.

    Set a tool reference frame (TRF) to move the robot's tool relative to the TRF. The TRF is set using the SET_TRF node.

    Inputs
    ------
    ip_address: TextBlob
        The IP address of the robot arm.
    keyframes: DataFrame
        A dataframe containing the keyframes to move to. The dataframe must have the following columns:
        x, y, z, alpha, beta, gamma, duration. The duration column is the time in seconds to move to the next keyframe.

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
