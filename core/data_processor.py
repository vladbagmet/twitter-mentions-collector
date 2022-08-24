__all__ = ['DataProcessor']

from datetime import datetime
from uuid import uuid4

import pytz
from pydantic.error_wrappers import ValidationError

from dto.twitter import Tweets
from utils.logger import logger
from core.object_storage import get_object_storage_client
from core.nosql_storage import get_nosql_storage_client
from core.data_retriever import DataRetriever
from settings import MAX_DAYS_BACK_DATA_RETRIEVAL_ALLOWED
from exceptions.input import InvalidInputDatesException
from utils.dates_ranges import generate_day_by_day_date_ranges
from core.abstract.data_processor import AbstractDataProcessor
from exceptions.client import UnexpectedApiResponseStructureException


class DataProcessor(AbstractDataProcessor):
    @staticmethod
    def _validate_input_dates(
            start_datetime: datetime,
            end_datetime: datetime,
    ) -> None:
        if start_datetime >= end_datetime:
            raise InvalidInputDatesException('End datetime should be greater than start datetime.')
        if (datetime.now(tz=pytz.UTC) - start_datetime).days > MAX_DAYS_BACK_DATA_RETRIEVAL_ALLOWED:
            raise InvalidInputDatesException(
                f'Not allowed to request data for more than {MAX_DAYS_BACK_DATA_RETRIEVAL_ALLOWED} days back.'
            )

    def process_tweets(
        self,
        query_string: str,
        start_datetime: datetime,
        end_datetime: datetime,
    ) -> None:
        self._validate_input_dates(start_datetime=start_datetime, end_datetime=end_datetime)
        data_retriever = DataRetriever()

        day_by_day_ranges = generate_day_by_day_date_ranges(start_datetime=start_datetime, end_datetime=end_datetime)
        for intraday_start_dt, intraday_end_dt in day_by_day_ranges:
            logger.info(
                f'Processing data collection for start_date `{intraday_start_dt}` and end_date `{intraday_end_dt}`.'
            )
            raw_data = data_retriever.get_tweets(
                query_string=query_string,
                start_datetime=intraday_start_dt,
                end_datetime=intraday_end_dt
            )
            logger.info('Raw data is retrieved from Twitter API.')
            object_storage = get_object_storage_client()
            object_storage.set(key=uuid4(), value=raw_data)
            logger.info('Raw data is saved into object storage.')

            try:
                structured_tweets = Tweets(**raw_data).statuses
            except ValidationError as e:
                logger.error(f'Failed to parse raw data, error: {e}.')
                raise UnexpectedApiResponseStructureException(
                    f'Twitter API response structure has changed, raw response: {raw_data}.'
                )
            nosql_storage = get_nosql_storage_client()
            logger.info(f'Got {len(structured_tweets)} to process, saving them to NoSQL storage...')
            for tweet in structured_tweets:
                nosql_storage.set(tweet.dict())  # ToDo: Save data in bulks.
            logger.info('Data processing is finished.')
