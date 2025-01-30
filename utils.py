import os
from logging import Logger


def exit_if_none(logger: Logger, **kwargs):
    """Checks whether values are None and exits if they are"""
    for k, v in kwargs.items():
        logger.info(f"Checking if environment variable '{k}' is None")
        if v is None:
            logger.error(f"Environment variable '{k}' is None")
            os._exit(1)
