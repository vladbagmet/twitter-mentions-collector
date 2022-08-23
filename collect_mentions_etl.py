import pytz
from datetime import datetime, timedelta

from prefect import flow, task

from core.data_processor import DataProcessor
from utils.logger import logger


@task
def _run_mentions_collection_etl_job():
    data_processor = DataProcessor()
    # ToDo: Store intermediate state (start and end date and times).
    start = datetime.now(tz=pytz.UTC) - timedelta(days=7)
    end = datetime.now(tz=pytz.UTC) - timedelta(days=1)
    data_processor.process_mentions(start, end)


@flow(name="Twitter Mentions Collection Flow")
def collect_mentions():
    logger.info('Twitter mentions collection has started...')
    _run_mentions_collection_etl_job()


collect_mentions()
