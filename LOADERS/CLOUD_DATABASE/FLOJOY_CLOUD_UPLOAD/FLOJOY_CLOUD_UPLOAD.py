import json
import os
from typing import Optional
import requests
from flojoy import DataContainer, flojoy, get_env_var
from flojoy.utils import PlotlyJSONEncoder


FLOJOY_CLOUD_URI: str = os.environ.get("FRONTIER_URI") or "https://cloud.flojoy.ai"


@flojoy
def FLOJOY_CLOUD_UPLOAD(
    default: DataContainer,
    measurement_id: Optional[str] = None,
) -> DataContainer:
    """The FLOJOY_CLOUD_UPLOAD node takes a DataContainer as input and uploads that to Flojoy Cloud.

    Parameters
    ----------
    measurement_id: The measurement id of the data to be uploaded to Flojoy Cloud. If not provided, a new measurement will be created.

    Returns
    -------
    DataContainer
        The input DataContainer will be returned as it is
    """

    api_key = get_env_var("FLOJOY_CLOUD_KEY")

    if api_key is None:
        raise KeyError(
            "Flojoy Cloud key is not found! You can set it under Settings -> Environment Variables."
        )

    if default:
        # This will stream the data to the cloud
        resp: requests.Response
        if measurement_id is None:
            resp = requests.post(
                f"{FLOJOY_CLOUD_URI}/api/v1/measurements/{measurement_id}",
                headers={"api_key": api_key},
                json={
                    "data": json.dumps(default, cls=PlotlyJSONEncoder),
                },
            )

        else:
            resp = requests.post(
                f"{FLOJOY_CLOUD_URI}/api/v1/dcs",
                headers={"api_key": api_key},
                json={
                    "measurement_id": measurement_id,
                    "data": json.dumps(default, cls=PlotlyJSONEncoder),
                },
            )

        if not (resp.status_code >= 200 and resp.status_code < 300):
            raise Exception(str(resp.json()["error"]))

    return default
