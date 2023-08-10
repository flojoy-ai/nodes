from flojoy import flojoy, DataFrame, OrderedTriple


@flojoy
def DF_2_ORDEREDTRIPLE(
    default: DataFrame, x: int = 0, y: int = 1, z: int = 2
) -> OrderedTriple:
    """
    The DF_2_ORDEREDTRIPLE node converts a dataframe type data into an OrderedTriple type data.

    It takes one dataframe type data and selects 3 different columns to generate the OrderedTriple type.

    Parameters
    ----------
    x : the index of the column that represents the x axis
    y : the index of the column that represents the y axis
    z : the index of the column that represents the z axis

    Returns
    -------
    OrderedTriple
    """

    df = default.m
    if df.shape[1] < 3:
        raise AssertionError(
            f"The DataFrame needs to have a shape greater than 2 in order to be converted to the OrderedTriple type, got: {df.shape[1]}"
        )

    x_list = df.iloc[:, x]
    y_list = df.iloc[:, y]
    z_list = df.iloc[:, z]

    x_numpy = x_list.to_numpy(dtype=object)
    y_numpy = y_list.to_numpy(dtype=object)
    z_numpy = z_list.to_numpy(dtype=object)

    return OrderedTriple(x=x_numpy, y=y_numpy, z=z_numpy)
