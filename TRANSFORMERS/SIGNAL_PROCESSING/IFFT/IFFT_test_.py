import numpy as np
from scipy import fft
from pandas import DataFrame

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
import IFFT


def test_IFFT():
    N = 600
    T = 1.0 / 800.0
    x = np.linspace(0.0, N * T, N, endpoint=False)
    y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * x)
    fourier = fft.fft(y)

    d = {"x": x, "real": fourier.real, "imag": fourier.imag}
    element = DataContainer(type="dataframe", m=DataFrame(data=d))
    res = IFFT.IFFT([element], {"real_signal": False})

    original = fft.ifft(fourier).real
    assert (x == res.x).all()
    assert (original == res.y).all()
