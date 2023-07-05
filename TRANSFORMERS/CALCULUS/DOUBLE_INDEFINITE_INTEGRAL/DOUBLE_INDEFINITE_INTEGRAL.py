from flojoy import flojoy, Matrix, OrderedTriple, DefaultParams
import numpy as np


@flojoy
def DOUBLE_INDEFINITE_INTEGRAL(
    default : OrderedTriple, params: DefaultParams
) -> Matrix:
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

    input_x = default.x
    input_y = default.y
    input_z = default.z

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

    return Matrix(m=result)
