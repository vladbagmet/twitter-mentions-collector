__all__ = ['NosqlStorage', 'get_nosql_storage_client']

import contextlib

from typing import Optional, Dict, Any

import boto3
from botocore.exceptions import ClientError

from core.abstract.storage import AbstractStorage
from settings import DYNAMODB_TABLE_NAME, AWS_REGION_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


class NosqlStorage(AbstractStorage):
    def __init__(
        self,
        table_name: str,
        region: str,
        aws_access_key: str,
        aws_secret_access_key: str
    ):
        self.table_name = table_name
        self.db = boto3.resource(
            'dynamodb',
            region_name=region,
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_access_key
        )
        self.table = self.db.Table(self.table_name)

    def set(self, item: Dict[str, Any]) -> None:
        self.table.put_item(Item=item)

    def get(self, key: str, default=None) -> Optional[Dict[str, Any]]:
        with contextlib.suppress(ClientError):
            response = self.table.get_item(Key=key)
            return response['Item']
        return default


def get_nosql_storage_client() -> NosqlStorage:
    return NosqlStorage(
        table_name=DYNAMODB_TABLE_NAME,
        region=AWS_REGION_NAME,
        aws_access_key=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
