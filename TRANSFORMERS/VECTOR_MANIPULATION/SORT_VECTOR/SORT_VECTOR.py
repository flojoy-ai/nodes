from flojoy import flojoy, Vector


@flojoy
def SORT_VECTOR(
    default: Vector,
    reverse: bool = False,
) -> Vector:
    """The SORT_VECTOR node returns an input vector that is sorted.

    Inputs
    ------
    default : Vector
        The input vector.

    Parameters
    ----------
    reverse : bool
        If False, sorted in ascending order. 
        If True, sorted in descending order.

    Returns
    -------
    Vector
        The sorted input vector.
    """
    
    return Vector(v=sorted(default.v, reverse=reverse))
