import os
from logging.config import dictConfig

from pydantic import BaseModel


class Config:
    PROJECT_NAME: str = 'fastapi_index'

    DB_USERNAME: str = os.getenv('DB_USERNAME')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD')
    DB_HOST: str = os.getenv('DB_HOST', '127.0.0.1')
    DB_PORT: str = os.getenv('DB_PORT', 3306)
    DB_NAME: str = os.getenv('DB_NAME')

    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'info')

    @property
    def db_url(self):
        return f'mysql://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


config = Config()


class LogConfig(BaseModel):
    LOGER_NAME: str = config.PROJECT_NAME
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = config.LOG_LEVEL

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        "app": {"handlers": ["default"], "level": LOG_LEVEL},
    }


dictConfig(LogConfig().dict())
