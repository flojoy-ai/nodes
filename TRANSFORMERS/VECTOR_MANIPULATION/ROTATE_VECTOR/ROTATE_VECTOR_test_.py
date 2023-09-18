from numpy import arange, array_equal, roll
from flojoy import Vector

def test_ROTATE_VECTOR(mock_flojoy_decorator):
    import ROTATE_VECTOR

    v = arange(1, 11)
    v = Vector(v=v)

    res = ROTATE_VECTOR.ROTATE_VECTOR(v, 3) 

    ex = v.copy()
    assert array_equal(res.v, roll(ex.v, 3))
