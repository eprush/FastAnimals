"""
The script that runs the application
"""
import os.path
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
import logging

from app.core.config import (
    Settings,
    get_app_settings,
    get_static_dir
)
from app.core.logging_config import setup_json_logging
from app.endpoints.api import routers
from app.core.exception_handlers import (
    http_exception_handler,
    all_exception_handler,
)


def get_application() -> FastAPI:
    """Returns the FastAPI application instance."""
    settings: Settings = get_app_settings()

    if settings.environment != "development":
        setup_json_logging()
        logger = logging.getLogger("health_tracker")
        logger.warning("Running in production mode")

    application = FastAPI(
        **settings.model_dump(),
        title="FastAnimals",
        description="Приложение для получения случайных фотографий животных",
        separate_input_output_schemas=False,
        contact={
            "name": "eprush",
            "url": "https://github.com/eprush",
            "email": "pavlovich.er@phystech.edu"
        },
        license_info={
            "name": "MIT",
            "url": "https://opensource.org/license/mit"
        },
    )

    application.include_router(routers)
    STATIC_DIR = get_static_dir()
    if not os.path.exists(STATIC_DIR):
        os.mkdir(STATIC_DIR)

    static_dir = Path("static")
    if static_dir.is_dir():
        application.mount("/app/static", StaticFiles(directory="static"), name="static")

    application.add_exception_handler(HTTPException, http_exception_handler) # type: ignore
    application.add_exception_handler(Exception, all_exception_handler)

    return application


app = get_application()
