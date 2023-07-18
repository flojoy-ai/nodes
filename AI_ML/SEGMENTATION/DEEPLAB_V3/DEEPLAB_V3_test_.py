import os
import pytest
from unittest.mock import patch

from PIL import Image as PIL_Image
import numpy as np

from flojoy import Image


@pytest.fixture
def obama_image_array_rgb():
    _image_path = (
        f"{os.path.dirname(os.path.realpath(__file__))}/assets/obama_image.jpg"
    )
    image = PIL_Image.open(_image_path).convert("RGB")
    return np.array(image)


@pytest.fixture
def obama_segmentation_array_rgb():
    _image_path = f"{os.path.dirname(os.path.realpath(__file__))}/assets/obama_segmentation_image.jpg"
    image = PIL_Image.open(_image_path).convert("RGB")
    return np.array(image)


def test_DEEPLAB_V3(
    mock_flojoy_decorator, obama_image_array_rgb, obama_segmentation_array_rgb
):
    import DEEPLAB_V3

    input_image = Image(
        r=obama_image_array_rgb[:, :, 0],
        g=obama_image_array_rgb[:, :, 1],
        b=obama_image_array_rgb[:, :, 2],
        a=None,
    )
    output_dc = DEEPLAB_V3.DEEPLAB_V3(default=input_image)  # type: ignore
    output_segmentation = np.stack((output_dc.r, output_dc.g, output_dc.b), axis=2)

    # Threshold both segmentation masks
    output_segmentation = (output_segmentation > 0).astype(np.uint8) * 255
    expected_segmentation = (obama_segmentation_array_rgb > 0).astype(np.uint8) * 255

    # Compare mean pixel difference of thresholded masks
    assert np.mean(np.abs(output_segmentation - expected_segmentation)) < 1
