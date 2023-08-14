from flojoy import flojoy, TextBlob


@flojoy
def TEXT_VIEW(default: TextBlob):
    """The TEXT_VIEW node creates a text visualization for a given TextBlob DataContainer type.

    Inputs
    ------
    default : TextBlob
        the DataContainer to be visualized in text format

    Returns
    -------
    TextBlob
        the DataContainer containing text data
    """

    return default
