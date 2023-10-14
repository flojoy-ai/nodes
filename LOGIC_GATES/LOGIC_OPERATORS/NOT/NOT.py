from flojoy import flojoy, Boolean

@flojoy
def NOT(default: Boolean) -> Boolean:
    """The NOT node takes a boolean data type and computs logical NOT operation on them.

    Inputs
    ------
    default : Boolean
        The input boolean to which we apply the NOT operation.

    Returns
    -------
    Boolean
        The boolean result from the operation of the input.
    """
    reverse = not default.b
    return Boolean(b=reverse)