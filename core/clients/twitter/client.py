import json
from json.decoder import JSONDecodeError
from datetime import datetime
from urllib.parse import urlencode
from typing import Dict, Any, Optional

from retrying import retry
from requests import Response, get

from core.abstract.twitter import AbstractTwitterClient
from utils.transport_errors import retry_if_5xx_or_connection_error
from exceptions.client import ClientConfigurationException, MethodNotImplementedException, EmptyApiResponseException

UTC_TIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


class TwitterClient(AbstractTwitterClient):
    def __init__(self, bearer_token: str) -> None:
        if not all([bearer_token, isinstance(bearer_token, str)]):
            raise ClientConfigurationException(f'Bearer token should be provided to initialize client.')
        self._api_url = 'https://api.twitter.com/1.1'
        self._set_headers(bearer_token=bearer_token)

    def _set_headers(self, bearer_token) -> None:
        self._headers = {
            'Authorization': f"Bearer {bearer_token}"
        }

    @retry(
        retry_on_exception=retry_if_5xx_or_connection_error,
        stop_max_attempt_number=5,
        wait_fixed=6000
    )
    def _make_request(self, method: str, path: str, params: Dict[str, Any]) -> Response:
        if method != 'GET':
            raise MethodNotImplementedException(f'Method `{method}` not implemented.')
        non_empty_params = {key: value for key, value in params.items() if value}
        encoded_parameters = urlencode(non_empty_params)
        response = get(
            f'{self._api_url}/{path}?{encoded_parameters}',
            headers=self._headers
        )
        response.raise_for_status()
        return response

    def retrieve_tweets(
        self,
        query_string: str,
        start_datetime: datetime,
        end_datetime: datetime,
        tweet_fields: Optional[str],
        expansions: Optional[str],
        user_fields: Optional[str],
        place_fields: Optional[str]
    ) -> Dict[str, Any]:
        """ Finds tweets by specified search parameters. """

        api_path = '/search/tweets.json'
        params = {
            'q': query_string,
            'start_time': start_datetime.strftime(UTC_TIME_FORMAT),
            'end_time': end_datetime.strftime(UTC_TIME_FORMAT),
            'tweet.fields': tweet_fields,
            'expansions': expansions,
            'user.fields': user_fields,
            'place.fields': place_fields
        }
        response = self._make_request(
            method='GET',
            path=api_path,
            params=params
        )

        try:
            deserialized_response = json.loads(response.text)
        except (JSONDecodeError, TypeError,) as _:
            raise EmptyApiResponseException(
                'Got empty response from Twitter API, '
                f'start_datetime `{start_datetime}`, end_datetime `{end_datetime}`.'
            )
        return deserialized_response
