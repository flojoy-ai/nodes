import numpy

from functools import wraps
from unittest.mock import patch

import numpy as np
import pandas as pd
from flojoy import DataContainer
from PIL import Image
from pathlib import Path


def mock_flojoy_decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)

    return decorated_function


# Patch the flojoy decorator that handles connecting our node to the App.
patch("flojoy.flojoy", mock_flojoy_decorator).start()

# After Patching the flojoy decorator, let's load the node under test.
import STABILITY_UPSCALING


def test_STABILITY_UPSCALING():
    image_path = Path(__file__).parent / "test_img.png"
    output_width = 1024
    res = STABILITY_UPSCALING.STABILITY_UPSCALING(
        [DataContainer()], {"output_width": output_width, "image_path": image_path}
    )

    assert res.type == 'image'
    assert isinstance(res.r, numpy.ndarray)
    assert isinstance(res.g, numpy.ndarray)
    assert isinstance(res.b, numpy.ndarray)

    img_array = np.stack([res.r, res.g, res.b], axis=2)
    img = Image.fromarray(img_array, 'RGB')
    assert img.width == output_width
