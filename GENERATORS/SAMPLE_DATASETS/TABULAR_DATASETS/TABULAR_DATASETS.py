from flojoy import flojoy, DataFrame as FlojoyDataframe, run_in_venv
from typing import Literal
from sklearn.datasets import (
    load_iris, 
    load_diabetes, 
    load_digits, 
    load_wine, 
    load_linnerud, 
    load_breast_cancer
)


DATASETS_MAP = {
    "Iris": load_iris,
    "Diabetes": load_diabetes,
    "Digits": load_digits,
    "Wine": load_wine,
    "Linnerud": load_linnerud,
    "Breast Cancer": load_breast_cancer
}


@flojoy
def TABULAR_DATASETS(
    dataset: Literal["Iris", "Diabetes", "Digits", "Wine", "Linnerud", "Breast Cancer"] = "Iris"
) -> FlojoyDataframe:
    
    load_method = DATASETS_MAP[dataset]
    data = load_method(as_frame=True).frame

    df = FlojoyDataframe(df=data)
    return df

    
