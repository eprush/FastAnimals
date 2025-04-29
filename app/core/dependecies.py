from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import Settings, get_app_settings
from app.services.animal import AnimalsService
from app.services.image import AnimalImage
from typing import Annotated
from fastapi import Depends

app_settings: Settings = get_app_settings()

# Need to be changed
pg_connection_string = (
    f"postgresql+asyncpg://{app_settings.pg_username}:{app_settings.pg_password}@"
    f"{app_settings.pg_host}:{app_settings.pg_port}/{app_settings.pg_database}"
)

async_engine = create_async_engine(
    pg_connection_string,
    pool_pre_ping=True,
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


def get_animals_service(db: Annotated[AsyncSession, Depends(get_db)]) -> AnimalsService:
    """Returns an instance of AnimalsService."""
    return AnimalsService(db_session=db)

def get_image_service() -> AnimalImage:
    return AnimalImage()
