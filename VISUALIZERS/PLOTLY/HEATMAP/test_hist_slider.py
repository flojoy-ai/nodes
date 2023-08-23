import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Generate example data
data = 255*np.random.rand(512, 512)


fig = make_subplots(rows=1, cols=2, column_widths=[0.95, 0.05],specs = [[{}, {}]],
                          horizontal_spacing = 0.05)

fig.add_trace(
    go.Heatmap(
        z=data
    ), 
    row=1, 
    col=1
)

# # Calculate histogram data
histogram = np.histogram(data, bins='auto')
x_values = histogram[1][:-1] + 0.05  # Center bars on bin edges

# # Add histogram with shading
histogram_trace = go.Bar(
    x=x_values,
    y=histogram[0],
    orientation='h',
    showlegend=False
)
fig.add_trace(histogram_trace, row=1, col=2)

fig.update_layout(
    sliders=[
        {
            "steps": [
                {"label": str(v), "method": "restyle", "args": [{"zmin": 0, "zmax": v}]}
                for v in range(1, 255, 1)
            ],
            "name" : "zmax"
        },
    ]
)

fig.show()
