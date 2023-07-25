from flojoy import flojoy, DataFrame as FlojoyDataframe
from typing import Literal
from sklearn import datasets


DATASETS_MAP = {
    "Iris": datasets.load_iris,
    "Diabetes": datasets.load_diabetes,
    "Digits": datasets.load_digits,
    "Wine": datasets.load_wine,
    "Linnerud": datasets.load_linnerud,
    "Breast Cancer": datasets.load_breast_cancer
}


@flojoy
def TABULAR_DATASETS(
    dataset: Literal["Iris", "Diabetes", "Digits", "Wine", "Linnerud", "Breast Cancer"] = "Iris"
) -> FlojoyDataframe:
    """
    The TABULAR_DATASETS node loads a tabular dataset from sklearn.datasets.

    Parameters
    ----------
    dataset: str, default="Iris"
        The name of the dataset to load. Options are: "Iris", "Diabetes", "Digits", "Wine", "Linnerud", "Breast Cancer".

    Returns
    -------
    dataframe: FlojoyDataframe
        The original dataframe for the input data.
    """
    
    load_method = DATASETS_MAP[dataset]
    data = load_method(as_frame=True).frame

    return FlojoyDataframe(df=data)

    
