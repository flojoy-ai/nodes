from flojoy import flojoy, DataContainer
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from typing import cast


@flojoy
def SUPPORT_VECTOR_MACHINE(
    dc_inputs: list[DataContainer], params: dict
) -> DataContainer:
    """
    Parameters
    ----------
    kernel: 'linear' | 'poly' | 'rvm', default='linear'

    Returns
    -------
    dataframe
        The predictions for the input data.
    """

    # Should input training dataset and data to classify

    x = dc_inputs[0]
    y = dc_inputs[1]
    input_data = dc_inputs[2]

    X, Y = cast_np_array(x), cast_np_array(y)
    data = cast_np_array(input_data)

    kernel = params.get("kernel", "linear")

    clf = svm.SVC(kernel=kernel)
    prediction = clf.predict(input_data)

    output = pd.DataFrame(data)
    return DataContainer(type="dataframe", m=output)


def cast_np_array(dc: DataContainer) -> np.ndarray:
    if dc.type == "dataframe":
        return cast(pd.DataFrame, dc.m).to_numpy()
    elif dc.type == "matrix":
        return cast(np.ndarray, dc.m)
    else:
        raise ValueError(
            f"unsupported DataContainer type passed to SUPPORT_VECTOR_MACHINE node: {x.type}"
        )
