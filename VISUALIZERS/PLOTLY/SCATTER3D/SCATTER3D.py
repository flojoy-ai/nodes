from flojoy import OrderedTriple, DataFrame, flojoy


@flojoy(node_type="SCATTER3D", forward_result=True)
def SCATTER3D(default: OrderedTriple | DataFrame) -> OrderedTriple:
    """The SCATTER3D node creates a Plotly 3D Scatter visualization for a given input DataContainer.

    Inputs
    ------
    default : OrderedTriple|DataFrame
        the DataContainer to be visualized

    Returns
    -------
    Plotly
        the DataContainer containing the Plotly 3D Scatter visualization
    """

    match default:
        case OrderedTriple():
            return default
        case DataFrame():
            df = default.m
            if len(df.columns) < 3:
                raise ValueError(
                    "DataFrame must have at least 3 columns for x, y, and z coordinates."
                )

            x = df.columns[0].to_numpy()
            y = df.columns[1].to_numpy()
            z = df.columns[2].to_numpy()

            return OrderedTriple(x=x, y=y, z=z)
