"""
A module that implements the search for functions for receiving photos of
 animals like get_{source}_{animal_type}.
When trying to add a new function in the import, give it an alias as get_{animal_type}
"""

import requests
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
import os
from pathlib import Path

from app.repositories.animals import AnimalsRepository
from app.schemas.animal import AnimalDetailSchema
from app.services.animal_service.animals import (
    Fox,
    Dog,
    Cat,
    Animal
)

# Need to be changed
STATIC_DIR: str = os.path.join(Path(__file__).resolve().parent.parent.parent, "static")
def get_new_file_path(filename: str):
    return os.path.join(STATIC_DIR, filename + ".jpg")

class AnimalsService:
    def __init__(self, db_session: AsyncSession) -> None:
        self.animals_repository = AnimalsRepository(db_session= db_session)
        self.animals: dict[str, Animal] = {"dog": Dog, "cat": Cat, "fox": Fox}

    async def create_animal_by(self, animal_type: str) -> AnimalDetailSchema:
        animal = await self.animals_repository.create_animal_by(animal_type= animal_type)
        return AnimalDetailSchema.model_validate(animal)

    def get_animal_image(self, animal_type: str) -> bytes | None:
        animal = self.animals.get(animal_type, None)
        if animal is None:
            return #raise SomeError
        link, headers = animal.get_image()
        response = requests.get(link, headers=dict(headers))
        if response.status_code == 200:
            return response.content
        return #raise SomeError

    @staticmethod
    def save_image(data: bytes, *, name: UUID) -> None:
        filepath = get_new_file_path(str(name))
        with open(filepath, "wb") as file:
            file.write(data)
        return
