import json
import os
from datetime import datetime
import requests
from flojoy import DataContainer, flojoy
from flojoy.utils import PlotlyJSONEncoder, get_frontier_api_key

FRONTIER_URI: str = (
    os.environ.get("FRONTIER_URI")
    or "https://cipfsgeml2.execute-api.us-east-1.amazonaws.com"
)
MEASUREMENT_API: str = f"{FRONTIER_URI}/measurements"


@flojoy
def LOADER(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    api_key: str | None = get_frontier_api_key()
    measurement_uuid: str = params["measurement_uuid"]

    if api_key is not None and measurement_uuid != "":
        try:
            requests.post(
                f"{MEASUREMENT_API}/{measurement_uuid}",
                json={
                    "api_key": api_key,
                    "measurements": json.dumps(
                        {"data": dc_inputs[0]}, cls=PlotlyJSONEncoder
                    ),
                    "time": datetime.now().__str__(),
                },
            )
        except Exception as e:
            raise e
        return dc_inputs[0]
    else:
        not_found_key = (
            "FRONTIER_API_KEY" if api_key is not None else "Measurement UUID"
        )
        raise KeyError(f"{not_found_key} not found!")
