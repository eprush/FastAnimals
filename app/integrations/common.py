"""
A module describing a wrapper service around external animal access services
"""

import requests

from app.integrations.abstract_animal import AbstractAnimalReceiver
from app.integrations.real_animals import (
    DogReceiver,
    CatReceiver,
    FoxReceiver,
)

class AnimalReceiver:
    """ A class for all types of animals. """
    def __init__(self):
        self.animal_receivers: dict[str, AbstractAnimalReceiver] = {
            "dog": DogReceiver(),
            "cat": CatReceiver(),
            "fox": FoxReceiver()
        }

    def request_image(self, animal_type: str) -> bytes | None:
        """ A method for sending a request for a photo of a certain type of animal. """
        animal = self.animal_receivers.get(animal_type, None)
        if animal is None:
            return

        link, headers = animal.request_image()
        response = requests.get(link, headers=dict(headers))
        if response.status_code == 200:
            return response.content
