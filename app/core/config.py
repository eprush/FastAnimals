import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration settings for the application."""

    environment: str = "development"

    debug: bool = True

    docs_url: str = "/api/docs"
    openapi_url: str = "/api/openapi.json"
    api_prefix: str = "/api"

    title: str = "Animal Photo Downloader"
    version: str = "0.1.0"
    description: str = "Приложение для показа рандомных фотографий животных"

    allowed_hosts: list[str] | None = ["localhost"]

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