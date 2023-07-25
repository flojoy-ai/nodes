
import numpy
import numpy as np
from PIL import Image
from pathlib import Path
import pytest
import os


def test_STABILITY_IMAGE_TO_IMAGE_no_api_key(mock_flojoy_decorator):
    import STABILITY_IMAGE_TO_IMAGE
    with pytest.raises(ValueError, match='STABILITY_API_KEY environment variable is required'):
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



def test_STABILITY_IMAGE_TO_IMAGE(mock_flojoy_decorator):
    api_key = os.getenv("STABILITY_API_KEY", None)
    if api_key:
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
