import json
import os
from datetime import datetime
from pathlib import Path

import requests
import yaml
from flojoy import DataContainer, flojoy
from flojoy.utils import PlotlyJSONEncoder

FRONTIER_URI = (
    os.environ.get("FRONTIER_URI")
    or "https://cipfsgeml2.execute-api.us-east-1.amazonaws.com"
)
MEASUREMENT_API = f"{FRONTIER_URI}/measurements"


@flojoy
def LOADER(dc_inputs: list[DataContainer], params: dict):
    api_key = get_api_key()
    measurement_uuid = params["measurement_uuid"]

    if api_key != "" and measurement_uuid != "":
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
        not_found_key = "FRONTIER_API_KEY" if api_key == "" else "Measurement UUID"
        raise KeyError(f"{not_found_key} not found!")


def get_api_key():
    home = str(Path.home())
    api_key = ""
    path = os.path.join(home, ".flojoy/credentials")
    if not os.path.exists(path):
        return api_key

    stream = open(path, "r", encoding="utf-8")
    yaml_dict = yaml.load(stream, Loader=yaml.FullLoader)
    if yaml_dict is None:
        return api_key
    if isinstance(yaml_dict, str) == True:
        split_by_line = yaml_dict.split("\n")
        for line in split_by_line:
            if "FRONTIER_API_KEY" in line:
                api_key = line.split(":")[1]
    else:
        api_key = yaml_dict.get("FRONTIER_API_KEY", "")
    return api_key


def set_api_key(api_key: str) -> bool:
    home = str(Path.home())
    path = os.path.join(home, ".flojoy/credentials")

    if not os.path.exists(path):
        return False

    with open(path, "r", encoding="utf-8") as stream:
        yaml_dict = yaml.load(stream, Loader=yaml.FullLoader)
        yaml_dict.put("FRONTIER_API_KEY", api_key)
    return True
