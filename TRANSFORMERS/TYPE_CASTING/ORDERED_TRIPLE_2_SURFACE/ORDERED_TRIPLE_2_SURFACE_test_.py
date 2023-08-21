from flojoy import OrderedTriple
import numpy as np


def test_ORDERED_TRIPLE_2_SURFACE_general(mock_flojoy_decorator):
    import ORDERED_TRIPLE_2_SURFACE

    ordTriple = OrderedTriple(
        x=np.array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]),
        y=np.array([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]),
        z=np.array([0.0, 3.9, 2.4, 5.0, 1.2, 3.3, 3.4, 3.5, 0.9, 8.7, 5.6, 7.1]),
    )
    out = ORDERED_TRIPLE_2_SURFACE.ORDERED_TRIPLE_2_SURFACE(ordTriple)

    np.testing.assert_array_equal(([[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]), out.x)
    np.testing.assert_array_equal(([[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]]), out.y)
    np.testing.assert_array_equal(
        ([[0.0, 3.9, 2.4, 5.0], [1.2, 3.3, 3.4, 3.5], [0.9, 8.7, 5.6, 7.1]]), out.z
    )


def test_ORDERED_TRIPLE_2_SURFACE_with_padding(mock_flojoy_decorator):
    import ORDERED_TRIPLE_2_SURFACE

    ordTriple = OrderedTriple(x=np.array([0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]), y=np.array([0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]), z=np.array([0.0, 3.9, 2.4, 5.0, 1.2, 3.3, 3.4, 3.5, 0.9]))
    out = ORDERED_TRIPLE_2_SURFACE.ORDERED_TRIPLE_2_SURFACE(ordTriple)

    print(out.z)
    assert len(out.z) == len(np.unique(ordTriple.y))
    #Test with x,y unique and len(z) smaller??
    #Test with x,y not unique and len(z) smaller??


#def test_ORDERED_TRIPLE_2_SURFACE_no_padding(mock_flojoy_decorator):
    #import ORDERED_TRIPLE_2_SURFACE

    #Test with x,y unique and len(z) bigger??
    #Test with x,y not unique and len(z) bigger
