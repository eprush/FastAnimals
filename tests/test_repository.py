from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from collections.abc import AsyncGenerator
from typing import Iterable
import asyncio
import uuid
import pytest_asyncio
import pytest

from app.core.config import Settings, get_settings_no_cache
from app.repositories.animals import AnimalRepository
from app.models.animal import Animal

app_settings: Settings = get_settings_no_cache()

async_engine = create_async_engine(
    app_settings.url_test_asyncpg,
    pool_pre_ping=True,
    pool_size=app_settings.pool_size,
)

async_session = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
    autoflush=False,
)

@pytest_asyncio.fixture(scope="module")
async def session() -> AsyncGenerator[AsyncSession]:
    """Fixture for creating a new test session."""
    async with async_session() as s:
        yield s

@pytest.fixture(scope="module")
def repo(session):
    return AnimalRepository(db_session=session)


@pytest.mark.asyncio(loop_scope="module")
async def test_can_create_any_animal(repo):
    animal = await repo.create_animal("capybara")
    print(animal)
    assert type(animal) is Animal

@pytest.mark.asyncio(loop_scope="module")
async def test_cannot_get_unexistent(repo):
    animal = await repo.get_animal_by_uuid(uuid.uuid4())
    assert animal is None

@pytest.mark.asyncio(loop_scope="module")
async def test_get_iterable_animals(repo):
    animals = await repo.get_all_animals()
    assert isinstance(animals, Iterable)
