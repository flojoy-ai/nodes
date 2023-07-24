import numpy as np
from flojoy import OrderedPair, Matrix, Scalar


def test_MOMENT(mock_flojoy_decorator):
    import MOMENT

    element_a = OrderedPair(x=np.ones(50), y=np.arange(1, 51))
    res = MOMENT.MOMENT(default=element_a)

    # check that the outputs are one of the correct types.
    assert isinstance(res, Scalar | OrderedPair | Matrix)
