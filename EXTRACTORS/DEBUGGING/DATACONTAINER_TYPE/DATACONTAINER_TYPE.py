from flojoy import flojoy, DataContainer, TextBlob


@flojoy()
def DATACONTAINER_TYPE(
    default: DataContainer,
) -> TextBlob:
    """The DATACONTAINER_TYPE node

    Returns
    -------
    DataContainer
        TextBlob:
    """

    return TextBlob(text_blob=str(default.type))
