__all__ = ['generate_day_by_day_date_ranges']

from datetime import datetime, timedelta
from typing import Optional, List, Tuple

import pytz

from exceptions.input import InvalidInputDatesException


def _get_day_start_datetime(dt: datetime) -> datetime:
    return datetime(
        year=dt.year,
        month=dt.month,
        day=dt.day,
        hour=0,
        minute=0,
        second=0,
        tzinfo=pytz.UTC
    )


def _get_day_end_datetime(dt: datetime) -> datetime:
    return datetime(
        year=dt.year,
        month=dt.month,
        day=dt.day,
        hour=23,
        minute=59,
        second=59,
        tzinfo=pytz.UTC
    )


def _get_intraday_datetime_range(dt) -> Tuple[datetime, datetime]:
    start = _get_day_start_datetime(dt)
    now = datetime.now(tz=pytz.UTC) - timedelta(days=1)  # Yesterday can be chosen as most recent end datetime.
    end = _get_day_end_datetime(now)
    return start, end


def _validate_input_parameters(
    start_date: Optional[datetime],
    end_date: Optional[datetime]
) -> None:
    if not any([isinstance(start_date, datetime), isinstance(end_date, datetime)]):
        raise InvalidInputDatesException(f'Datetime only arguments are expected.')

    for dt in [start_date, end_date]:
        if dt and not dt.tzinfo:
            raise InvalidInputDatesException(f'Timezone naive datetime arguments are not allowed.')

    if end_date and end_date + timedelta(days=1) > datetime.now(pytz.UTC):
        raise InvalidInputDatesException(f'Date or end date can not be greater than day before yesterday.')

    if (start_date and not end_date) or (end_date and not start_date):
        raise InvalidInputDatesException(f'Both start and end dates should be defined.')


def generate_day_by_day_date_ranges(
    start_datetime: Optional[datetime],
    end_datetime: Optional[datetime]
) -> List[Tuple[datetime, datetime]]:
    _validate_input_parameters(start_date=start_datetime, end_date=end_datetime)

    if abs((end_datetime - start_datetime).total_seconds()/3600) > 24:
        start, end = start_datetime, end_datetime
    else:
        start, end = _get_intraday_datetime_range(start_datetime)
        return [(start, end,)]

    dates_ranges = []
    days_between = (end - start).days
    for day in range(days_between):
        dt = start + timedelta(days=day)
        intraday_start = _get_day_start_datetime(dt)
        intraday_end = _get_day_end_datetime(dt)
        dates_ranges.append((intraday_start, intraday_end,))
    return dates_ranges
