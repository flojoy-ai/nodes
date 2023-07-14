import numpy

from functools import wraps
from unittest.mock import patch

from flojoy import Matrix, DataFrame, Vector


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
import COUNT_VECTORIZER


def test_COUNT_VECTORIZER():
    # create the two ordered pair datacontainers
    element_a = Matrix(
        m=numpy.array(
            [
                "This is the first document.",
                "This document is the second document.",
                "And this is the third one.",
                "Is this the first document?",
            ]
        ),
    )

    # node under test
    res = COUNT_VECTORIZER.COUNT_VECTORIZER([element_a], {})

    # check that the outputs look correct
    assert isinstance(res, COUNT_VECTORIZER.CountVectorizerOutput)
    assert isinstance(res.tokens, DataFrame)
    assert isinstance(res.word_count_vector, Vector)
    assert (set(res.tokens.df)) == {
        "and",
        "document",
        "first",
        "is",
        "one",
        "second",
        "the",
        "third",
        "this",
    }

    assert numpy.array_equal(
        res.word_count_vector.v,
        numpy.array(
            [
                [0, 1, 1, 1, 0, 0, 1, 0, 1],
                [0, 2, 0, 1, 0, 1, 1, 0, 1],
                [1, 0, 0, 1, 1, 0, 1, 1, 1],
                [0, 1, 1, 1, 0, 0, 1, 0, 1],
            ]
        ),
    )
