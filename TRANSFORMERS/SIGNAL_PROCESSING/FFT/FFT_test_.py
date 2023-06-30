import numpy as np
from scipy import fft
from functools import wraps
from unittest.mock import patch
from flojoy import DataContainer


def mock_flojoy_decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)

    return decorated_function


patch("flojoy.flojoy", mock_flojoy_decorator).start()

import FFT


def test_FFT():
    N = 600
    T = 1.0 / 800.0
    x = np.linspace(0.0, N * T, N, endpoint=False)
    y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * x)
    element = DataContainer(x=x, y=y)
    res = FFT.FFT(
        [element],
        {
            "window_type": "none",
            "real_signal": False,
            "sample_rate": 800.0,
            "display": True,
        },
    )

    yf = fft.fft(y)
    yf = np.abs(fft.fftshift(yf))
    xf = fft.fftfreq(N, T)
    xf = fft.fftshift(xf)

    assert (yf == res.y).all()
    assert (xf == res.x).all()
