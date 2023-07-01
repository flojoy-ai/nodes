from flojoy import flojoy, DataContainer, DefaultParams
import numpy as np


@flojoy
def DOUBLE_INDEFINITE_INTEGRAL(
    default: DataContainer, default_params: DefaultParams
) -> DataContainer:
    """
    The INDEFINITE_INTEGRAL node takes three matrices and computes double integral.
    It returns a matrix where each cell represents volumn up to the given point.

    Parameters
    ----------
    None

    Returns
    -------
    DataContainer:
        type 'matrix', m
    """
    dc_input = dc_inputs[0]
    input_x = dc_input.x
    input_y = dc_input.y
    input_z = dc_input.z
    integrate = np.zeros_like(input_x)
    for i in range(1, len(input_x)):
        for j in range(1, len(input_y)):
            cal = (
                (input_x[i][j] - input_x[i][j - 1])
                * (input_y[i][j] - input_y[i - 1][j])
                / 4
            )
            result = cal * (
                input_z[i - 1][j - 1]
                + input_z[i][j - 1]
                + input_z[i - 1][j]
                + input_z[i][j]
            )
            integrate[i][j] = result
    result = np.copy(integrate)
    for i in range(len(integrate)):
        for j in range(1, len(integrate)):
            if i == 0:
                result[i][j] = result[i][j - 1] + result[i][j]
            elif j == 1:
                result[i][j] = result[i - 1][j] + result[i][j]
            else:
                result[i][j] = (
                    result[i][j - 1]
                    + result[i - 1][j]
                    + result[i][j]
                    - result[i - 1][j - 1]
                )
    return DataContainer(type="matrix", m=result)
