from flojoy import flojoy, DataContainer, Scalar


@flojoy(deps={"mecademicpy": "1.4.0"})
def SET_JOINT_VEL(ConnHandle: DataContainer, v: Scalar) -> DataContainer:
    """
    The SET_JOINT_VEL node sets the robot arm's angular velocity for its joints.

    Inputs
    ------
    ConnHandle : DataContainer
        A handle to the robot arm object.

    Parameters
    ------
    v : Scalar
        The angular velocity to be set for each joint.

    Returns
    -------
    ConnHandle
        A handle to the robot arm object after its joint velocity has been set.

    """
    if not ConnHandle.extra.IsConnected():
        raise ValueError("Robot connection failed.")
    
    ConnHandle.extra.SetJointVel(v.c)
    return ConnHandle
