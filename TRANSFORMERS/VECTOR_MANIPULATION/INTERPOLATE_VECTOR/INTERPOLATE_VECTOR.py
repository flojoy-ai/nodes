from flojoy import flojoy, Vector, Scalar
from math import floor


@flojoy
def INTERPOLATE_VECTOR(default: Vector, fractional_index: float) -> Scalar:
    """The INTERPOLATE_VECTOR node takes the element located closest to the fractional index (rounded down)
    and the next element and calculates the interpolated point.
    This number gets multiplied to the difference of fractional_index and its closests whole integer,
    which finally gets added to the element at the interpolated point. The resulting number is the interpolated value.

    Inputs
    ------
    default : Vector
        The input vector

    Parameters
    ----------
    fractional_index: float
        The starting index to interpolate from

    Returns
    -------
    Scalar
        interpolated value
    """

    if fractional_index > len(default.v) - 1:
        return Scalar(c=default.v[-1])
    elif fractional_index < 0:
        return Scalar(c=default.v[0])

    interpolation_point = floor(fractional_index)
    fraction = fractional_index - interpolation_point
    difference = default.v[interpolation_point + 1] - default.v[interpolation_point]
    interpolated_value = default.v[interpolation_point] + (difference * fraction)

    return Scalar(c=interpolated_value)
