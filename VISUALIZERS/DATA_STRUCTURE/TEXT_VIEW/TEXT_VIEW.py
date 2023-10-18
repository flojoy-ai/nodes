import pprint
from flojoy import flojoy, TextBlob


@flojoy
def TEXT_VIEW(default: TextBlob, prettify: bool = False) -> TextBlob:
    """The TEXT_VIEW node creates a text visualization for a given TextBlob DataContainer type.

    Inputs
    ------
    default : TextBlob
        The DataContainer to be visualized in text format

    Parameters
    ----------
    prettify : Boolean
        Whether to prettify the displayed text (defaults to True)

    Returns
    -------
    TextBlob
        The DataContainer containing text data
    """

    s = default.text_blob

    if prettify:
        s = pprint.pformat(default.text_blob)

    return TextBlob(s)
