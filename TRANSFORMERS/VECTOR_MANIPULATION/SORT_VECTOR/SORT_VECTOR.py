from flojoy import flojoy, Vector

@flojoy
def SORT_VECTOR(
    default: Vector,
) -> Vector:
    """The SORT_VECTOR node returns the input Vector that is sorted

    Inputs
    ------
    v : Vector
        The input vector

    Returns
    -------
    Vector
        Sorted input vector
    """

    return Vector(sorted(default.v))
