from flojoy import flojoy, DataContainer
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


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
    #
    #
    #

    X = []
    Y = []

    kernel = params.get("kernel", "linear")

    clf = svm.SVC(kernel=kernel)

    output = pd.DataFrame([])
    return DataContainer(type="dataframe", m=output)
