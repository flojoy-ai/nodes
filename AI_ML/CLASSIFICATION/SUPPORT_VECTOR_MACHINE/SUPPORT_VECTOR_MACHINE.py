from flojoy import flojoy, DataFrame, Matrix
import pandas as pd
import numpy as np
from sklearn import svm, preprocessing
from typing import cast, Literal, Optional


@flojoy
def SUPPORT_VECTOR_MACHINE(
    training_data: DataFrame | Matrix,
    input_data: DataFrame | Matrix,
    target: Optional[str] = None,
    kernel: Literal["linear", "poly", "rvm", "sigmoid"] = "linear",
) -> DataFrame:
    """The SUPPORT_VECTOR_MACHINE node is used to train a support vector machine model for classification tasks.
    It takes a dataframe of labelled training data, and a dataframe of unlabelled input data.

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

    le = preprocessing.LabelEncoder()

    if isinstance(training_data, DataFrame):
        df = training_data.m
        if not target:
            target = str(df.columns[-1])

        col = df[target]
        train = df.drop(target, axis=1).to_numpy()
    # Other case is matrix
    else:
        # assume the last column is the labelxw
        data = training_data.m
        col = data[:, -1]

        # remove the last column
        train = np.delete(data, -1, axis=1)

    X = train
    Y = le.fit_transform(col)

    clf = svm.SVC(kernel=kernel)
    clf.fit(X, Y)

    if isinstance(input_data, DataFrame):
        input_arr = input_data.m.to_numpy()
    else:
        input_arr = input_data.m

    prediction = clf.predict(input_arr)
    prediction = le.inverse_transform(prediction)
    prediction = pd.DataFrame({target: prediction})

    return DataFrame(df=prediction)
