from flojoy import flojoy, DataContainer


@flojoy(deps={"mecademicpy": "1.4.0"})
def HOME(ConnHandle: DataContainer) -> DataContainer:
    """
    The HOME node homes the robot arm.
            
    Returns
    -------
    DataContainer
        Extra: A handle to the activated robot arm object.
        
    """
    if not ConnHandle.extra.IsConnected():
        raise ValueError("Robot connection failed.")
    
    ConnHandle.extra.Activate()
    return ConnHandle
