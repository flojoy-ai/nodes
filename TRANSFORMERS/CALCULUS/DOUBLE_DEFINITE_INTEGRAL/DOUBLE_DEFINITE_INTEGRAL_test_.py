def test_DOUBLE_DEFINITE_INTEGRAL(mock_flojoy_decorator):
    import DOUBLE_DEFINITE_INTEGRAL
    import numpy as np

    function = "2*x*y"
    node = DOUBLE_DEFINITE_INTEGRAL.DOUBLE_DEFINITE_INTEGRAL(function, 1, 0, 1, 0)

    print(node.c)
    assert np.array_equal(np.array([0.5]), node.c)
