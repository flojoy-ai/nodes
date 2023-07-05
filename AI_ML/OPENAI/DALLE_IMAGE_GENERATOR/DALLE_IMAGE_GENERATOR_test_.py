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
import DALLE_IMAGE_GENERATOR


def test_DALLE_IMAGE_GENERATOR():
    # Generate random time series data
    prompt = "A painting of a cat"

    res = DALLE_IMAGE_GENERATOR.DALLE_IMAGE_GENERATOR(
        [DataContainer()], {"prompt": prompt}
    )

    # Should get back a dataframe
    assert res.type == "image"
    assert isinstance(res.r, numpy.ndarray)
    assert isinstance(res.g, numpy.ndarray)
    assert isinstance(res.b, numpy.ndarray)
