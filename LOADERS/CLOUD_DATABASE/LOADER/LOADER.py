import json
import os
import requests
from flojoy import DataContainer, flojoy
from flojoy.utils import PlotlyJSONEncoder, get_frontier_api_key

FRONTIER_URI: str = os.environ.get("FRONTIER_URI") or "https://frontier.flojoy.io"
MEASUREMENT_API: str = f"{FRONTIER_URI}/api/streaming"


@flojoy
def LOADER(default: DataContainer, measurement_uuid: str = "") -> DataContainer:
    api_key: str | None = get_frontier_api_key()
    if api_key is None:
        raise KeyError(f"Frontier API key is not found!")

    if measurement_uuid == "":
        raise KeyError(f"Measurement ID is not found!")

    if default:
        resp = requests.post(
            MEASUREMENT_API,
            json={
                "api_key": api_key,
                "measurement_id": measurement_uuid,
                "measurement": json.dumps(default, cls=PlotlyJSONEncoder),
            },
        )
        if not (resp.status_code == 200 or resp.status_code == 201):
            raise Exception(str(resp.json()["error"]))
        return default

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
