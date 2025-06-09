from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from collections.abc import AsyncGenerator
from typing import Iterable
import uuid
import pytest_asyncio
import pytest

from app.core.config import Settings, get_settings_no_cache
from app.repositories.animals import SQLAlchemyAnimalRepository
from app.models.animal import Animal
from app.models.base import BaseModel

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

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    BaseModel.metadata.drop_all(async_engine)
    BaseModel.metadata.create_all(async_engine)
    yield
    BaseModel.metadata.drop_all(async_engine)


@pytest_asyncio.fixture(scope="class")
async def session() -> AsyncGenerator[AsyncSession]:
    """Fixture for creating a new test session."""
    async with async_session() as s:
        yield s


@pytest.fixture(scope="class")
def repo(session):
    return SQLAlchemyAnimalRepository(db_session=session)


class TestAnimalRepository:
    @pytest.mark.parametrize("name", ("capybara", "giraffe", "wolf"))
    @pytest.mark.asyncio(loop_scope="class")
    async def test_can_create_any_animal(self, repo, name):
        animal = await repo.add_by_name(name)
        print(animal)
        assert type(animal) is Animal

    @pytest.mark.asyncio(loop_scope="class")
    async def test_cannot_get_unexistent(self, repo):
        animal = await repo.get_by_uuid(uuid.uuid4())
        assert animal is None

    @pytest.mark.asyncio(loop_scope="class")
    async def test_get_iterable_animals(self, repo):
        animals = await repo.get_all()
        assert isinstance(animals, Iterable)
