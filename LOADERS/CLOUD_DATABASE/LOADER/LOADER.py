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
    measurement_uuid: str = params["measurement_uuid"]

    if dc_inputs:
        if api_key is not None and measurement_uuid != "":
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
            not_found_key = (
                "FRONTIER_API_KEY" if api_key is not None else "Measurement UUID"
            )
            raise KeyError(f"{not_found_key} not found!")

    if api_key is not None and measurement_uuid != "":
        dc_list = requests.get(
            MEASUREMENT_API,
            params={
                "api_key": api_key,
                "measurement_id": measurement_uuid,
            },
        ).json()
        # TODO: now it only supports x and y, and it only loads the first entry
        if not (dc_list.status_code == 200 or dc_list.status_code == 201):
            raise Exception(dc_list.json()["message"])
        return DataContainer(
            x=dc_list[0]["dataContainer"]["x"], y=dc_list[0]["dataContainer"]["y"]
        )
    else:
        not_found_key = (
            "FRONTIER_API_KEY" if api_key is not None else "Measurement UUID"
        )
        raise KeyError(f"{not_found_key} not found!")
