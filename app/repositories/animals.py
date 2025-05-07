import uuid
from sqlalchemy import insert, select, Row
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.animal import Animal

AnimalRow = Row[tuple[Animal]]

class AnimalsRepository:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create_animal_by(self, animal_type: str) -> Animal | None:
        statement = insert(Animal).values(
            processed_image=uuid.uuid4(),
            animal_type=animal_type,
        ).returning(Animal)
        result = await self.db_session.execute(statement)
        new_record = result.scalars().one()
        await self.db_session.commit()

        return new_record

    async def get_animal_by_uuid(self, uuid_code: uuid.UUID) -> Animal | None:
        statement = select(Animal).where(Animal.processed_image == uuid_code) # type error
        result = await self.db_session.execute(statement)
        return result.scalars().one_or_none()

    async def get_all_animals(self) -> tuple[AnimalRow, ...]:
        statement = select(Animal)
        result = await self.db_session.execute(statement)
        return tuple(result.scalars().all())
