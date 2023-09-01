import numpy as np
from flojoy import Matrix


def test_DOT_PRODUCT(mock_flojoy_decorator):
    import DOT_PRODUCT

    x = np.eye(3)
    x[2, 0] = 1

    element = Matrix(m=x)
    res = DOT_PRODUCT.DOT_PRODUCT(a=element, b=element)

    assert np.array_equal(res.m, np.dot(x, x))
