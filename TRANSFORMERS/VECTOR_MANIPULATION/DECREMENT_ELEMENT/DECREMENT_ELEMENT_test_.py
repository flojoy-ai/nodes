from numpy import arange, array_equal
from flojoy import Vector


def test_DECREMENT_ELEMENT(mock_flojoy_decorator):
    import DECREMENT_ELEMENT

    v = arange(1, 11)
    v = Vector(v=v)

    res = DECREMENT_ELEMENT.DECREMENT_ELEMENT(v, 20)

    ex = v.copy()
    assert array_equal(res.v, ex.v - 20)
