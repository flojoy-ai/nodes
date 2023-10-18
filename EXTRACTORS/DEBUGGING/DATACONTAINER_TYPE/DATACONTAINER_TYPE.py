from flojoy import flojoy, DataContainer, TextBlob


@flojoy()
def DATACONTAINER_TYPE(
    default: DataContainer,
) -> TextBlob:
    """The DATACONTAINER_TYPE node returns a TextBlob containing the input DataContainer type (e.g. Vector).

    Must use the TEXT_VIEW node to view the text.

    Returns
    -------
    DataContainer
        TextBlob: Input DataContainer type
    """

    return TextBlob(text_blob=default.type)
