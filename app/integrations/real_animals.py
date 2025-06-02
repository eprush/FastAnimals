"""
A module describing the implementations of an external animal service interface for accessing all animal types
"""

import requests
from random import randint

from app.core.config import get_app_settings
from app.integrations.abstract_animal import AbstractAnimalReceiver, Link, Headers


class CatReceiver(AbstractAnimalReceiver):
    """ A class for thecatapi.com """
    def request_image(self) -> tuple[Link, Headers]:
        settings = get_app_settings()
        api_key = str(settings.cat_api_key)

        headers = {"content_type": "application/json", "api_key": api_key}
        url = f"https://api.thecatapi.com/v1/images/search"
        response = requests.get(url, headers=headers).json()
        cat_link = response[0].get("url", None) if response else None
        return cat_link, headers

class DogReceiver(AbstractAnimalReceiver):
    """ A class for dog.ceo """
    def request_image(self) -> tuple[Link, Headers]:
        headers = {"content_type": "application/json"}
        url = "https://dog.ceo/api/breeds/image/random"
        response = requests.get(url, headers=headers).json()
        dog_link = response.get("message", None) if response else None
        return dog_link, headers

class FoxReceiver(AbstractAnimalReceiver):
    """ A class for randomfox.ca """
    def request_image(self) -> tuple[Link, Headers]:
        fox_count = 124
        random_fox_number = randint(1, fox_count)
        headers = {"content_type": "application/json"}
        fox_link = f"https://randomfox.ca//images//{random_fox_number}.jpg"
        return fox_link, headers