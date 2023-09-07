import numpy as np
from flojoy import flojoy, OrderedPair, Matrix, DataFrame, Vector, Scalar


@flojoy
def APPEND(
    primary_dp: OrderedPair | Matrix | DataFrame | Scalar | Vector,
    secondary_dp: OrderedPair | Matrix | DataFrame | Scalar | Vector,
) -> OrderedPair | Matrix | DataFrame | Vector:
    """The APPEND node appends a single data point to an array.

    The large array must be passed to the bottom "array" connection.

    For ordered pair, the single point must have a shape of 1 (or (1,)).

    Inputs
    ------
    primary_dp : OrderedPair|Vector|Scalar|Matrix|DataFrame
        Input that ends up "on top" of the resulting DataContainer.
    secondary_dp : OrderedPair|Vector|Scalar|Matrix|DataFrame
        Input that ends up "on the bottom" of the resulting DataContainer.

    Returns
    -------
    OrderedPair, Matrix, DataFrame, Vector
    """

    if isinstance(primary_dp, OrderedPair) and isinstance(secondary_dp, OrderedPair):
        x0 = primary_dp.x
        y0 = primary_dp.y

        x1 = secondary_dp.x
        y1 = secondary_dp.y

        if y1.shape[0] != 1:
            raise ValueError(
                (
                    "To append, APPEND node the requires the non-array "
                    "input to have a single point. "
                    f"The data passed has a shape of: {y1.shape}"
                )
            )

        x = np.append(x0, x1)
        y = np.append(y0, y1)
        return OrderedPair(x=x, y=y)

    elif isinstance(primary_dp, Matrix) and isinstance(secondary_dp, Matrix):
        m0 = primary_dp.m
        m1 = secondary_dp.m

        m = np.append(m0, m1, axis=0)
        return Matrix(m=m)

    elif isinstance(primary_dp, Vector) and isinstance(secondary_dp, Vector):
        v0 = primary_dp.v
        v1 = secondary_dp.v

        v = np.append(v0, v1, axis=0)
        return Vector(v=v)

    elif isinstance(primary_dp, Vector) and isinstance(secondary_dp, Scalar):
        v0 = primary_dp.v
        v1 = secondary_dp.c

        v = np.append(v0, [v1], axis=0)
        return Vector(v=v)

    elif isinstance(primary_dp, Scalar) and isinstance(secondary_dp, Scalar):
        c0 = primary_dp.c
        c1 = secondary_dp.c

        v = np.append([c0], [c1], axis=0)
        return Vector(v=v)

    else:
        df0 = primary_dp.m
        df1 = secondary_dp.m

        df = np.append(df0, df1, axis=0)
        return DataFrame(df=df)
