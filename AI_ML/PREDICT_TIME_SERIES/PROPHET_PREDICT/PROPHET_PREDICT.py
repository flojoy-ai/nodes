import pandas as pd
from flojoy import flojoy, DataFrame
from typing import Any, Dict, List
from prophet import Prophet
from prophet.serialize import model_to_json


@flojoy
def PROPHET_PREDICT(
    default: DataFrame, run_forecast: bool = True, periods: int = 365
) -> DataFrame:
    """The PROPHET_PREDICT node rains a Prophet model on the incoming dataframe

    The DataContainer input type must be `dataframe`, and that dataframe must have its
    first column (or index) be of datetime type.

    This node always returns a DataContainer of type 'dataframe'. It will also
    always return an `extra` field with a key `prophet` whose value is the JSONified
    Prophet model, which can be loaded as follows:
        ```python
        from prophet.serialize import model_from_json

        model = model_from_json(dc_inputs.extra["prophet"])
        ```

    Parameters
    ----------
    run_forecast : bool
        If the True (default case), the returning DataContainer
        will have its dataframe (`m` parameter of the DataContainer) be the forecasted
        dataframe. It will also have an `extra` field with the key "original" which is
        the original dataframe passed in.

        If false, the returning dataframe will be the original data.

        This node will also always have an `extra` field "run_forecast" which matches
        that of the param passed in. This is for future nodes to know if a forecast
        has already been run

        Default True
    periods : int
        The number of periods to predict out. Only used if run_forecast is True.
        Default 365

    Returns
    -------
    DataContainer of type `dataframe` with param `m` which indicates either the original
        df passed in, or the forecasted df (depending on if `run_forecast` is True),
        as well as the `extra` param with keys "run_forecast" which correspond to the
        input param, and potentially "original" in the event that `run_forecast` is True
    """
    dc_input = default
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
                future = model.make_future_dataframe(periods)
                forecast = model.predict(future)
                extra["original"] = df
                return_df = forecast
            return DataFrame(
                type="dataframe",
                df=return_df,
                extra=extra,
            )
        case _:
            raise ValueError(
                f"unsupported DataContainer type passed to PROPHET_PREDICT: {dc_input.type}"
            )
