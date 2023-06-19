import numpy as np

from functools import wraps
from unittest.mock import patch


def mock_flojoy_decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)

    return decorated_function


patch("flojoy.flojoy", mock_flojoy_decorator).start()

import MATRIX


def test_MATRIX():
    # create the two matrices
    m1 = MATRIX.MATRIX([], {"row": 3, "column": 4})
    m2 = MATRIX.MATRIX([], {"row": 3, "column": 4})

    # Check if they are equal
    assert np.array_equal(m1, m2)
