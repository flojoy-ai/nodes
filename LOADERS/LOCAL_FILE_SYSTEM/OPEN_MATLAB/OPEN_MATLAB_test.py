import os
import pytest


@pytest.fixture
def output_shape():
    return (1831, 22)


@pytest.mark.slow
def test_OPEN_MATLAB(mock_flojoy_decorator, mock_flojoy_cache_directory, output_shape):
    import OPEN_MATLAB

    _file_path = f"{os.path.dirname(os.path.realpath(__file__))}/assets/default.mat"
    output = OPEN_MATLAB.OPEN_MATLAB(_file_path)

    assert output.m.shape == output_shape
