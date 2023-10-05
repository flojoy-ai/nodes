from typing import Literal

from flojoy import DataFrame, flojoy
from sklearn.datasets import load_iris


@flojoy()
def SCIKIT_LEARN_DATASET(dataset_name: Literal["iris"] = "iris") -> DataFrame:
    """The SCIKIT_LEARN_DATASET node retrieves a pandas DataFrame from 'sklearn.datasets', using the provided dataset_key parameter, and returns it wrapped in a DataContainer.

    Parameters
    ----------
    dataset_name : str

    Returns
    -------
    DataFrame
        A DataContainer object containing the retrieved pandas DataFrame.
    """

    if dataset_name == "iris":
        iris = load_iris(as_frame=True)
        return DataFrame(m=iris)  # type: ignore

    else:
        raise ValueError(f"Failed to retrieve '{dataset_name}' from rdatasets package!")
