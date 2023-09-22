from flojoy import TextBlob, flojoy, DataContainer
from typing import Optional


@flojoy
def TEXT(
    _: Optional[DataContainer] = None,
    value: str = "Hello World!",
) -> TextBlob:
    """The TEXT node returns a TextBlob DataContainer.

    Parameters
    ----------
    value : str
        The value set in Parameters.

    Returns
    -------
    TextBlob
        Return the value being set in Parameters.
    """

    return TextBlob(text_blob=value)
