from numpy import arange, array_equal
from flojoy import Vector
from pytest import raises

def test_VECTOR_INSERT(mock_flojoy_decorator):
    import VECTOR_MIN_MAX

    v = arange(10)

    v = Vector(v=v)
    res = VECTOR_MIN_MAX.VECTOR_MIN_MAX(v, "max")
    assert array_equal(res.c, v.v[-1])

    res = VECTOR_MIN_MAX.VECTOR_MIN_MAX(v, "min")
    assert array_equal(res.c, v.v[0])