import numpy as np
from flojoy import OrderedPair


def test_PEAK_DETECTION(mock_flojoy_decorator):
    import PEAK_DETECTION

    x = np.linspace(0.0, 2, 1000)
    y = np.sin(np.pi * x)

    element = OrderedPair(x=x, y=y)
    res = PEAK_DETECTION.PEAK_DETECTION(element)

    # PEAK_DETECTION should detect one peak at x = 0.5 y = 1
    assert np.isclose(res.x[0], 0.5, atol=0.01)
    assert np.isclose(res.y, 1, atol=0.01)
