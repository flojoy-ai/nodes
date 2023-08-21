from flojoy import Plotly, OrderedPair, flojoy, Matrix, DataFrame, Vector, OrderedTriple
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from nodes.VISUALIZERS.template import plot_layout


@flojoy
def HEATMAP(default: OrderedPair | Matrix | DataFrame | Vector | OrderedTriple, show_text: bool = False) -> Plotly:
    layout = plot_layout(title="HEATMAP")
    match default:
      case Vector():
        y = default.v
        if y.ndim < 2:
            num_columns = len(y) // 2
            y = np.reshape(y, (2, num_columns))
        fig = go.Figure(data=[go.Heatmap(z=y, text=y if show_text else None)])
        
      case OrderedPair():
        y = default.y
        if default.y.ndim < 2:
            num_columns = len(default.y) // 2
            y = np.reshape(default.y, (2, num_columns))
        fig = go.Figure(data=[go.Heatmap(z=y, text=y if show_text else None)])
      case OrderedTriple():
            x = np.unique(default.x)
            y = np.unique(default.y)
            z_size = len(x) * len(y)
            if z_size > len(default.z):
                z = np.pad(
                    default.z, (0, z_size - len(default.z)), mode="constant"
                ).reshape(len(y), len(x))
            else:
                z = default.z[:z_size].reshape(len(y), len(x))
            if z.ndim < 2:
                num_columns = len(z) // 2
                z = np.reshape(z, (2, num_columns))
            fig = go.Figure(data=[go.Heatmap(z=z, text=z if show_text else None, texttemplate="%{text}",)])
      case Matrix():
        m = default.m
        if m.ndim < 2:
            num_columns = len(m) // 2
            m = np.reshape(m, (2, num_columns))
        fig = go.Figure(data=[go.Heatmap(z=m)])
      case DataFrame():
        df = default.m
        fig = px.imshow(df, text_auto=show_text)
    
    fig = fig.update_layout(
      layout
    )
    return Plotly(
        fig = fig,
    )
