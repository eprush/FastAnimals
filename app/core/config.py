"""
A module that implements endpoints of the type /animal_type
"""

import os
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    """Configuration settings for the application."""

    environment: str = "production"

    postgres_host: str = "localhost"
    postgres_port: str = "5432"
    postgres_db: str = "fast_animals"
    postgres_username: str = "postgres"
    postgres_password: str = "example"
    pool_size: int = 20

    table_name : str = "table.xlsx"

    cat_api_key: str = "peace_35mbejkg4uuVzdso0012"

    @property
    def url_asyncpg(self):
        return (f"postgresql+asyncpg://{self.postgres_username}:{self.postgres_password}@"
                f"{self.postgres_host}:{self.postgres_port}/{self.postgres_db}")

    model_config = SettingsConfigDict(env_file=os.getenv("ENV_FILE", ".env"))


@lru_cache
def get_app_settings() -> Settings:
    """Retrieve the application settings.

    Returns
    -------
        Settings: The application settings.

    """
    return Settings()


def get_settings_no_cache() -> Settings:
    """Получение настроек без кеша."""
    return Settings()

def get_static_dir() -> str:
    BASE_DIR = Path(__file__).resolve().parent.parent
    return os.path.join(BASE_DIR, "static")