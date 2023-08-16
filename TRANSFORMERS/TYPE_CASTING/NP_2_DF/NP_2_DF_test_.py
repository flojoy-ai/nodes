from flojoy import (
    DataContainer,
    DataFrame,
    OrderedPair,
    OrderedTriple,
    Matrix,
    Grayscale,
    Image,
    ParametricDataFrame,
    ParametricOrderedPair,
    ParametricOrderedTriple,
    ParametricImage,
    ParametricGrayscale,
    ParametricMatrix,
)


def test_NP_2_DF(mock_flojoy_decorator):
    import NP_2_DF

    # Test case DataFrame | ParametricDataFrame.
    # Test case OrderedPair | ParametricOrderedPair.
    # Test case OrderedTriple | ParametricOrderedTriple.
    # Test case Matrix | ParametricMatrix.
    # Test case Grayscale | ParametricGrayscale.
    # Test case Image | ParametricImage.
    # Test case when none and raise an error message.
    # Check what is the Parametric variant and try to do one or two maybe.
