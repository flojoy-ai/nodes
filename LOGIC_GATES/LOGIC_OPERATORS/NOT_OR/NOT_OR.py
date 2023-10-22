from flojoy import flojoy, Boolean

@flojoy
def NOT_OR(default: Boolean, a: Boolean) -> Boolean:
    """The NOT_OR node takes two boolean data type and computs logical NOT OR operation on them.

    Inputs
    ------
    default : Boolean
        The input boolean to which we apply the NOT OR operation.

    a : Boolean
        The input boolean to which we apply the NOT OR operation.

    Returns
    -------
    Boolean
        The boolean result from the operation of the inputs.
    """
    if not default.b and not a.b:
        return Boolean(b=True)
    return Boolean(b=False)