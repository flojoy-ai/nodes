from flojoy import flojoy, Bytes


@flojoy(deps={"mecademicpy": "1.4.0"})
def ACTIVATE(ConnHandle: Bytes) -> Bytes:
    """
    The ACTIVATE node activates the robot arm.

    Inputs
    ------
    ConnHandle
        A handle to the robot arm object.

    Returns
    -------
    Bytes
        Containing a handle to the activated robot arm object.

    """
    if not ConnHandle.robot.IsConnected():
        raise ValueError("Robot connection failed.")

    ConnHandle.robot.Activate()
    return ConnHandle
