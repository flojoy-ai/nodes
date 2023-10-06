from flojoy import flojoy, Vector, Matrix


@flojoy
def MATRIX_2_VECTOR(default: Matrix) -> Vector:
    """The VECTOR_2_MATRIX node takes an input matrix and transpose it along the chosen axis.

    Inputs
    ------
    default: Matrix
        The input matrix that will be transformed into vector data type.

    Returns
    -------
    Vector
        Vector that is flatten from input matrix.
    """
    rVector = default.m.flatten()

    return Vector(v=rVector)
