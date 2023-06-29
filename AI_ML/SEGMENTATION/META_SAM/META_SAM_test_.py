import os
import pytest
from unittest.mock import patch

from PIL import Image
import numpy as np

from flojoy import DataContainer


@pytest.fixture(scope="module")
def mock_flojoy_decorator():
    with patch("flojoy.flojoy", lambda x: x) as mock_flojoy:
        yield mock_flojoy


@pytest.fixture
def oratoire_image_array_rgb():
    _image_path = (
        f"{os.path.dirname(os.path.realpath(__file__))}/oratoire.jpg"
    )
    image = Image.open(_image_path).convert("RGB").resize((512, 512))
    return np.array(image)


def test_META_SAM(mock_flojoy_decorator, oratoire_image_array_rgb):
    import META_SAM

    input_dc = DataContainer(
        type="image",
        r=oratoire_image_array_rgb[:, :, 0],
        g=oratoire_image_array_rgb[:, :, 1],
        b=oratoire_image_array_rgb[:, :, 2],
        a=None,
    )
    output_dc = META_SAM.META_SAM(dc_inputs=[input_dc], params={})
    assert output_dc.type == "image"
    assert output_dc.r.shape == (512, 512)
    assert output_dc.g.shape == (512, 512)
    assert output_dc.b.shape == (512, 512)
    assert output_dc.a.shape == (512, 512)