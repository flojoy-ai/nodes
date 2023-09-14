from flojoy import flojoy, Bytes


@flojoy(deps={"mecademicpy": "1.4.0"})
def SET_CART_LIN_VEL(ConnHandle: Bytes, v: float) -> Bytes:
    """
    The SET_CART_LIN_VEL node sets the robot arm's linear velocity in Cartesian coordinates.

    Inputs
    ------
    ConnHandle : Bytes
        A handle to the robot arm object.

    Parameters
    ------
    v : float
        The linear velocity to be set.

    Returns
    -------
    ConnHandle
        A handle to the robot arm object after its linear velocity has been set.

    """
    if not ConnHandle.robot.IsConnected():
        raise ValueError("Robot connection failed.")
    
    ConnHandle.robot.SetCartLinVel(v)
    return ConnHandle
