import pytest
from sklearn.datasets import fetch_kddcup99
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from flojoy import DataFrame as FlojoyDataFrame


def test_ADD(mock_flojoy_decorator):
    import ISOLATION_FOREST


    X, y = fetch_kddcup99(random_state=42, percent10=True, as_frame=True, return_X_y=True)
    df = pd.concat([X, y], axis=1)

    # Get only http service
    df = df[df["service"] == b"http"]
    df = df.drop("service", axis=1)
    
    encs = dict()
    data = df.copy()
    for c in data.columns:
        if data[c].dtype != 'object':
            continue
        encs[c] = LabelEncoder()
        data[c] = encs[c].fit_transform(data[c])


    X, y = data.drop("labels", axis=1), data["labels"]
    X = FlojoyDataFrame(df=X)
    results = ISOLATION_FOREST.ISOLATION_FOREST(X, contamination=0.1)


    assert 'anomaly_scores' in results.m.columns
    assert 'anomaly' in results.m.columns




