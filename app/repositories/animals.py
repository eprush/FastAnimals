"""
A module defining repository service for animal accessing at database
"""

import uuid
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.asbtract_repository import AbstractRepository
from app.models.animal import Animal


class SQLAlchemyAnimalRepository(AbstractRepository):
    Model = Animal
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def add_by_name(self, name: str) -> Model:
        """ A method for creating a сertain type of animal in the database. """
        statement = insert(self.Model).values(
            processed_image=uuid.uuid4(),
            animal_type=name,
        ).returning(self.Model)
        result = await self.db_session.execute(statement)
        new_record = result.scalars().one()
        await self.db_session.commit()

        return new_record

    async def get_by_uuid(self, uuid_code: uuid.UUID) -> Model | None:
        """ Method for getting an animal by uuid. """
        statement = select(self.Model).where(Animal.processed_image == uuid_code) # type error
        result = await self.db_session.execute(statement)
        return result.scalars().one_or_none()

    async def get_all(self) -> tuple[Model, ...]:
        """ Method for creating a query history file. """
        statement = select(self.Model)
        result = await self.db_session.execute(statement)
        return tuple(result.scalars().all())
