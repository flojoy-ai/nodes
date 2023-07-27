import boto3
import io
import pandas as pd
from moto import mock_s3
from moto.core import set_initial_no_auth_action_count
import pytest
from os import path
from flojoy import DataFrame


def verify_upload():
    client = boto3.client("s3")
    resp = client.get_object(Bucket="flojoy-bucket", Key="userdata1.parquet")
    data = resp.get("Body").read()
    buffer = io.BytesIO(data)
    df = pd.read_parquet(buffer)
    return df.shape


def create_bucket():
    s3 = boto3.resource("s3")
    bucket = s3.create_bucket(Bucket="flojoy-bucket")
    return s3, bucket


@set_initial_no_auth_action_count(10)
@mock_s3
@pytest.mark.slow
def test_READ_S3(mock_flojoy_decorator, mock_flojoy_cache_directory):
    import READ_S3

    s3_resource, _ = create_bucket()
    _file_path = f"{path.dirname(path.realpath(__file__))}/assets/userdata1.parquet"
    s3_resource.meta.client.upload_file(
        _file_path, "flojoy-bucket", "userdata1.parquet"
    )

    upload_shape = verify_upload()

    output = READ_S3.READ_S3("test", "flojoy-bucket", "userdata1.parquet")
    assert isinstance(output, DataFrame)
    assert upload_shape == output.m.shape
