import pytest
from functools import wraps
from unittest.mock import patch

@pytest.fixture
def mock_flojoy_decorator():

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