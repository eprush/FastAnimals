"""
A module that implements the search for functions for receiving photos of
 animals like get_{source}_{animal_type}.
When trying to add a new function in the import, give it an alias as get_{animal_type}
"""

import requests
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.animals import AnimalsRepository
from app.schemas.animal import AnimalDetailSchema
from app.services.animals.real_animals import (
    Fox,
    Dog,
    Cat,
    Animal
)

class AnimalsService:
    def __init__(self, db_session: AsyncSession) -> None:
        self.animals_repository = AnimalsRepository(db_session= db_session)
        self.animals: dict[str, Animal] = {"dog": Dog(), "cat": Cat(), "fox": Fox()}

    async def create_animal(self, animal_type: str) -> AnimalDetailSchema:
        animal = await self.animals_repository.create_animal_by(animal_type= animal_type)
        return AnimalDetailSchema.model_validate(animal)

    async def get_animal_by_uuid(self, uuid_code: UUID) -> AnimalDetailSchema:
        animal = await self.animals_repository.get_animal_by_uuid(uuid_code= uuid_code)
        return AnimalDetailSchema(
            id= animal.id,
            animal_type= animal.animal_type,
            processed_image= animal.processed_image,
            created_at= animal.created_at,
        )

    def request_animal_image(self, animal_type: str) -> bytes | None:
        animal = self.animals.get(animal_type, None)
        if animal is None:
            return #raise SomeError
        link, headers = animal.request_image()
        response = requests.get(link, headers=dict(headers))
        if response.status_code == 200:
            return response.content
        return #raise SomeError
