from flojoy import flojoy, DataContainer
import pandas as pd
import numpy as np
from sklearn import svm, preprocessing
from typing import cast


@flojoy
def SUPPORT_VECTOR_MACHINE(
    dc_inputs: list[DataContainer], params: dict
) -> DataContainer:
    """The SUPPORT_VECTOR_MACHINE node is used to train a support vector machine model for classification tasks.

    Parameters
    ----------
    target: str, optional
        The column name of the label in the input dataframe.
    kernel: 'linear' | 'poly' | 'rvm' | 'sigmoid', default='linear'
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

    training_data = dc_inputs[0]
    input_data = dc_inputs[1]

    if training_data.type != "dataframe" and training_data.type != "matrix":
        raise ValueError(
            f"unsupported DataContainer type passed to SUPPORT_VECTOR_MACHINE node for train: {training_data.type}"
        )

    if input_data.type != "dataframe" and input_data.type != "matrix":
        raise ValueError(
            f"unsupported DataContainer type passed to SUPPORT_VECTOR_MACHINE node for input: {input_data.type}"
        )

    target: str = params["target"]
    kernel: str = params.get("kernel", "linear")

    le = preprocessing.LabelEncoder()

    if training_data.type == "dataframe":
        df = cast(pd.DataFrame, training_data.m)
        if not target:
            target = str(df.columns[-1])

        col = df[target]
        train = cast(pd.DataFrame, df.drop(target, axis=1)).to_numpy()
    # Other case is matrix
    else:
        # assume the last column is the label
        data = cast(np.ndarray, training_data.m)
        col = data[:, -1]

        # remove the last column
        train = np.delete(data, -1, axis=1)

    X = train
    Y = le.fit_transform(col)

    clf = svm.SVC(kernel=kernel)
    clf.fit(X, Y)

    prediction = clf.predict(input_data.m)
    prediction = le.inverse_transform(prediction)
    prediction = pd.DataFrame({target: prediction})

    return DataContainer(type="dataframe", m=prediction)
