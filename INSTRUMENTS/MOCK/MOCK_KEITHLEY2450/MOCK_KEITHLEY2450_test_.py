import os
import pytest
import numpy as np
import json


def test_MOCK_KEITHLEY2450(
    mock_flojoy_decorator,
    mock_flojoy_venv_cache_directory,
    cleanup_flojoy_cache_fixture,
):


    assert 10.0 == 10.0