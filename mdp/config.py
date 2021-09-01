from typing import Optional

from pydantic import BaseConfig


class Settings(BaseConfig):
    SQLALCHEMY_DATABASE_URI: Optional[str] = None


settings = Settings()
