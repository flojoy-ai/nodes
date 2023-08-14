import json
import os
from typing import Optional
import requests
from flojoy import DataContainer, flojoy, get_env_var
from flojoy.utils import PlotlyJSONEncoder


FRONTIER_URI: str = os.environ.get("FRONTIER_URI") or "https://cloud.flojoy.ai"


@flojoy
def LOADER(
    default: DataContainer,
    measurement_id: Optional[str] = None,
    dc_id: Optional[str] = None,
) -> DataContainer:
    api_key = get_env_var("FLOJOY_CLOUD_KEY")

    if api_key is None:
        raise KeyError("Flojoy Cloud API key is not found!")

    if default:
        # This will stream the data to the cloud
        resp: requests.Response
        if measurement_id is None:
            resp = requests.post(
                f"{FRONTIER_URI}/api/v1/measurements/{measurement_id}",
                headers={"api_key": api_key},
                json={
                    "data": json.dumps(default, cls=PlotlyJSONEncoder),
                },
            )

        else:
            resp = requests.post(
                f"{FRONTIER_URI}/api/v1/dcs",
                headers={"api_key": api_key},
                json={
                    "measurement_id": measurement_id,
                    "data": json.dumps(default, cls=PlotlyJSONEncoder),
                },
            )

        if not (resp.status_code >= 200 and resp.status_code < 300):
            raise Exception(str(resp.json()["error"]))

        return default

    else:
        # If there is nothing connected to the node, then it will download from cloud
        if dc_id is None:
            raise Exception("A data container ID is required for downstreaming")

        resp = requests.get(
            f"{FRONTIER_URI}/api/v1/dcs/{dc_id}",
            headers={"api_key": api_key},
        )
        print(resp.json())
        # TODO: now it only supports x and y
        if not (resp.status_code == 200 or resp.status_code == 201):
            raise Exception(resp.json()["error"])

        return DataContainer(
            x=resp.json()["data"][0]["dataContainer"]["x"],
            y=resp.json()["data"][0]["dataContainer"]["y"],
        )
