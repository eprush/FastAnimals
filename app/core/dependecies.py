"""
The module that defines the dependencies.
Among them, connection to the database, dependence on their own services
"""

from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from typing import Annotated
from fastapi import Depends
from asyncio import sleep

from core.config import Settings, get_app_settings
from services.animal import AnimalsService
from services.image import AnimalImage

app_settings: Settings = get_app_settings()


pg_connection_string = (
    f"postgresql+asyncpg://{app_settings.pg_username}:{app_settings.pg_password}@"
    f"{app_settings.pg_host}:{app_settings.pg_port}/{app_settings.pg_database}"
)

async_engine = create_async_engine(
    pg_connection_string,
    pool_pre_ping=True,
    pool_size=app_settings.pool_size,
)

async_session = async_sessionmaker(
    async_engine, expire_on_commit=False, class_=AsyncSession, autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for getting a session with a database."""
    db = async_session()
    try:
        yield db
    finally:
        await db.close()


async def get_animals_service(db: Annotated[AsyncSession, Depends(get_db)]) -> AnimalsService:
    """Returns an instance of AnimalsService."""
    await sleep(1)
    return AnimalsService(db_session=db)

async def get_image_service() -> AnimalImage:
    await sleep(1)
    return AnimalImage()
