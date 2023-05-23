from flojoy import flojoy, DataContainer
import plotly.graph_objects as go
from plotly.graph_objects import Data
import numpy as np


@flojoy
def MATRIX_VIEW(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    """Node creates a Plotly table visualization for a given input data container.

    Args:
    dc_inputs (list): A list of DataContainer object(s) containing the input data.
    params (dict): A dictionary containing the parameters needed for the visualization.

    Returns:
    DataContainer: A DataContainer object containing the generated visualization and the processed data.

    Raises:
    ValueError: If the input data container is not supported.
    """
    dc_input: DataContainer = dc_inputs[0]
    if dc_input.type:
        # Generate random matrix data
        matrix_data = np.asarray(
            [[0, 1, 2, 3,5, 6], [4, 5, 6, 7,5, 6], [8, 9, 10, 11,5, 6], [12, 13, 14, 15,5, 6], [8, 9, 10, 11,5, 6], [12, 13, 14, 15,5, 6]]
        )

        # Create a Heatmap object
        # heatmap = go.Heatmap(z=matrix_data)
        # Create a table
        # trace1 ={
        #         "type": "table",
        #         "cells": {
        #           "fill": {"color": "rgb(255, 255, 255)"},
        #           "font": {
        #             "size": 10,
        #             "color": "rgb(0, 0, 0)",
        #             "family": "Overpass"
        #           },
        #           "line": {
        #             "color": "rgb(0, 0, 0)",
        #             "width": 2
        #           },
        #           "align": "center",
        #           "height": 33,
        #           "valuessrc": "jackp:18888:f2fba1,6a904e,27fb62,937cff*",
        #           "values": [
        #             ["1.2e6", "342", "$\vdots$", "-3.3e-9"],
        #             ["4", "5", "$\ddots$", "$\ldots$"],
        #             ["$\ldots$", "$\ddots$", "10", "11"],
        #             ["12", "$\vdots$", "14", "15" ]
        #           ],
        #         },
        #         # "header": {
        #         #   "fill": {"color": "rgb(255, 255, 255)"},
        #         #   "font": {"size": 12},
        #         #   "align": "left",
        #         #   "values": "~:-100:~1000,~1001,~1002,~1003*"
        #         # },
        #         "hoverlabel": {"align": "left"}
        #     }

        # data = Data([trace1])
        table = go.Table(
            columnorder=[0, 1, 2, 3],
            columnwidth=40,
            cells=dict(
                values=matrix_data, fill=dict(color="lavender"), align="left", height=40
            ),
        )
        layout = go.Layout(
            autosize=False,
            width=500,
            height=500,
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            hovermode="closest",
        )

        # Create a Figure object and add the Heatmap
        fig = go.Figure(data=table, layout=layout)
        # m:np.ndarray = dc_input.m
        # fig = go.Figure(
        #     data=[
        #         go.Table(
        #             # header=dict(values=list(m.columns), align="left"),
        #             cells=dict(values=[m[col] for col in m.columns], align="left"),
        #         )
        #     ]
        # )
        return DataContainer(type="plotly", fig=fig)
    else:
        raise ValueError(
            f"unsupported DataContainer type passed for MATRIX_VIEW: {dc_input.type}"
        )
