from flojoy import flojoy, DataContainer, TextBlob


@flojoy()
def PRINT_DATACONTAINER(
    default: DataContainer,
) -> TextBlob:
    """The PRINT_DATACONTAINER node

    Returns
    -------
    DataContainer
        TextBlob:
    """

    return TextBlob(text_blob=str(default))
