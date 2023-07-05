import numpy
from pathlib import Path
from functools import wraps
from unittest.mock import patch
import json
from flojoy import DataContainer


def mock_flojoy_decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)

    return decorated_function


# Patch the flojoy decorator that handles connecting our node to the App.
patch("flojoy.flojoy", mock_flojoy_decorator).start()

# After Patching the flojoy decorator, let's load the node under test.
import JSON_EXTRACTOR


def test_JSON_EXTRACTOR():
    properties = "price,name,model"
    prompt = """Headset Gamer Bluetooth MJ23 - $100 
Extract the price, name and model from the above text.
"""
    mock_properties_list = ["price", "name", "model"]
    params = dict(properties=properties, prompt=prompt)
    res = JSON_EXTRACTOR.JSON_EXTRACTOR([DataContainer()], params)

    for property in mock_properties_list:
        assert property in res.m.columns
