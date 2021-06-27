"""Common logger library for consistency across modules."""
# pylint: disable=too-few-public-methods
import logging


class Logger:
    """Common logger library that sets up a logger with a consistent format."""
    def __init__(self):
        self.logger = self._setup_logger()

    @classmethod
    def _setup_logger(cls):
        logger = logging.getLogger()
        return logger
