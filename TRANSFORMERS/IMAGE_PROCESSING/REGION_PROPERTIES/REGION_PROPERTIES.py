from skimage.draw import ellipse
from skimage.measure import label, regionprops, regionprops_table
from skimage.transform import rotate
from flojoy import flojoy, Plotly, run_in_venv, Grayscale, Image
import plotly.express as px
import numpy as np
from typing import Optional
import math 
from nodes.VISUALIZERS.template import plot_layout
from PIL import ImageFilter, Image as PILImage

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

    label_img = label(image)
    regions = regionprops(label_img)
    for props in regions:
        y0, x0 = props.centroid
        orientation = props.orientation
        x1 = x0 + math.cos(orientation) * 0.5 * props.axis_minor_length
        y1 = y0 - math.sin(orientation) * 0.5 * props.axis_minor_length
        x2 = x0 - math.sin(orientation) * 0.5 * props.axis_major_length
        y2 = y0 - math.cos(orientation) * 0.5 * props.axis_major_length


    layout = plot_layout(title="IMAGE")
    fig = px.imshow(img=image)
    fig.layout = layout
    
    # ax.plot((x0, x1), (y0, y1), '-r', linewidth=2.5)
    # ax.plot((x0, x2), (y0, y2), '-r', linewidth=2.5)
    # ax.plot(x0, y0, '.g', markersize=15)

    return Plotly(fig=fig)#Image(r=255*image, b=255*image, g=255*image)