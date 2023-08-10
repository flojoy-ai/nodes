from flojoy import flojoy, OrderedTriple, Matrix
import numpy as np


def contains_only_numbers(column, colName):
    for i in range(0, len(column)):
        if not isinstance(column.item(i), (int, float)):
            raise ValueError(
                f"The value {column.item(i)} in column {colName} is of type {type(column.item(i))}. The OrderedTriple need to contain only int or float values."
            )


@flojoy
def DOUBLE_INDEFINITE_INTEGRAL(
    default: OrderedTriple, width: int = 3, height: int = 3
) -> Matrix:
    """
    The DOUBLE_INDEFINITE_INTEGRAL node takes an OrderedTriple (x,y,z) and have the width and height parameter.
    The width and height respectively represent the number of columns and rows that the x, y and z reshape matrices will have.
    Here it's important to note that the length of x, y and z is the same and that the width times the height need to be equal to the length of x, y and z.
    It computes the double integral approximation according to the matrices dimensions given and it returns a matrix where each cell represents volume up to the given point.

    Parameters
    ----------
    width: int
        Number of columns of the 3 matrices generate by reshaping the x, y and z columns of the OrderedTriple.
    height: int
        Number of rows of the 3 matrices generate by reshaping the x, y and z columns of the OrderedTriple.

    Returns
    -------
    m: Matrix
        matrix containing in each cell the volume up to that point.
    """

    if np.divide(len(default.x), width) == height:
        contains_only_numbers(default.x, "x")
        contains_only_numbers(default.y, "y")
        contains_only_numbers(default.z, "z")

        input_x = np.reshape(default.x, (height, width))
        input_y = np.reshape(default.y, (height, width))
        input_z = np.reshape(default.z, (height, width))
    else:
        raise ArithmeticError(
            f"Cannot reshape size {len(default.x)} in a matrix of {width} by {height}. Please enter appropriate width and height."
        )

    integrate = np.zeros_like(input_x)

    for i in range(1, len(input_x)):
        for j in range(1, width):
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

    for i in range(1, len(integrate)):
        for j in range(1, width):
            if i == 1:
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
