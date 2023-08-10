from flojoy import flojoy, TextBlob


@flojoy
def TEXT_VIEW(default: TextBlob):
    """
    The TEXT_VIEW node creates a text visualization for a given TextBlob DataContainer type.

    Inputs
    ------
    default : TextBlob
        DataContainer object to be visualized in text format

    """

    return default
