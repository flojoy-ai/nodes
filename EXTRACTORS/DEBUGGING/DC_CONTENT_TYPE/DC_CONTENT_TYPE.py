from flojoy import flojoy, DataContainer, TextBlob


@flojoy()
def DC_CONTENT_TYPE(
    default: DataContainer,
) -> TextBlob:
    """The DC_CONTENT_TYPE node

    Returns
    -------
    DataContainer
        TextBlob:
    """

    dc_type = str(default.type)

    match dc_type:
        case "OrderedPair":
            s = f"x: {type(default.x)}, \ny: {type(default.y)}"
        case "OrderedTriple":
            s = f"x: {type(default.x)}, \ny: {type(default.y)}, \nz: {type(default.z)}"
        case "Surface":
            s = f"x: {type(default.x)}, \ny: {type(default.y)}, \nz: {type(default.z)}"
        case "Vector":
            s = f"v: {type(default.v)}"
        case "Matrix":
            s = f"m: {type(default.m)}"
        case "Grayscale":
            s = f"m: {type(default.m)}"
        case "DataFrame":
            s = f"m: {type(default.m)}"
        case "Scalar":
            s = f"c: {type(default.c)}"
        case "Image":
            s = f"r: {type(default.r)}, \ng: {type(default.g)}, \nb: {type(default.b)}"
        case "TextBlob":
            s = f"text_blob: {type(default.text_blob)}"
        case _:
            raise TypeError(
                f"Unsupported DC type {dc_type}. Please add it to the node."
            )

    return TextBlob(text_blob=s)
