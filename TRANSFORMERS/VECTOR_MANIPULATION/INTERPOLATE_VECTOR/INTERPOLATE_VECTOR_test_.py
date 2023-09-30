from numpy import array, array_equal
from flojoy import Vector


def test_INTERPOLATE_VECTOR(mock_flojoy_decorator):
    import INTERPOLATE_VECTOR

    x = array([2.3, 5.2, 7.8, 7.9, 10])
    x = Vector(v=x)

    interpolated_value = INTERPOLATE_VECTOR.INTERPOLATE_VECTOR(x, 1.69231)

    assert array_equal(interpolated_value.c, 7.000006)
