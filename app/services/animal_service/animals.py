"""
A module that implements the search for functions for receiving photos of
 animals like get_{source}_{animal_type}.
When trying to add a new function in the import, give it an alias as get_{animal_type}
"""

from collections.abc import Callable
import requests
import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.animals_repository import AnimalsRepository

import os
from pathlib import Path

from app.services.animal_service.dogs import get_dogapi_dog as get_dog
from app.services.animal_service.foxes import get_randomfox_fox as get_fox
from app.services.animal_service.cats import get_thecatapi_cat as get_cat


STATIC_DIR = os.path.join(Path(__file__).resolve().parent.parent.parent, "static")
def get_new_file_path():
    filename = str(uuid.uuid4()) + ".jpg"
    return os.path.join(STATIC_DIR, filename)

class AnimalsService:
    animals: dict[str, Callable[[], tuple[str, dict]]] = {
        name[4:]: func for name, func in globals().items()
        if name.startswith("get_") and callable(func)
    }

    def __init__(self, db_session: AsyncSession) -> None:
        self.animals_repository = AnimalsRepository(db_session= db_session)

    def get_image(self, animal_type: str) -> bytes | None:
        func = self.animals.get(animal_type, None)
        if func is None:
            return #raise SomeError
        link, headers = func()
        response = requests.get(link, headers=headers)
        if response.status_code == 200:
            return response.content
        return #raise SomeError

    @staticmethod
    def save_image(data: bytes) -> None:
        filepath = get_new_file_path()
        with open(filepath, "wb") as file:
            file.write(data)
        return
