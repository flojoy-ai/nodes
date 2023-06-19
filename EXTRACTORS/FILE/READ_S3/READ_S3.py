from pathlib import Path
import os
import pandas as pd
import yaml
import io
import boto3
from flojoy import flojoy, DataContainer


@flojoy
def READ_S3(dc_inputs: list[DataContainer], params: dict[str, str]):
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
