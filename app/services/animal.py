"""
A module that implements the search for functions for receiving photos of
 animals like get_{source}_{animal_type}.
When trying to add a new function in the import, give it an alias as get_{animal_type}
"""

from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
import pandas as pd
import os

from app.repositories.animals import AnimalsRepository
from app.schemas.animal import AnimalDetailSchema
from app.core.config import (
    get_static_dir,
    get_app_settings
)
from app.services.animals.real_animals import AnimalReceiver

class AnimalsService:
    def __init__(self, db_session: AsyncSession) -> None:
        self.animals_repository = AnimalsRepository(db_session= db_session)
        self.animal_receiver: AnimalReceiver = AnimalReceiver()

    async def create_animal(self, animal_type: str) -> AnimalDetailSchema:
        """ A method for creating a сertain type of animal. """
        animal = await self.animals_repository.create_animal_by(animal_type= animal_type)
        return AnimalDetailSchema.model_validate(animal)

    async def get_animal_by_uuid(self, uuid_code: UUID) -> AnimalDetailSchema:
        """ Method for getting an animal by uuid. """
        animal = await self.animals_repository.get_animal_by_uuid(uuid_code= uuid_code)
        return AnimalDetailSchema(
            id= animal.id,
            animal_type= animal.animal_type,
            processed_image= animal.processed_image,
            created_at= animal.created_at,
        )

    async def get_all_animals(self):
        """ Method for creating a query history file. """
        table_path = os.path.join(get_static_dir(), get_app_settings().table_name)
        if os.path.exists(table_path):
            os.remove(table_path)

        all_animals = await self.animals_repository.get_all_animals()
        data = pd.DataFrame({
            "id": [],
            "animal type": [],
            "processed image": [],
            "created at": []
        })
        for i, animal in enumerate(all_animals):
            data.loc[i] = [
                animal.id,
                animal.animal_type,
                animal.processed_image,
                str(animal.created_at)
            ]
        data.to_excel(table_path, index= False)
        return table_path

    def request_animal_image(self, animal_type: str) -> bytes | None:
        """ A method for sending a request for a photo of a certain type of animal. """
        return self.animal_receiver.request_image(animal_type)
