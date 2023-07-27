import numpy as np
from flojoy import Vector


def test_SECOND_ORDER_SYSTEM(mock_flojoy_decorator):
    import SECOND_ORDER_SYSTEM
    from flojoy import DefaultParams

    defaultP = DefaultParams(
        node_id="SECOND_ORDER_SYSTEM", job_id="0", jobset_id="0", node_type="default"
    )

    # TODO: rewrite this test using a mock SmallMemory.
    x = np.linspace(0, 10, 1000)
    v = Vector(v=x),

    res = SECOND_ORDER_SYSTEM.SECOND_ORDER_SYSTEM(default=v, default_params=defaultP)

    assert np.array_equal(res.x, x)
    assert np.allclose(res.y, np.zeros(1000), atol=1e-03)
