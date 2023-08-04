import pytest
import os


# def test_DALLE_IMAGE_GENERATOR_no_api_key(mock_flojoy_decorator):
#     import JSON_EXTRACTOR

#     with pytest.raises(Exception, match="OPENAI_API_KEY environment variable not set"):
#         properties = "price,name,model"
#         prompt = """Headset Gamer Bluetooth MJ23 - $100
# Extract the price, name and model from the above text."""
#         res = JSON_EXTRACTOR.JSON_EXTRACTOR(
#             properties=properties,
#             prompt=prompt,
#         )


def test_JSON_EXTRACTOR(mock_flojoy_decorator):
    api_key = os.getenv("OPENAI_API_KEY", None)
    if api_key:
        import JSON_EXTRACTOR

        properties = "price,name,model"
        prompt = """Headset Gamer Bluetooth MJ23 - $100 
Extract the price, name and model from the above text."""
        mock_properties_list = ["price", "name", "model"]
        res = JSON_EXTRACTOR.JSON_EXTRACTOR(
            properties=properties,
            prompt=prompt,
        )
        for property in mock_properties_list:
            assert property in res.m.columns
