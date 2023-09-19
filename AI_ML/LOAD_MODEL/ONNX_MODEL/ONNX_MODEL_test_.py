import os

import urllib.request

import numpy as np

from flojoy import Vector
from tempfile import TemporaryDirectory


def test_ONNX_MODEL_default(
    mock_flojoy_decorator,
    mock_flojoy_venv_cache_directory,
    cleanup_flojoy_cache_fixture,
):
    """ONNX_MODEL functional test for the example application."""
    from ONNX_MODEL import ONNX_MODEL

    # The ONNX model zoo is a collection of pre-trained models for common
    # machine learning tasks. The models are stored in ONNX format.
    # The repository is not updated frequently.
    # See: https://github.com/onnx/models/commits/69c5d3751dda5349fd3fc53f525395d180420c07/
    ONNX_MODEL_ZOO_BASE_URL = "https://github.com/onnx/models/raw/69c5d3751dda5349fd3fc53f525395d180420c07/vision"

    with TemporaryDirectory() as temp_dir:
        full_path = os.path.join(temp_dir, "model.onnx")
        urllib.request.urlretrieve(
            url=f"{ONNX_MODEL_ZOO_BASE_URL}/classification/alexnet/model/bvlcalexnet-12-int8.onnx",
            filename=full_path,
        )

        input_tensor = Vector(v=np.random.random((1, 3, 224, 224)))

        image_vector = ONNX_MODEL(
            default=input_tensor,
            file_path=full_path,
        )

    assert isinstance(image_vector, Vector)
