from pathlib import Path

from app.core.config import Settings, get_app_settings

from app.endpoints.api import routers
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


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

    return application


app = get_application()
