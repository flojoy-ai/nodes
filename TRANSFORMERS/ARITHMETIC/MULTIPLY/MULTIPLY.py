import numpy as np
from flojoy import flojoy, DataContainer


@flojoy
def MULTIPLY(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """The MULTIPLY node multiplies the values from the two inputs.
    The node can handle scalar and ordered pair inputs currently

    TODO - reconcile.py so matrix and dataframe types can be handled.

    Parameters
    ----------
    None

    Returns:
    --------
    DataContainer:
        type 'ordered pair' if one 'ordered pair' is input.

        type 'scalar' if two 'scalars' are input.
    """

    if len(dc_inputs) < 2:
        raise ValueError(
            f"To multiply the values, MULTIPLY node requires two inputs, {len(dc_inputs)} was given!"
        )
    match [dc_inputs[0].type, dc_inputs[1].type]:
        case ["scalar", "ordered_pair"]:
            raise ValueError(
                "The 'scalar' type should be connect to the 'y' input."
            )

        case ["ordered_pair", "ordered_pair"]:
            a = dc_inputs[0].y
            b = dc_inputs[1].y

            x = dc_inputs[0].x
            y = np.multiply(a, b)

            return DataContainer(x=x, y=y)

        case ["ordered_pair", "scalar"]:
            a = dc_inputs[0].y
            b = dc_inputs[1].c

            x = dc_inputs[0].x
            y = np.multiply(a, b)

            return DataContainer(x=x, y=y)

        case ["scalar", "scalar"]:
            a = dc_inputs[0].c
            b = dc_inputs[1].c

            c = np.multiply(a, b)

            return DataContainer(type="scalar", c=c)

