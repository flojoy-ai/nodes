from flojoy import flojoy, DataContainer, DefaultParams
import plotly.graph_objects as go
import numpy as np
CELL_SIZE = 50
FONT_SIZE = 10
MAX_ALLOWED_SHAPE = 8
v_dot = '$\\vdots$'
d_dot = '$\\ddots$'
l_dot = '$\\ldots$'

def numpy_2d_array_as_table(arr: np.ndarray, arr_row_shape: int, arr_col_shape: int, placeholder: str):
    new_arr = arr
    if arr_row_shape > MAX_ALLOWED_SHAPE or arr_col_shape > MAX_ALLOWED_SHAPE:
        new_arr = np.full((MAX_ALLOWED_SHAPE, MAX_ALLOWED_SHAPE), placeholder, dtype=object)
        new_arr[:-2, :-2] = arr[:MAX_ALLOWED_SHAPE - 2, :MAX_ALLOWED_SHAPE - 2]
        last_row = arr[arr_row_shape - 1, :]
        first_cols = last_row[:MAX_ALLOWED_SHAPE - 2]
        new_arr[MAX_ALLOWED_SHAPE - 1, :MAX_ALLOWED_SHAPE - 2] = first_cols
        last_col = arr[:, arr.shape[1] - 1]
        first_rows = last_col[:MAX_ALLOWED_SHAPE - 2]
        new_arr[:MAX_ALLOWED_SHAPE - 2, MAX_ALLOWED_SHAPE - 1] = first_rows
        new_arr[MAX_ALLOWED_SHAPE - 1, MAX_ALLOWED_SHAPE - 1:] = arr[arr_row_shape - 1, arr.shape[1] - 1:]
        new_arr[0, MAX_ALLOWED_SHAPE - 2] = l_dot
        new_arr[MAX_ALLOWED_SHAPE - 1, MAX_ALLOWED_SHAPE - 2] = l_dot
        new_arr[MAX_ALLOWED_SHAPE - 2, 0] = v_dot
        new_arr[MAX_ALLOWED_SHAPE - 2, MAX_ALLOWED_SHAPE - 1] = v_dot
    else:
        new_arr
    return new_arr.T

def numpy_1d_array_as_table(arr: np.ndarray, placeholder: str):
    if arr.size > MAX_ALLOWED_SHAPE:
        converted_type = arr.astype(object)
        new_arr = converted_type[:MAX_ALLOWED_SHAPE]
        new_arr[MAX_ALLOWED_SHAPE - 2] = l_dot
    else:
        new_arr = arr
    return new_arr.reshape(-1, 1)

def numpy_array_as_table(arr: np.ndarray):
    ndim = arr.ndim
    if ndim == 1:
        cell_values = numpy_1d_array_as_table(arr, l_dot)
    elif ndim > 2:
        raise ValueError('MATRIX_VIEW can process only 2D arrays!')
    else:
        (row_shape, col_shape) = arr.shape
        cell_values = numpy_2d_array_as_table(arr, row_shape, col_shape, d_dot)
    return cell_values

@flojoy
def MATRIX_VIEW(default: DataContainer, default_parmas: DefaultParams) -> DataContainer:
    """
    The MATRIX_VIEW node "matrix" or "ordered_pair" type as input type and displays its visualization
    using plotly table in matrix format.

    Parameters
    ----------
    None

    Returns
    -------
    plotly
        Visualization of the input data in matrix format
    """
    dc_input = dc_inputs[0]
    match dc_input.type:
        case 'matrix':
            np_arr = dc_input.m
            cell_values = numpy_array_as_table(np_arr)
        case 'ordered_pair':
            np_arr = dc_input.y
            cell_values = numpy_array_as_table(np_arr)
        case _:
            raise ValueError(f'unsupported DataContainer type passed for MATRIX_VIEW: {dc_input.type}')
    fig = go.Figure(data=[go.Table(header=dict(line={'width': 0}, values=[]), cells=dict(values=cell_values, line={'width': 3}, font={'size': FONT_SIZE}, height=CELL_SIZE, align='center', format=['.3']))])
    width = MAX_ALLOWED_SHAPE * CELL_SIZE + 80
    height = width + 80
    fig.layout = go.Layout(autosize=False, width=width, height=height, margin=dict(l=0, r=0, t=0, b=0), xaxis=dict(visible=False), yaxis=dict(visible=False), hovermode='closest', font=dict(size=FONT_SIZE))
    return DataContainer(type='plotly', fig=fig)