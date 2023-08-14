from flojoy import flojoy, TextBlob


@flojoy
def TEXT(
    value: str = "Hello World!",
) -> TextBlob:
    """The TEXT node returns a TextBlob DataContainer.

    Parameters
    ----------
    value: str
        The value set in Parameters

    Returns
    -------
    TextBlob
        text_blob: return the value being set in Parameters
    """

    return TextBlob(text_blob=value)
