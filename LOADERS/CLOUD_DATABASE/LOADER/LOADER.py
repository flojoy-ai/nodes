import json
import os
import requests
from flojoy import DataContainer, flojoy
from flojoy.utils import PlotlyJSONEncoder, get_frontier_api_key

FRONTIER_URI: str = os.environ.get("FRONTIER_URI") or "https://frontier-next.vercel.app"
MEASUREMENT_API: str = f"{FRONTIER_URI}/api/streaming"


@flojoy
def LOADER(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    api_key: str | None = get_frontier_api_key()
    measurement_uuid: str = params["measurement_uuid"]

    if api_key is not None and measurement_uuid != "":
        try:
            requests.post(
                MEASUREMENT_API,
                json={
                    "api_key": api_key,
                    "measurement_id": measurement_uuid,
                    "measurement": json.dumps(dc_inputs[0], cls=PlotlyJSONEncoder),
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
