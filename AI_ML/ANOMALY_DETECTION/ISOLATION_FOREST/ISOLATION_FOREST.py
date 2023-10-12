from flojoy import flojoy, DataFrame as FlojoyDataFrame
from sklearn.ensemble import IsolationForest


@flojoy
def ISOLATION_FOREST(
    default: FlojoyDataFrame, 
    contamination: float = 0
) -> FlojoyDataFrame:
    """
    The ISOLATION_FOREST node uses the Isolation Forest algorithm to detect anomalous points in a tabular dataset.
    Reference: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html

    Parameters
    ----------
    contamination: float, default=0 (auto)
        The estimated proportion of outliers in the data set.

    Returns
    -------
    dataframe
        The original dataframe for the input data including two columns: 'anomaly_scores' and 'anomaly'.
    """
    
    df = default.m
    if contamination == 0:
        contamination = "auto"
    model = IsolationForest(contamination=contamination)
    model.fit(df)
    results = model.decision_function(df)
    df['anomaly'] = model.predict(df)
    df['anomaly_scores'] = results

    return FlojoyDataFrame(df=df)