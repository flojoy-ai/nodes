import numpy as np
from flojoy import Image


def test_CHANNEL_SPLIT(mock_flojoy_decorator):
    import CHANNEL_SPLIT

    red = 255 * np.ones((600, 600), dtype=np.uint8)
    green = 255 * np.ones((600, 600), dtype=np.uint8)
    blue = 255 * np.ones((600, 600), dtype=np.uint8)
    alpha = np.ones((600, 600), dtype=np.uint8)

    input = Image(r=red, g=green, b=blue, a=alpha)
    res = CHANNEL_SPLIT.CHANNEL_SPLIT(input)
    r = res[0].r
    g = res[1].g
    b = res[2].b
    a = res[3].a

    # Assert returns image channels are matching the input channel
    assert np.isclose(red, r, atol=0.1)
    assert np.isclose(green, g, atol=0.1)
    assert np.isclose(blue, b, atol=0.1)
    assert np.isclose(alpha, a, atol=0.1)
