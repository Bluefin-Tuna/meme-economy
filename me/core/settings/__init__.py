from pydantic import BaseSettings, Field, PostgresDsn, RedisDsn
from typing import Optional
from .extra import ExtraSettings


class Settings(BaseSettings):

    """Storage container for important fields used by the app."""

    auth_key: Optional[str] = ""
    api_key: Optional[str] = ""

    pg_dsn: PostgresDsn = "postgresql://tanush:299792458@localhost:5432/meme-economy"
    re_dsn: Optional[RedisDsn] = None

    ex_settings: ExtraSettings = ExtraSettings()

    class Config:

        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()