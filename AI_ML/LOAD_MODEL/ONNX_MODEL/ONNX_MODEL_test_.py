import os
import pytest

import urllib.request

import numpy as np

from flojoy import Vector
from tempfile import TemporaryDirectory

# The ONNX model zoo is a collection of pre-trained models for common
# machine learning tasks. The models are stored in ONNX format.
# The repository is not updated frequently.
# See: https://github.com/onnx/models/commits/69c5d3751dda5349fd3fc53f525395d180420c07/
ONNX_MODEL_ZOO_BASE_URL = (
    "https://github.com/onnx/models/raw/69c5d3751dda5349fd3fc53f525395d180420c07"
)

ALEX_NET_MODEL = f"{ONNX_MODEL_ZOO_BASE_URL}/vision/classification/alexnet/model/bvlcalexnet-12-int8.onnx"


def test_ONNX_MODEL_local_file_path(
    mock_flojoy_decorator,
    mock_flojoy_venv_cache_directory,
    cleanup_flojoy_cache_fixture,
):
    """ONNX_MODEL functional test for a local file."""
    from ONNX_MODEL import ONNX_MODEL

    with TemporaryDirectory() as temp_dir:
        full_path = os.path.join(temp_dir, "model.onnx")
        urllib.request.urlretrieve(
            url=ALEX_NET_MODEL,
            filename=full_path,
        )

        input_tensor = Vector(v=np.random.random((1, 3, 224, 224)))

        image_vector = ONNX_MODEL(
            default=input_tensor,
            file_path=full_path,
        )

    assert isinstance(image_vector, Vector)


def test_ONNX_MODEL_remote_file_path(
    mock_flojoy_decorator,
    mock_flojoy_venv_cache_directory,
    cleanup_flojoy_cache_fixture,
):
    """ONNX_MODEL functional test for a remote file path."""
    from ONNX_MODEL import ONNX_MODEL

    input_tensor = Vector(v=np.random.random((1, 3, 224, 224)))

    image_vector = ONNX_MODEL(
        default=input_tensor,
        file_path=ALEX_NET_MODEL,
    )

    assert isinstance(image_vector, Vector)


def test_ONNX_MODEL_wrong_usages(
    mock_flojoy_decorator,
    mock_flojoy_venv_cache_directory,
    cleanup_flojoy_cache_fixture,
):
    # TODO(jjerphan): assert the Exception being wrapped by `ChildProcessError`.
    from ONNX_MODEL import ONNX_MODEL

    input_tensor = Vector(v=np.random.random((1, 3, 224, 224)))

    # Wrong file path
    with pytest.raises(ChildProcessError):
        ONNX_MODEL(
            default=input_tensor,
            file_path="wrong_file_path",
        )

    # Wrong input tensor
    with pytest.raises(ChildProcessError):
        ONNX_MODEL(
            default=1,
            file_path=ALEX_NET_MODEL,
        )

    # Wrong file path
    with pytest.raises(ChildProcessError):
        ONNX_MODEL(
            default=input_tensor,
            file_path=1,
        )
