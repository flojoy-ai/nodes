import numpy
import pytest



def test_STABILITY_TEXT_TO_IMAGE(mock_flojoy_decorator):
    import STABILITY_TEXT_TO_IMAGE
    prompt = "A painting of a cat"
    width = 512
    height = 512
    res = STABILITY_TEXT_TO_IMAGE.STABILITY_TEXT_TO_IMAGE(
       prompt=prompt, 
       width=width,
       height=height
    )

    assert res.type == 'image'
    assert isinstance(res.r, numpy.ndarray)
    assert isinstance(res.g, numpy.ndarray)
    assert isinstance(res.b, numpy.ndarray)
