import numpy
import pytest
import os


def test_DALLE_IMAGE_GENERATOR_no_api_key(mock_flojoy_decorator):
    import DALLE_IMAGE_GENERATOR

    with pytest.raises(Exception, match="OPENAI_API_KEY environment variable not set"):
        prompt = "A painting of a cat"
        res = DALLE_IMAGE_GENERATOR.DALLE_IMAGE_GENERATOR(
            prompt=prompt,
        )


def test_DALLE_IMAGE_GENERATOR(mock_flojoy_decorator):
    api_key = os.getenv("OPENAI_API_KEY", None)
    if api_key:
        import DALLE_IMAGE_GENERATOR

        prompt = "A painting of a cat"
        res = DALLE_IMAGE_GENERATOR.DALLE_IMAGE_GENERATOR(
            prompt=prompt,
        )
        assert res.type == "image"
        assert isinstance(res.r, numpy.ndarray)
        assert isinstance(res.g, numpy.ndarray)
        assert isinstance(res.b, numpy.ndarray)
