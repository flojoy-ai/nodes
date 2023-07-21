import numpy as np

from flojoy import OrderedPair, Vector, Scalar


def test_MULTIPLY_vec_vec(mock_flojoy_decorator):

    import MULTIPLY

    x = Vector(v=np.arange(10, 20, 1))
    y = Vector(v=np.arange(20, 30, 1))
    res = MULTIPLY.MULTIPLY(a=x, b=[y])

    np.testing.assert_allclose(res.v, x.v*y.v)


def test_MULTIPLY_vec_scalar(mock_flojoy_decorator):

    import MULTIPLY

    x = Vector(v=np.arange(-10, 10, 1))
    res = MULTIPLY.MULTIPLY(a=x, b=[Scalar(c=2), Scalar(c=3)])

    np.testing.assert_allclose(res.v, (x.v*2)*3)


def test_MULTIPLY_ordered_pair_vector(mock_flojoy_decorator):

    import MULTIPLY

    x = np.arange(10, 20, 1)
    y = np.arange(20, 30, 1)
    z = np.arange(30, 40, 1)
    res = MULTIPLY.MULTIPLY(a=OrderedPair(x=x, y=y), b=[Vector(v=z)])

    np.testing.assert_allclose(res.x, x)
    np.testing.assert_allclose(res.y, y*z)