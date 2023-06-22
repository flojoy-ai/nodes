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
import APPEND


def test_APPEND():
    # create the two ordered pair datacontainers
    element_a = DataContainer(
        type="ordered_pair", x=numpy.linspace(0, 10, 10), y=numpy.linspace(0, 10, 10)
    )

    element_b = DataContainer(
        type="ordered_pair", x=numpy.linspace(11, 12, 1), y=numpy.linspace(11, 12, 1)
    )

    # node under test
    res = APPEND.APPEND([element_a, element_b], {})

    # check that the correct number of elements
    print(res.y, type(res.y), len(res.y))
    assert (len(res.y)) == 11
    assert res.y[-1] == 11
