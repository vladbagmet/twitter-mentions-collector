__all__ = ['logger']

import sys
import logging

logger = logging.getLogger('etl')
handler = logging.StreamHandler(sys.stderr)
logger.setLevel(logging.INFO)
