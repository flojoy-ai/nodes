from flojoy import flojoy, Boolean

@flojoy
def EXCLUSIVE_OR(default: Boolean, a: Boolean) -> Boolean:
    """The EXCLUSIVE_OR node takes two boolean data type and computs logical EXCLUSIVE OR operation on them.

    Inputs
    ------
    default : Boolean
        The input boolean to which we apply the EXCLUSIVE OR operation.

    a : Boolean
        The input boolean to which we apply the EXCLUSIVE OR operation.

    Returns
    -------
    Boolean
        The boolean result from the operation of the inputs.
    """
    if (default.b and not a.b) or (not default.b and a.b):
        return Boolean(b=True)
    return Boolean(b=False)