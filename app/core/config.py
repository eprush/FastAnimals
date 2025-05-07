import os
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    """Configuration settings for the application."""

    pg_host: str = "localhost"
    pg_port: str = "5432"
    pg_database: str = "fast_animals"
    pg_username: str = "postgres"
    pg_password: str = "example"

    table_name : str = "table.xlsx"

    cat_api_key: str = "peace_35mbejkg4uuVzdso0012"

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