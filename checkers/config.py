"""Module containing the project configuration settings."""
import logging
import logging.config
import os

project_path = os.path.sep.join(__file__.split(os.path.sep)[:-2])

logdir = os.path.join(project_path, "logs")
os.makedirs(logdir, exist_ok=True)
logpath = os.path.join(logdir, "checkers.log")


class StdoutFilter(logging.Filter):
    """Standard output filter."""

    def filter(self, record: logging.LogRecord) -> bool:
        """Filter for stdout log records."""

        is_info = record.levelno >= logging.INFO
        is_not_warning = record.levelno < logging.WARNING

        return is_info and is_not_warning


class StderrFilter(logging.Filter):
    """Standard error filter."""

    def filter(self, record: logging.LogRecord) -> bool:
        """Filter for stderr."""

        return record.levelno >= logging.WARNING


logger_config = {
    "version": 1,
    "formatters": {
        "debug": {
            "format": "%(asctime)s  |  %(levelname)s  |  %(name)s  |  %(message)s"
        },
        "stdout": {
            "format": "%(message)s"
        },
        "stderr": {
            "format": "[%(levelname)s] %(message)s"
        }
    },
    "filters": {
        "stdout": {
            "()": StdoutFilter
        },
        "stderr": {
            "()": StderrFilter
        }
    },
    "handlers": {
        "debug": {
            "formatter": "debug",
            "class": "logging.FileHandler",
            "filename": logpath,
            "mode": "w",
            "level": "DEBUG"
        },
        "stdout": {
            "formatter": "stdout",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "filters": ["stdout"]
        },
        "stderr": {
            "formatter": "stderr",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
            "filters": ["stderr"]
        },
    },
    "loggers": {
        "__main__": {
            "level": "DEBUG",
            "handlers": ["debug", "stdout", "stderr"]
        },
        "checkers": {
            "level": "DEBUG",
            "handlers": ["debug", "stdout", "stderr"]
        }
    }
}
