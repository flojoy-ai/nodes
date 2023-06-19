import numpy as np
from scipy import fft

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
import TWO_DIMENSIONAL_FFT

def test_2DFFT():
    m = np.mgrid[:5, :5][0]
    element = DataContainer(type="matrix", m=m)
    res = TWO_DIMENSIONAL_FFT.TWO_DIMENSIONAL_FFT([element], {"real_signal": False, "color": "red"})
    expected = fft.fft2(m).real
    assert (expected == res.m).all()