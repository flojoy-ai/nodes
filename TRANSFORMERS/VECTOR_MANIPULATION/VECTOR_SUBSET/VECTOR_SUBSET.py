
from numpy import any, array, arange, put
from flojoy import flojoy, Vector, Array


@flojoy
def VECTOR_SUBSET(default: Vector, indices: Array, values: Array, length: int = 1) -> Vector:
    """The VECTOR_SUBSET node returns the subset of values from the input vector
    Inputs
    ------
    v : Vector
        The input vector to return subset of values from

    Parameters
    ----------
    indices: Array
        specified indices to replace values at from the input vector
    
    values: Array
        subset of values to replace the specified indices

    length: int
        number of elements to replace from the input vector, default is 1 (this only applies when one index is specified for indices parameter)

    Returns
    -------
    Vector
        The new vector with subset of elements replaced from the input vector
    """
    # unwrap the indices first
    indices = array(indices.unwrap(), dtype=int)
    # unwrap the values next
    values = array(values.unwrap(), dtype=int)
    
    assert(len(default.v) > len(indices)),  "The length of indices parameter must be less than the length of the Vector."
    assert(any(indices >= 0)), "The indices must be greater than zero."
    
    if (len(indices) == 1):
        assert((indices[0] + (length - 1)) < len(default.v)), "The length of items to delete starting from index parameter must not exceed the length of the Vector."

    if (len(indices) > 1):
        v = put(default.v, indices, values)
    else:
        indices = arange(indices[0], length)
        v = put(default.v, indices, values)
    return Vector(v=v)
