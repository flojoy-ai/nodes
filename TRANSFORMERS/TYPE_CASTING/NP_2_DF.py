import pandas as pd
from flojoy import flojoy, DataContainer


@flojoy
def NP_2_DF(dc_input: DataContainer) -> DataContainer:
    """
    Node to convert matrix type data into dataframe type data
    """
    if dc_input.type == "matrix":
        matrixToArray = dc_input.flatten()
        df = pd.DataFrame(matrixToArray)
        
        return DataContainer()
    else:
        print("Invalid type of DataContainer")
