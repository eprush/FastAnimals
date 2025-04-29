import uuid

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.animal_model import Animal

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
