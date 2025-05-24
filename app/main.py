"""
The script that runs the application
"""

from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
import logging

from core.config import Settings, get_app_settings
from core.logging_config import setup_json_logging
from endpoints.api import routers
from core.exception_handlers import (
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
        separate_input_output_schemas=False,
    )

    application.include_router(routers)

    static_dir = Path("static")
    if static_dir.is_dir():
        application.mount("/app/static", StaticFiles(directory="static"), name="static")

    application.add_exception_handler(HTTPException, http_exception_handler) # type: ignore
    application.add_exception_handler(Exception, all_exception_handler)

    return application


app = get_application()
