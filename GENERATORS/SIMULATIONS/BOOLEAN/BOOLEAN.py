from flojoy import flojoy, Boolean


@flojoy
def BOOLEAN(status: bool=True) -> Boolean:
    """The MATRIX node takes two arguments, 'row' and 'col', as input.

    Based on these inputs, it generates a random matrix where the integers inside the matrix are between 0 and 19.

    Parameters
    ----------
    status : True
        either True or False value that you want to assign

    Returns
    -------
    Boolean
        Boolean node
    """

    return Boolean(b=status)
