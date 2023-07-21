import pytest
import numpy
import numpy as np
from PIL import Image
from pathlib import Path



def test_STABILITY_IMAGE_TO_IMAGE(mock_flojoy_decorator):
    import STABILITY_IMAGE_TO_IMAGE
    prompt = "Rocket ship launching under a dark sky"
    image_path = Path(__file__).parent / "test_img.png"
    width = 512
    height = 512
    res = STABILITY_IMAGE_TO_IMAGE.STABILITY_IMAGE_TO_IMAGE(
        prompt=prompt,
        width=width,
        height=height,
        image_path=image_path
    )

    assert res.type == 'image'
    assert isinstance(res.r, numpy.ndarray)
    assert isinstance(res.g, numpy.ndarray)
    assert isinstance(res.b, numpy.ndarray)

    img_array = np.stack([res.r, res.g, res.b], axis=2)
    img = Image.fromarray(img_array, 'RGB')
    assert img.width == width
    assert img.height == height
