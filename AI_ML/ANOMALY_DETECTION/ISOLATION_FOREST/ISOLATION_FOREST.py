from flojoy import flojoy, DataContainer
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from typing import cast


@flojoy
def ISOLATION_FOREST(
    dc_inputs: list[DataContainer], 
    params: dict
) -> DataContainer:
    """
    The ISOLATION_FOREST node uses the Isolation Forest algorithm to detect anomalous points in a tabular dataset.

    Parameters
    ----------
    contamination: float, default=0.01
        The estimated proportion of outliers in the data set.

    Returns
    -------
    dataframe
        The original dataframe for the input data including two columns: 'anomaly_scores' and 'anomaly'.
    """
    
    data = dc_inputs[0]
    if data.type != "dataframe":
        raise ValueError(
            f"unsupported DataContainer type passed to ISOLATION_FOREST node: {data.type}"
        )
    df = cast(pd.DataFrame, data.m)

    contamination: float = params.get("contamination", 0.01)
    model = IsolationForest(contamination=contamination)
    model.fit(df)
    df['anomaly_scores'] = model.decision_function(df)
    df['anomaly'] = model.predict(df)

    return DataContainer(type="dataframe", m=df)