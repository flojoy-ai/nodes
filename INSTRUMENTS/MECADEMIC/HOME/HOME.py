from flojoy import flojoy, DataContainer


@flojoy(deps={"mecademicpy": "1.4.0"})
def HOME(ConnHandle: DataContainer) -> DataContainer:
    """
    The HOME node homes the robot arm. This node is required to be run before any other robot arm movement. It is recommended to run this node immediately after "ACTIVATE".

    Inputs
    ------
    ConnHandle
        A handle to the robot arm object.

    Returns
    -------
    DataContainer
        Containing a handle to the robot arm object, which is now homed assuming no errors were encountered.

    """
    if not ConnHandle.extra.IsConnected():
        raise ValueError("Robot connection failed.")

    ConnHandle.extra.Activate()
    return ConnHandle
