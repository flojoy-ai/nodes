import os
from flojoy import DataContainer, flojoy, get_env_var, node_preflight
from flojoy.flojoy_cloud import FlojoyCloud


FLOJOY_CLOUD_URI: str = os.environ.get("FLOJOY_CLOUD_URI") or "https://cloud.flojoy.ai"


@node_preflight
def preflight():
    api_key = get_env_var("FLOJOY_CLOUD_KEY")

    if api_key is None:
        raise KeyError(
            "Flojoy Cloud key is not found! You can set it under Settings -> Environment Variables."
        )


@flojoy
def FLOJOY_CLOUD_DOWNLOAD(
    data_container_id: str,
) -> DataContainer:
    """The FLOJOY_CLOUD_DOWNLOAD node downloads a DataContainer from Flojoy Cloud.

    Parameters
    ----------
    data_container_id: The data container id of the data to be downloaded from Flojoy Cloud.

    Returns
    -------
    DataContainer
        The downloaded DataContainer will be returned as it is
    """

    api_key = get_env_var("FLOJOY_CLOUD_KEY")

    if api_key is None:
        raise KeyError(
            "Flojoy Cloud key is not found! You can set it under Settings -> Environment Variables."
        )

    cloud = FlojoyCloud(apikey=api_key)

    return cloud.to_dc(cloud.fetch_dc(data_container_id))
