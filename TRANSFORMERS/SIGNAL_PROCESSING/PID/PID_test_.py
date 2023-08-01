import numpy as np
from flojoy import OrderedPair, DefaultParams


def test_PID(mock_flojoy_decorator):
    import PID

    default = DefaultParams(
        node_id="PID", job_id="0", jobset_id="0", node_type="default"
    )

    x = np.linspace(0.0, 10.0, 1000)
    y = np.linspace(2.0, 2.0, 1000)

    element = OrderedPair(x=x, y=y)
    res = PID.PID(element, default_params=default)

    # PID value should be close to 128.8 with input 2.0.
    assert np.isclose(np.mean(res.y), 128.8, atol=0.5)
