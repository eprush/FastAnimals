from pathlib import Path

from app.core.config import Settings, get_app_settings


from app.endpoints.api import routers
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.staticfiles import StaticFiles


def get_application() -> FastAPI:
    """Returns the FastAPI application instance."""
    settings: Settings = get_app_settings()

    application = FastAPI(
        **settings.model_dump(),
        separate_input_output_schemas=False,
    )

    application.include_router(routers, prefix=settings.api_prefix)

    static_dir = Path("static")
    if static_dir.is_dir():
        application.mount("/app/static", StaticFiles(directory="static"), name="static")

    application.add_exception_handler(HTTPException, http_exception_handler)  # type: ignore
    application.add_exception_handler(Exception, all_exception_handler)  # type: ignore
    return application


app = get_application()
