"""
The script that runs the application
"""

from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

from core.config import Settings, get_app_settings
from endpoints.api import routers
from core.exception_handlers import (
    http_exception_handler,
    all_exception_handler,
)


def get_application() -> FastAPI:
    """Returns the FastAPI application instance."""
    settings: Settings = get_app_settings()

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
