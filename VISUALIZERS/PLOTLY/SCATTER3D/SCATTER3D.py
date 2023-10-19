from flojoy import DataContainer, Vector, OrderedTriple, DataFrame, flojoy
import numpy as np


@flojoy(node_type="SCATTER3D", forward_result=True)
def SCATTER3D(
    default: OrderedTriple | DataFrame | Vector,
    point_size: int = 4,
    show_xy_plane: bool = False,
    show_xz_plane: bool = True,
    show_yz_plane: bool = False,
    x_min: float = -10,
    x_max: float = 10,
    x_step: float = 1,
    y_min: float = 0,
    y_max: float = 10,
    y_step: float = 1,
    z_min: float = -10,
    z_max: float = 10,
    z_step: float = 1,
) -> DataContainer:
    """The SCATTER3D node creates a Plotly 3D Scatter visualization for a given input DataContainer.

    Inputs
    ------
    default : OrderedTriple|DataFrame|Vector
        the DataContainer to be visualized

    Returns
    -------
    Plotly
        the DataContainer containing the Plotly 3D Scatter visualization
    """

    match default:
        case Vector():
            return default
        case OrderedTriple():
            x = default.x
            y = default.y
            z = default.z
        case DataFrame():
            df = default.m
            if len(df.columns) < 3:
                raise ValueError(
                    "DataFrame must have at least 3 columns for x, y, and z coordinates."
                )

            x = df.columns[0].to_numpy()
            y = df.columns[1].to_numpy()
            z = df.columns[2].to_numpy()

    return Vector(v=np.column_stack((x, y, z)), extra=default.extra)
