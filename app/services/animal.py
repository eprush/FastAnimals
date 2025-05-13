"""
A module that implements the search for functions for receiving photos of
 animals like get_{source}_{animal_type}.
When trying to add a new function in the import, give it an alias as get_{animal_type}
"""

from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from repositories.animals import AnimalsRepository
from integrations.common import AnimalReceiver
from schemas.animal import (
    AnimalDetailSchema,
    AllAnimalsSchema,
    ImageSchema,
)

class AnimalsService:
    def __init__(self, db_session: AsyncSession) -> None:
        self.animals_repository = AnimalsRepository(db_session= db_session)
        self.animal_receiver: AnimalReceiver = AnimalReceiver()

    async def create_animal(self, *, animal_type: str) -> AnimalDetailSchema:
        """ A method for creating a сertain type of animal. """
        animal = await self.animals_repository.create_animal(animal_type)
        return AnimalDetailSchema.model_validate(animal)

    async def get_animal_by_uuid(self, uuid_code: UUID) -> AnimalDetailSchema | None:
        """ Method for getting an animal by uuid. """
        animal = await self.animals_repository.get_animal_by_uuid(uuid_code)
        return AnimalDetailSchema.model_validate(animal) if animal is not None else None

    async def get_all_animals(self) -> AllAnimalsSchema:
        """ Method for creating a query history file. """
        all_animals = await self.animals_repository.get_all_animals()
        return AllAnimalsSchema(animals= all_animals)

    def request_animal_image(self, *, animal_type: str) -> ImageSchema | None:
        """ A method for sending a request for a photo of a certain type of animal. """
        image_bytes = self.animal_receiver.request_image(animal_type)
        return ImageSchema(image= image_bytes) if image_bytes is not None else None
