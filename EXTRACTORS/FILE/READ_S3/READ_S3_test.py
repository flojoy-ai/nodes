import boto3
import io
import pandas as pd
from moto import mock_s3, mock_iam
from moto.core import set_initial_no_auth_action_count

import pytest
from os import path
import json

# @mock_s3
# def test_my_model_save():
#     s3_resource, _ = create_bucket()
#     _file_path = f"{path.dirname(path.realpath(__file__))}/assets/userdata1.parquet"
#     s3_resource.meta.client.upload_file(_file_path, "flojoy-bucket", "userdata1.parquet")

#     return verify_upload()

@mock_iam
def create_user_with_access_key_and_policy(user_name="test-user"):
    """
    Should create a user with attached policy allowing read/write operations on S3.
    """
    policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {"Effect": "Allow", "Action": "s3:*", "Resource": "*"}
        ],
    }
    
    # Create client and user
    client = boto3.client("iam", region_name="us-east-1")
    client.create_user(UserName=user_name)

    # Create and attach the policy
    policy_arn = client.create_policy(
        PolicyName="policy1", PolicyDocument=json.dumps(policy_document)
    )["Policy"]["Arn"]
    client.attach_user_policy(UserName=user_name, PolicyArn=policy_arn)
    
    # Return the access keys
    return client.create_access_key(UserName=user_name)["AccessKey"]

def verify_upload():
    client = boto3.client("s3")
    resp = client.get_object(Bucket="flojoy-bucket", Key="userdata1.parquet")
    data=resp.get('Body').read()
    buffer = io.BytesIO(data)
    df = pd.read_parquet(buffer)
    return df.shape

def create_bucket():
    s3 = boto3.resource("s3")
    bucket = s3.create_bucket(Bucket="flojoy-bucket")
    return s3, bucket

@set_initial_no_auth_action_count(4)
@mock_s3
def test_READ_S3(mock_flojoy_decorator, mock_flojoy_cache_directory):

    import READ_S3
    s3_resource, _ = create_bucket()
    _file_path = f"{path.dirname(path.realpath(__file__))}/assets/userdata1.parquet"
    s3_resource.meta.client.upload_file(_file_path, "flojoy-bucket", "userdata1.parquet")
    
    upload_shape = verify_upload()

    output = READ_S3.READ_S3("test", "flojoy-bucket", "userdata1.parquet")
    print(output.m)
    # assert upload_shape == output.m.shape
