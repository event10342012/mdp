import os
import secrets

from dotenv import find_dotenv, load_dotenv
from pydantic import BaseSettings, AnyHttpUrl, validator

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    PROJECT_NAME: str = 'MDP'
    ENVIRONMENT: str = os.getenv('ENVIRONMENT') or 'dev'
    SECRET_KEY: str = os.getenv('SECRET_KEY') or secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str = 'MDP'
    SERVER_HOST: AnyHttpUrl = 'http://localhost'
    ALGORITHM: str = 'HS256'

    SQLALCHEMY_URI: str = os.getenv('SQLALCHEMY_URI')

    @validator('ENVIRONMENT')
    def check_environment(cls, v):
        if v.lower() not in ('dev', 'prod'):
            raise ValueError('ENVIRONMENT variable must be dev or prod')
        return v


settings = Settings()
