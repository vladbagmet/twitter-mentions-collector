__all__ = ['ObjectStorage', 'get_object_storage_client']

import io
import pickle
from http import HTTPStatus
from typing import Any, Union
from uuid import UUID

import boto3
from botocore.exceptions import ClientError

from core.abstract.storage import AbstractStorage
from settings import BUCKET_NAME, AWS_REGION_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


class ObjectStorage(AbstractStorage):
    def __init__(
        self,
        bucket_name: str,
        region: str,
        aws_access_key: str,
        aws_secret_access_key: str
    ):
        self.bucket_name = bucket_name
        self.s3 = boto3.resource(
            's3',
            region_name=region,
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_access_key
        )
        self.bucket = self.s3.Bucket(bucket_name)

    def set(self, key: Union[UUID, str], value: Any):
        value = pickle.dumps(value)
        return self.bucket.put_object(Key=str(key), Body=value)

    def get(self, key, default=None):
        with io.BytesIO() as stream:
            try:
                self.bucket.download_fileobj(key, stream)
            except ClientError as err:
                code = err.response.get('Error', {}).get('Code', 'Unknown')
                if code == HTTPStatus.NOT_FOUND:
                    return default
                else:
                    raise
            stream.seek(0)
            data = stream.read()
        return pickle.loads(data)


def get_object_storage_client() -> ObjectStorage:
    return ObjectStorage(
        bucket_name=BUCKET_NAME,
        region=AWS_REGION_NAME,
        aws_access_key=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
