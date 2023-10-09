import logging.config
import sys
from datetime import datetime
from logging import Logger

from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        log_record['name'] = record.name
        log_record['level'] = record.levelname
        log_record['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_record['filename'] = record.filename
        log_record['funcName'] = record.funcName
        if not log_record.get('path'):
            log_record['lineno'] = f'{record.lineno}'

        super().add_fields(log_record, record, message_dict)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'json': {
            '()': CustomJsonFormatter,
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'json',
            'stream': sys.stdout,
        },
    },
    'root': {'handlers': ['console'], 'level': 'DEBUG'},
}

logging.config.dictConfig(LOGGING)
LOGGER: Logger = logging.getLogger()
