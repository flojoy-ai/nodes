from numpy import where
from flojoy import flojoy, Vector, Scalar


@flojoy
def VECTOR_SEARCH(default: Vector, element: int) -> Scalar:
    """The VECTOR_SEARCH node returns the index where the element is located at

    Inputs
    ------
    default : Vector
        The input vector

    Parameters
    ----------
    element: value to search for in the vector

    Returns
    -------
    Scalar
        the index of the value found, returns -1 otherwise.
    """
    
    ind = where(default.v == element)[0]
    if (len(ind) == 0):
        ind = -1
    else:
        ind = ind[0]
    return Scalar(c=ind)
