import numpy as np


def test_TEXT(mock_flojoy_decorator):
    import TEXT

    res = TEXT.TEXT(value="Hello World!")
    assert np.equal("Hello World!", res.text_blob)
