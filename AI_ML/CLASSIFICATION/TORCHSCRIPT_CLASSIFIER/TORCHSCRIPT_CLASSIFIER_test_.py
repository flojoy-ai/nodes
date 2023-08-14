import pytest
import os
import json
import pandas as pd
import numpy as np
import PIL
from flojoy import Image, DataFrame


@pytest.fixture
def torchscript_model_path():
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "assets",
        "mbnet_v3_small.torchscript",
    )


@pytest.fixture
def class_names():
    json_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "assets", "class_names.json"
    )
    with open(json_path, "r") as f:
        class_names_json = json.load(f)
    return DataFrame(df=pd.Series(class_names_json).to_frame())


@pytest.fixture
def obama_image():
    _image_path = f"{os.path.dirname(os.path.realpath(__file__))}/assets/President_Barack_Obama.jpg"
    image = np.array(PIL.Image.open(_image_path).convert("RGB"))
    return Image(r=image[:, :, 0], g=image[:, :, 1], b=image[:, :, 2], a=None)


@pytest.mark.slow
def test_TORHSCRIPT_CLASSIFIER(
    mock_flojoy_decorator,
    mock_flojoy_venv_cache_directory,
    obama_image,
    torchscript_model_path,
    class_names,
):
    import TORCHSCRIPT_CLASSIFIER

    # Test the model
    clf_output = TORCHSCRIPT_CLASSIFIER.TORCHSCRIPT_CLASSIFIER(
        input_image=obama_image,
        model_path=torchscript_model_path,
        class_names=class_names,
    )

    assert clf_output.m.iloc[0].class_name == "suit, suit of clothes"
