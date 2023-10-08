from numpy import array_equal, arange, array
from flojoy import Vector
from pytest import raises


def test_VECTOR_SEARCH(mock_flojoy_decorator):
    import VECTOR_SEARCH

    v = arange(1, 11)
    v = Vector(v=v)
    ex = v.copy()

    res = VECTOR_SEARCH.VECTOR_SEARCH(v, 8)

    assert array_equal(v.v[res.c], v.v[7])
    
    # when item does not exist
    res = VECTOR_SEARCH.VECTOR_SEARCH(v, 12)

    assert  array_equal(res.c, -1)

