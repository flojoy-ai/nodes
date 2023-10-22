from flojoy import flojoy, Boolean

@flojoy
def IMPLIES(x: Boolean, y: Boolean) -> Boolean:
    """The IMPLIES node takes two boolean data type and computs logical IMPLIES operation on them.
    x implies y

    Inputs
    ------
    default : Boolean
        The input boolean to which we apply the IMPLIES operation.

    a : Boolean
        The input boolean to which we apply the IMPLIES operation.

    Returns
    -------
    Boolean
        The boolean result from the operation of the inputs.
    """
    if x.b and not y.b:
        return Boolean(b=False)
    return Boolean(b=True)
    