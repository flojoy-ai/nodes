import pytest
from unittest.mock import patch

@pytest.fixture
def mock_flojoy_decorator():
    with patch("flojoy.flojoy", lambda x: x) as mock_flojoy:
        yield mock_flojoy