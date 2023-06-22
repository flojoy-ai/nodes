import json
import os
import requests
from flojoy import DataContainer, flojoy
from flojoy.utils import PlotlyJSONEncoder, get_frontier_api_key

FRONTIER_URI: str = os.environ.get("FRONTIER_URI") or "https://frontier.flojoy.io"
MEASUREMENT_API: str = f"{FRONTIER_URI}/api/streaming"


@flojoy
def LOADER(dc_inputs: list[DataContainer], params: dict) -> DataContainer:
    api_key: str | None = get_frontier_api_key()
    if api_key is None:
        raise KeyError(f"Frontier API key is not found!")

    measurement_uuid: str = params["measurement_uuid"]
    if measurement_uuid == "":
        raise KeyError(f"Measurement ID is not found!")

    if dc_inputs:
        resp = requests.post(
            MEASUREMENT_API,
            json={
                "api_key": api_key,
                "measurement_id": measurement_uuid,
                "measurement": json.dumps(dc_inputs[0], cls=PlotlyJSONEncoder),
            },
        )
        if not (resp.status_code == 200 or resp.status_code == 201):
            raise Exception(str(resp.json()["error"]))
        return dc_inputs[0]

    else:
        resp = requests.get(
            MEASUREMENT_API,
            params={
                "api_key": api_key,
                "measurement_id": measurement_uuid,
            },
        )
        print(resp.json())
        # TODO: now it only supports x and y, and it only loads the first entry
        if not (resp.status_code == 200 or resp.status_code == 201):
            raise Exception(resp.json()["error"])
        return DataContainer(
            x=resp.json()["data"][0]["dataContainer"]["x"],
            y=resp.json()["data"][0]["dataContainer"]["y"],
        )
