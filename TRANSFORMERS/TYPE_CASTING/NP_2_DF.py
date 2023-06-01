import pandas as pd
from flojoy import flojoy, DataContainer


@flojoy
def NP_2_DF(dc_input: DataContainer):
    if dc_input.type == "matrix":
        matrixToArray = dc_input.flatten()
        df = pd.DataFrame(matrixToArray)
        dc_input.set_data(df)
