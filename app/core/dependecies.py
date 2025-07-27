"""
The module that defines the dependencies.
Among them, connection to the database, dependence on their own services
"""
import asyncio
from collections.abc import AsyncGenerator
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from fastapi import Depends
from asyncio import sleep

from app.core.config import Settings, get_app_settings
from app.services.animal import AnimalService
from app.services.image import AnimalImage
from app.services.email import EmailService

app_settings: Settings = get_app_settings()

async_engine = create_async_engine(
    app_settings.url_asyncpg,
    pool_pre_ping=True,
    pool_size=app_settings.pool_size,
)

async_session = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
    autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for getting a session with a database."""
    db = async_session()
    try:
        yield db
    finally:
        await db.close()


DatabaseDependence = Annotated[AsyncSession, Depends(get_db)]

async def get_animal_service(db: DatabaseDependence) -> AnimalService:
    """Returns an instance of AnimalsService."""
    await sleep(1)
    return AnimalService(db_session=db)

async def get_image_service() -> AnimalImage:
    await sleep(1)
    return AnimalImage()

async def get_email_service() -> EmailService:
    await asyncio.sleep(1)
    return EmailService(
        to_email=app_settings.email_address,
        from_email=app_settings.email_address,
        password=app_settings.email_password,
    )

AnimalServiceDependence = Annotated[AnimalService, Depends(get_animal_service)]
ImageServiceDependence = Annotated[AnimalImage, Depends(get_image_service)]
EmailServiceDependence = Annotated[EmailService, Depends(get_email_service)]
