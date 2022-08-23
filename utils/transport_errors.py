__all__ = ['retry_if_5xx_or_connection_error']

from requests.exceptions import HTTPError, ConnectionError, SSLError


def is_5xx_error(e):
    return True if isinstance(e, HTTPError) and 500 <= e.response.status_code < 600 else False


def is_connection_error(e):
    return True if isinstance(e, SSLError) or isinstance(e, ConnectionError) else False


def retry_if_5xx_or_connection_error(e):
    return True if is_5xx_error(e) or is_connection_error(e) else False
