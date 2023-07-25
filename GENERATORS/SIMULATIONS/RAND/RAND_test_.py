import numpy as np

from flojoy import Vector


def test_RAND_single_value_uniform(mock_flojoy_decorator):
    import RAND

    res = RAND.RAND(default=None, distribution="uniform", lower_bound=0, upper_bound=1)
    assert res.c < 1
    assert res.c > 0


def test_RAND_array_value_uniform(mock_flojoy_decorator):
    import RAND

    x = Vector(v=np.arange(0, 99, 2))
    res = RAND.RAND(default=x, distribution="uniform", lower_bound=0, upper_bound=1)
    assert np.all(res.x == x.v)
    assert np.all(res.y < 1)
    assert np.all(res.y > 0)


def test_RAND_single_value_normal(mock_flojoy_decorator):
    import RAND

    res = RAND.RAND(
        default=None, distribution="normal", normal_mean=0, normal_standard_deviation=1
    )
    assert abs(res.c) < 5


def test_RAND_array_value_normal(mock_flojoy_decorator):
    import RAND

    x = Vector(v=np.arange(0, 100000, 1))
    res = RAND.RAND(
        default=x, distribution="normal", normal_mean=0, normal_standard_deviation=1
    )
    # Test for shape
    assert np.all(res.x == x.v)
    assert res.y.shape == x.v.shape
    # Test for mean and std
    assert abs(np.mean(res.y)) < 0.01
    assert abs(np.std(res.y) - 1) < 0.01


def test_RAND_single_value_poisson(mock_flojoy_decorator):
    import RAND

    res = RAND.RAND(default=None, distribution="poisson", poisson_events=1)
    assert res.c.shape == (1,) and isinstance(res.c[0].item(), int)
    assert res.c < 10


def test_RAND_array_value_poisson(mock_flojoy_decorator):
    import RAND

    x = Vector(v=np.arange(0, 100000, 1))
    res = RAND.RAND(default=x, distribution="poisson", poisson_events=1)
    assert np.all(res.x == x.v)
    assert res.y.shape == x.v.shape
    assert abs(np.mean(res.y) - 1) < 0.01
