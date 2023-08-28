import os
import pytest

from PIL import Image as PIL_Image
import numpy as np

from flojoy import Image, DataFrame


@pytest.fixture
def ada_lovelace_array_rgb():
    _image_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "assets",
        "ada_lovelace.png",
    )
    image = PIL_Image.open(_image_path).convert("RGB")
    return np.array(image, copy=True)


@pytest.mark.slow
def test_HUGGING_FACE_PIPELINE(
    mock_flojoy_decorator,
    mock_flojoy_venv_cache_directory,
    cleanup_flojoy_cache_fixture,
    ada_lovelace_array_rgb,
):
    from HUGGING_FACE_PIPELINE import HUGGING_FACE_PIPELINE

    input_image = Image(
        r=ada_lovelace_array_rgb[:, :, 0],
        g=ada_lovelace_array_rgb[:, :, 1],
        b=ada_lovelace_array_rgb[:, :, 2],
        a=None,
    )

    df_classification_confidence_scores = HUGGING_FACE_PIPELINE(
        default=input_image,
        model="google/vit-base-patch16-224",
        revision="5dca96d",
    )

    assert isinstance(df_classification_confidence_scores, DataFrame)

    first_class_confidence_scores = classification_confidence_scores.iloc[0, :]

    assert first_class_confidence_scores["label"] == "overskirt"
    assert first_class_confidence_scores["score"] > 0.725
