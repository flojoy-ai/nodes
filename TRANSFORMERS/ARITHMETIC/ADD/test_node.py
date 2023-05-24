import numpy

from functools import wraps
from unittest.mock import patch

from flojoy import DataContainer


# Python functions are decorated at module-loading time, So we'll need to patch our decorator 
#  with a simple mock ,before loading the module.

def mock_flojoy_decorator(f):
   @wraps(f)
   def decorated_function(*args, **kwargs):
      return f(*args, **kwargs)
   return decorated_function


# Patch the flojoy decorator that handles connecting our node to the App.
patch('flojoy.flojoy', mock_flojoy_decorator).start()

# After Patching the flojoy decorator, let's load the node under test.
import ADD

def test_ADD():

   # create the two ordered pair datacontainers
   element_a = DataContainer(
      type='ordered_pair', 
      x=numpy.linspace(-10, 10, 100), 
      y=[10]*100)

   element_b = DataContainer(
      type='ordered_pair', 
      x=numpy.linspace(-10, 10, 100), 
      y=[7]*100)

   # node under test
   res = ADD.ADD([element_a, element_b], {})

   # check that the correct number of elements
   assert(len(res.y)) == 100
   for y in res.y:
      assert y == 17  
