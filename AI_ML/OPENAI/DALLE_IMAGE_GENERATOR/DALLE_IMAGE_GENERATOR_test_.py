import numpy

def test_DALLE_IMAGE_GENERATOR(mock_flojoy_decorator):
    import DALLE_IMAGE_GENERATOR
    # Generate random time series data
    prompt = "A painting of a cat"

    res = DALLE_IMAGE_GENERATOR.DALLE_IMAGE_GENERATOR(
        prompt=prompt,
    )

    # Should get back a dataframe
    assert res.type == "image"
    assert isinstance(res.r, numpy.ndarray)
    assert isinstance(res.g, numpy.ndarray)
    assert isinstance(res.b, numpy.ndarray)
