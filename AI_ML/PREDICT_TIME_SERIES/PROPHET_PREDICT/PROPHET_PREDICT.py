import pandas as pd
from flojoy import flojoy, DataContainer
from typing import Any, Dict, List
from prophet import Prophet
from prophet.serialize import model_to_json


@flojoy
def PROPHET_PREDICT(
    dc_inputs: List[DataContainer], params: Dict[str, Any]
) -> DataContainer:
    """Trains a Prophet model on the incoming dataframe, optionally running a forecast

    The DataContainer input type must be `dataframe`, and that dataframe must have its
    first column (or index) be of datetime type.

    This node always returns a DataContainer of type 'dataframe'. It will also
    always return an `extra` field with a key `prophet` whose value is the JSONified
    Prophet model, which can be loaded as follows:
        ```python
        from prophet.serialize import model_from_json

        model = model_from_json(dc_inputs.extra["prophet"])
        ```
    If the `run_forecast` param is True (default case), the returning DataContainer
    will have it's dataframe (`m` parameter of the DataContainer) be the forecast
    dataframe. It will also have an `extra` field with the key "original" which is
    the original dataframe.

    If `run_forecast` is false, the returning dataframe will be the original data
    """
    dc_input = dc_inputs[0]
    run_forecast = params["run_forecast"]
    match dc_input.type:
        case "dataframe":
            df: pd.DataFrame = dc_input.m
            first_col = df.iloc[:, 0]
            if not pd.api.types.is_datetime64_any_dtype(first_col):
                raise ValueError(
                    "First column must be of datetime type data for PROPHET_PREDICT!"
                )
            df.rename(
                columns={df.columns[0]: "ds", df.columns[1]: "y"}, inplace=True
            )  # PROPHET model expects first column to be `ds` and second to be `y`
            model = Prophet()
            model.fit(df)
            extra = {"prophet": model_to_json(model), "run_forecast": run_forecast}
            # If run_forecast, the return df is the forecast, otherwise the original
            return_df = df.copy()
            if run_forecast:
                future = model.make_future_dataframe(periods=params["periods"])
                forecast = model.predict(future)
                extra["original"] = df
                return_df = forecast
            return DataContainer(
                type="dataframe",
                m=return_df,
                extra=extra,
            )
        case _:
            raise ValueError(
                f"unsupported DataContainer type passed to PROPHET_PREDICT: {dc_input.type}"
            )
