import numpy

from functools import wraps
from unittest.mock import patch

import pytest
import numpy as np
from flojoy import DataContainer
from PIL import Image
from pathlib import Path

def test_STABILITY_UPSCALING(mock_flojoy_decorator):
    import STABILITY_UPSCALING
    image_path = Path(__file__).parent / "test_img.png"
    output_width = 1024
    res = STABILITY_UPSCALING.STABILITY_UPSCALING(
        output_width=output_width,
        image_path=image_path
    )

    assert res.type == 'image'
    assert isinstance(res.r, numpy.ndarray)
    assert isinstance(res.g, numpy.ndarray)
    assert isinstance(res.b, numpy.ndarray)

    img_array = np.stack([res.r, res.g, res.b], axis=2)
    img = Image.fromarray(img_array, 'RGB')
    assert img.width == output_width
