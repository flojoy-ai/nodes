import os
import pytest
from unittest.mock import patch

import requests
from PIL import Image
import numpy as np

from flojoy import DataContainer


@pytest.fixture(scope="module")
def mock_flojoy_decorator():
    with patch("flojoy.flojoy", lambda x: x) as mock_flojoy:
        yield mock_flojoy


@pytest.fixture
def obama_image_array_rgb():
    _image_path = (
        f"{os.path.dirname(os.path.realpath(__file__))}/obama_image.jpg"
    )
    image = Image.open(_image_path).convert("RGB")
    return np.array(image)


@pytest.fixture
def obama_segmentation_array_rgb():
    _image_path = (
        f"{os.path.dirname(os.path.realpath(__file__))}/obama_segmentation_image.jpg"
    )
    image = Image.open(_image_path).convert("RGB")
    return np.array(image)


def test_DEEPLAB_V3(
    mock_flojoy_decorator, obama_image_array_rgb, obama_segmentation_array_rgb
):
    import DEEPLAB_V3

    input_dc = DataContainer(
        type="image",
        r=obama_image_array_rgb[:, :, 0],
        g=obama_image_array_rgb[:, :, 1],
        b=obama_image_array_rgb[:, :, 2],
        a=None,
    )
    output_dc = DEEPLAB_V3.DEEPLAB_V3(dc_inputs=[input_dc], params={})
    output_segmentation = np.stack((output_dc.r, output_dc.g, output_dc.b), axis=2)

    # Threshold both segmentation masks
    output_segmentation = (output_segmentation > 0).astype(np.uint8) * 255
    expected_segmentation = (obama_segmentation_array_rgb > 0).astype(np.uint8) * 255

    # Compare mean pixel difference of thresholded masks
    assert np.mean(np.abs(output_segmentation - expected_segmentation)) < 1
