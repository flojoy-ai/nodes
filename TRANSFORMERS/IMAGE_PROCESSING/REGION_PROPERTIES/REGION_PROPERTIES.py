from skimage.draw import ellipse
from skimage.measure import label, regionprops, find_contours
from skimage.transform import rotate
from flojoy import flojoy, Plotly, run_in_venv, Image
import plotly.express as px
import plotly.graph_objects as go

import numpy as np
from typing import Optional
import math 
from nodes.VISUALIZERS.template import plot_layout
from PIL import Image as PILImage

@flojoy
@run_in_venv(pip_dependencies=["scikit-image==0.21.0"])
def REGION_PROPERTIES(default: Optional[Image] = None) -> Plotly:

    if default:
        r = default.r
        g = default.g
        b = default.b
        a = default.a

        if a is None:
            image = np.stack((r, g, b), axis=2)
        else:
            image = np.stack((r, g, b, a), axis=2)
        image = PILImage.fromarray(image)
        image = np.array(image.convert("L"))

    else:
        image = np.zeros((600, 600))
        rr, cc = ellipse(300, 350, 100, 220)
        image[rr, cc] = 1
        image = rotate(image, angle=15, order=0)
        rr, cc = ellipse(100, 100, 60, 50)
        image[rr, cc] = 1
        
    rgb_image = np.zeros((600, 600, 3), dtype=np.uint8)
    rgb_image[..., 0] = image * 255  # Red channel
    rgb_image[..., 1] = image * 255  # Green channel
    rgb_image[..., 2] = image * 255  # Blue channel
    layout = plot_layout(title="IMAGE")
    fig = px.imshow(img=rgb_image)
    fig.layout = layout

    labels = label(image)
    rprops = regionprops(labels,image)
    properties = ['area', 'eccentricity', 'perimeter','centroid',
                  'orientation','axis_major_length', 'axis_minor_length']

    for props in rprops:
        y0, x0 = props.centroid
        orientation = props.orientation
        x1 = x0 + math.cos(orientation) * 0.5 * props.axis_minor_length
        y1 = y0 - math.sin(orientation) * 0.5 * props.axis_minor_length
        x2 = x0 - math.sin(orientation) * 0.5 * props.axis_major_length
        y2 = y0 - math.cos(orientation) * 0.5 * props.axis_major_length
    
        line_trace1 = go.Scatter(x=[x0, x1], y=[y0, y1], mode='lines', line=dict(color='red', width=2.5), showlegend=False)
        line_trace2 = go.Scatter(x=[x0, x2], y=[y0, y2], mode='lines', line=dict(color='red', width=2.5), showlegend=False)
        marker_trace = go.Scatter(x=[x0], y=[y0], mode='markers', marker=dict(color='green', size=15), showlegend=False)

        fig.add_trace(line_trace1)
        fig.add_trace(line_trace2)
        fig.add_trace(marker_trace)

        minr, minc, maxr, maxc = props.bbox
        bx = [minc, maxc, maxc, minc, minc]
        by = [minr, minr, maxr, maxr, minr]
        
        bounding_box_trace = go.Scatter(x=bx, y=by, mode='lines', line=dict(color='blue', width=2), showlegend=False)
        fig.add_trace(bounding_box_trace)


    for index in range(labels.max()):
        label_i = rprops[index].label
        contour = find_contours(labels == label_i, 0.5)[0]
        y, x = contour.T
        hoverinfo = ''
        for prop_name in properties:
            val = getattr(rprops[index], prop_name)
            if type(val) == tuple:
                line = [f' <b>{prop_name}_{idv}: {v:.2f}</b>' for idv, v in enumerate(val)]
                hoverinfo += ",".join(line) + "<br>"
            else:
                hoverinfo += f'<b>{prop_name}: {val:.2f}</b><br>'
        fig.add_trace(go.Scatter(
            x=x, y=y, name=label_i,
            mode='lines', fill='toself', showlegend=False,
            hovertemplate=hoverinfo, hoveron='points+fills'))

    fig.update_xaxes(range=[0, 600])
    fig.update_yaxes(range=[0, 600])
    return Plotly(fig=fig)