import os
import pytest
import numpy as np
import json


def test_MOCK_WEINSCHEL8320(
    mock_flojoy_decorator,
    mock_flojoy_venv_cache_directory,
    cleanup_flojoy_cache_fixture,
):
    import MOCK_WEINSCHEL8320

    dB = MOCK_WEINSCHEL8320.MOCK_WEINSCHEL8320()

    assert dB.c == 10.0
