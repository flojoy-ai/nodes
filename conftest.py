import pytest
import tempfile
from functools import wraps
from unittest.mock import patch


@pytest.fixture
def mock_flojoy_decorator():
    """A fixture that mocks the flojoy decorator to a no-op decorator that does not create a Flojoy node"""
    def no_op_decorator(func=None, **kwargs):
        def decorator(func):
            @wraps(func)
            def decorated_function(*args, **kwargs):
                return func(*args, **kwargs)

            return decorated_function

        if func is not None:
            return decorator(func)

        return decorator

    with patch("flojoy.flojoy") as mock_flojoy:
        mock_flojoy.side_effect = no_op_decorator
        yield mock_flojoy


@pytest.fixture
def mock_flojoy_cache_directory():
    """A fixture that mocks the flojoy cache directory to a temporary directory that is cleaned up automatically after each test function"""
    with tempfile.TemporaryDirectory() as tempdir:
        with patch("flojoy.flojoy_node_venv._get_venv_cache_dir", return_value=tempdir) as mock_venv_cache_dir:
            yield mock_venv_cache_dir