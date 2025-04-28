from sqlalchemy.ext.asyncio import AsyncSession

class AnimalsRepository:
    def __init__(self, db_session: AsyncSession) -> None:
        ...
