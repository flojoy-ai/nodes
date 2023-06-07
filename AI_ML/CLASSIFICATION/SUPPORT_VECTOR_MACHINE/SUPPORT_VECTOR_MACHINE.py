from flojoy import flojoy, DataContainer
import pandas as pd
import numpy as np
from sklearn import svm, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from typing import Union, cast


@flojoy
def SUPPORT_VECTOR_MACHINE(
    dc_inputs: list[DataContainer], params: dict
) -> DataContainer:
    """The SUPPORT_VECTOR_MACHINE node is used to train a support vector machine model.

    Parameters
    ----------
    label_col: str
        The column name of the label in the input dataframe.
    kernel: 'linear' | 'poly' | 'rvm', default='linear'
        Specifies the kernel type to be used in the algorithm.

    Returns
    -------
    dataframe
        The predictions for the input data.
    """

    if len(dc_inputs) != 2:
        raise ValueError(
            "SUPPORT_VECTOR_MACHINE requires both training data and input data"
        )

    label_col: Union[str, int] = params.get("label_col")
    if not label_col:
        label_col = -1
    kernel = params.get("kernel", "linear")

    training_data = dc_inputs[0]
    input_data = dc_inputs[1]

    if training_data.type != "dataframe" and training_data.type != "matrix":
        raise ValueError(
            f"unsupported DataContainer type passed to SUPPORT_VECTOR_MACHINE node for train: {training_data.type}"
        )

    if input_data.type != "dataframe" and input_data.type != "matrix":
        raise ValueError(
            f"unsupported DataContainer type passed to SUPPORT_VECTOR_MACHINE node for input: {training_data.type}"
        )

    if training_data.type == "dataframe":
        le = preprocessing.LabelEncoder()
        df = cast(pd.DataFrame, training_data.m)

        if isinstance(label_col, str):
            col = training_data[label_col]
            encoded_labels = le.fit_transform(col)
            train = df.drop(label_col, axis=1).to_numpy()
        else:
            col = training_data.iloc[:, label_col]
            encoded_labels = le.fit_transform(col)
            train = df.drop(df.columns[label_col], axis=1).to_numpy()
    else:
        train = []
        encoded_labels = []

    X = train
    Y = encoded_labels

    clf = svm.SVC(kernel=kernel)
    clf.fit(X, Y)

    prediction = clf.predict(input_data.m)
    prediction = pd.DataFrame(prediction)

    return DataContainer(type="dataframe", m=prediction)
