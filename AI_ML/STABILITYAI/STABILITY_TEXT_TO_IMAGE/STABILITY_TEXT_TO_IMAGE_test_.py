import numpy
import pytest
import os


def test_STABILITY_TEXT_TO_IMAGE_no_api_key(mock_flojoy_decorator):
    import STABILITY_TEXT_TO_IMAGE
    with pytest.raises(ValueError, match='STABILITY_API_KEY environment variable is required'):
         prompt = "A painting of a cat"
         width = 512
         height = 512
         res = STABILITY_TEXT_TO_IMAGE.STABILITY_TEXT_TO_IMAGE(
            prompt=prompt, 
            width=width,
            height=height
         )


def test_STABILITY_TEXT_TO_IMAGE(mock_flojoy_decorator):
    api_key = os.getenv("STABILITY_API_KEY", None)
    if api_key:
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
