import numpy

from functools import wraps
from unittest.mock import patch

from flojoy import DataContainer


# Python functions are decorated at module-loading time, So we'll need to patch our decorator
#  with a simple mock ,before loading the module.


def mock_flojoy_decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)

    return decorated_function


# Patch the flojoy decorator that handles connecting our node to the App.
patch("flojoy.flojoy", mock_flojoy_decorator).start()

# After Patching the flojoy decorator, let's load the node under test.
import ABS


def test_ABS():
    # create the two ordered pair datacontainers
    element_a = DataContainer(type="scalar", c=-10)

    # node under test
    res = ABS.ABS([element_a], {})

    # check that the correct number of elements
    for c in res.c:
        assert c == 10
