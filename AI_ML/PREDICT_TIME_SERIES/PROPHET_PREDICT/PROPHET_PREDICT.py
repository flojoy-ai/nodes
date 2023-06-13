import pandas as pd
from flojoy import flojoy, DataContainer
from typing import Any, Dict, List
from prophet import Prophet
from prophet.serialize import model_to_json


@flojoy
def PROPHET_PREDICT(
    dc_inputs: List[DataContainer], params: Dict[str, Any]
) -> DataContainer:
    dc_input = dc_inputs[0]
    run_forcast = params["run_forecast"]
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
            extra = {"prophet": model_to_json(model)}

            if run_forcast:
                future = model.make_future_dataframe(periods=params["periods"])
                forecast = model.predict(future)
                extra["forecast"] = forecast
            return DataContainer(
                type="dataframe",
                m=df,
                extra=extra,
            )
        case _:
            raise ValueError(
                f"unsupported DataContainer type passed to PROPHET_PREDICT: {dc_input.type}"
            )
