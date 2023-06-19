from pathlib import Path
import os
import pandas as pd
import yaml
import io
import boto3
from flojoy import flojoy, DataContainer


@flojoy
def READ_S3(dc_inputs: list[DataContainer], params: dict[str, str]):
    """
    The READ_S3 node takes S3_key name, S3 bucket name, and file name as input,
    and extract the file from the specified bucket using the S3_key that they saved.

    Parameters
    ----------
    s3_name:
        name of the key that the user used to save access and secret access key
    bucket_name:
        AWS S3 bucket name that they are trying to access
    file_name:
        name of the file that they want to extract

    Returns
    ------
    DataContainer:
        type 'dataframe', m
    """
    try:
        name = params["s3_name"]

        if name == "":
            raise ValueError("Provide a name that was used to set AWS S3 key")

        home = str(Path.home())
        file_path = os.path.join(home, ".flojoy/credentials.yaml")

        with open(file_path, "r") as file:
            data = yaml.safe_load(file)

        s3_access_key = data[name + "accessKey"]
        s3_secret_key = data[name + "secretKey"]

        s3 = boto3.resource(
            "s3", aws_access_key_id=s3_access_key, aws_secret_access_key=s3_secret_key
        )
        object = s3.Object(params["bucket_name"], params["file_name"])
        buffer = io.BytesIO()
        object.download_fileobj(buffer)
        df = pd.read_parquet(buffer)

        return DataContainer(type="dataframe", m=df)
    except Exception as e:
        raise e
