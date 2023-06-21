import os
import pytest
from unittest.mock import patch

import pandas as pd

from flojoy import DataContainer


@pytest.fixture(scope="module")
def mock_flojoy_decorator():
    with patch("flojoy.flojoy", lambda x: x) as mock_flojoy:
        yield mock_flojoy


@pytest.fixture
def long_text():
    _file_path = (
        f"{os.path.dirname(os.path.realpath(__file__))}/story.txt"
    )
    with open(_file_path, "r") as f:
        text = f.read()
    return text


def test_BART_LARGE_CNN(mock_flojoy_decorator, long_text):

    import BART_LARGE_CNN

    input_dc = DataContainer(
        type="dataframe",
        m=pd.DataFrame({"text": [long_text] * 3}),
    )

    input_dc.m.iloc[:1].to_csv("test_BART_LARGE_CNN_input.csv", index=False)

    output_dc = BART_LARGE_CNN.BART_LARGE_CNN(dc_inputs=[input_dc], params={})
    assert output_dc.type == "dataframe"
    assert output_dc.m.shape == (3, 1)
    assert output_dc.m.columns == ["summary_text"]