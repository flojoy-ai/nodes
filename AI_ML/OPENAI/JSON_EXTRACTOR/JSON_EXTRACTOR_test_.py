from functools import wraps
import pytest

def test_JSON_EXTRACTOR(mock_flojoy_decorator):
    import JSON_EXTRACTOR
    properties = "price,name,model"
    prompt = """Headset Gamer Bluetooth MJ23 - $100 
Extract the price, name and model from the above text.
"""
    mock_properties_list = ["price", "name", "model"]
    res = JSON_EXTRACTOR.JSON_EXTRACTOR(
        properties=properties,
        prompt=prompt,
    )

    for property in mock_properties_list:
        assert property in res.m.columns
