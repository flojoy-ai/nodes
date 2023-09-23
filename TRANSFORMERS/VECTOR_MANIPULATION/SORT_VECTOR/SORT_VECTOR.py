from flojoy import flojoy, Vector


@flojoy
def SORT_VECTOR(
    default: Vector,
    reverse: int = 0,
) -> Vector:
    """The SORT_VECTOR node returns the input Vector that is sorted

    Inputs
    ------
    default : Vector
        The input vector

    Parameters
    ----------
    reverse : int
        If it's given 0, sort in ascending order.
        If it's given 1, sort in descending order.

    Returns
    -------
    Vector
        Sorted input vector
    """
    if reverse == 0:
        return Vector(v=sorted(default.v))
    elif reverse == 1:
        return Vector(v=sorted(default.v, reverse=True))
    else:
        raise AssertionError(
            f"Invalid reverse value! It should be either 0 or 1 but given {reverse}"
        )
