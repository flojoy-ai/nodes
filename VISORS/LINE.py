from flojoy import JobResultBuilder, flojoy, DataContainer
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


@flojoy
def LINE(v, params):
    return JobResultBuilder().from_inputs(v).to_plot(plot_type='line')
