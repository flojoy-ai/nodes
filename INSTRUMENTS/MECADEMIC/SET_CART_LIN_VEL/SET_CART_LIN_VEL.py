from flojoy import flojoy, DataContainer, Scalar


@flojoy(deps={"mecademicpy": "1.4.0"})
def SET_CART_LIN_VEL(ConnHandle: DataContainer, v: Scalar) -> DataContainer:
    """
    The SET_CART_LIN_VEL node sets the arm's linear velocity.
    
    Inputs
    ------
    ConnHandle : DataContainer
        A handle to the robot arm object.
    
    v : Scalar
        The cart velocity to be set.
    
    Returns
    -------
    ConnHandle
        A handle to the activated robot arm object.
        
    """
    if not ConnHandle.extra.IsConnected():
        raise ValueError("Robot connection failed.")
    
    ConnHandle.extra.SetCartLinVel(v.c)
    return ConnHandle
