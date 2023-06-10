import numpy as np
import pandas as pd
from flojoy import flojoy, DataContainer
from typing import Any, Dict, List
import plotly.express as px


@flojoy
def PROPHET(dc: List[DataContainer], params: Dict[str, Any]) -> DataContainer:
    try:
        from prophet import Prophet
        from prophet.plot import plot_plotly
        # FIXME: We shouldn't need this if we can get the normal line-chart working.
        #  for now, we need to use px.imshow to render on flojoy.
        #  see https://github.com/flojoy-io/nodes/issues/96
        import imageio
    except ImportError:
        # raise Exception("You must install Prophet for this node")
        raise Exception("You must install Prophet and imageio for this node")

    ts = dc[0].x
    y = dc[0].y
    df = pd.DataFrame(dict(ds=ts, y=y))
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=params["periods"])
    forecast = model.predict(future)
    fig = plot_plotly(model, forecast)

    # FIXME: Again, see above. None of this should be necessary. We should be able
    #  to use the line directly from `fig` above. But this makes the demo work
    file_path = "/tmp/img.jpg"
    fig.write_image(file_path)
    image = imageio.v2.imread(file_path)
    fig = px.imshow(image)

    return DataContainer(
        type='plotly',
        fig=fig
    )
