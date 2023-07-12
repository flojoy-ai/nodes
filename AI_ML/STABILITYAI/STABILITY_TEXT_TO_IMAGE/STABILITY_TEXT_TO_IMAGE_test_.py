import numpy

from functools import wraps
from unittest.mock import patch

import numpy as np
import pandas as pd
from flojoy import DataContainer


def mock_flojoy_decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)

    return decorated_function


# Patch the flojoy decorator that handles connecting our node to the App.
patch("flojoy.flojoy", mock_flojoy_decorator).start()

# After Patching the flojoy decorator, let's load the node under test.
import STABILITY_TEXT_TO_IMAGE


def test_STABILITY_TEXT_TO_IMAGE():
    prompt = "A painting of a cat"
    width = 512
    height = 512
    res = STABILITY_TEXT_TO_IMAGE.STABILITY_TEXT_TO_IMAGE(
        [DataContainer()], {"prompt": prompt, "width": width, "height": height}
    )

    assert res.type == 'image'
    assert isinstance(res.r, numpy.ndarray)
    assert isinstance(res.g, numpy.ndarray)
    assert isinstance(res.b, numpy.ndarray)
