import uuid
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from models.animal import Animal


class AnimalsRepository:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create_animal(self, animal_type: str) -> Animal:
        """ A method for creating a сertain type of animal in the database. """
        statement = insert(Animal).values(
            processed_image=uuid.uuid4(),
            animal_type=animal_type,
        ).returning(Animal)
        result = await self.db_session.execute(statement)
        new_record = result.scalars().one()
        await self.db_session.commit()

        return new_record

    async def get_animal_by_uuid(self, uuid_code: uuid.UUID) -> Animal | None:
        """ Method for getting an animal by uuid. """
        statement = select(Animal).where(Animal.processed_image == uuid_code) # type error
        result = await self.db_session.execute(statement)
        return result.scalars().one_or_none()

    async def get_all_animals(self) -> tuple[Animal, ...]:
        """ Method for creating a query history file. """
        statement = select(Animal)
        result = await self.db_session.execute(statement)
        return tuple(result.scalars().all())
