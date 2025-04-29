import requests
from app.core.config import get_app_settings
from app.services.animals.abstract_animal import AbstractAnimal, Link, Headers
from random import randint
from typing import Protocol, TypeVar


class Cat(AbstractAnimal):
    def get_image(self) -> tuple[Link, Headers]:
        settings = get_app_settings()
        api_key = str(settings.cat_api_key)

        headers = {"content_type": "application/json", "api_key": api_key}
        url = f"https://api.thecatapi.com/v1/images/search"
        response = requests.get(url, headers=headers).json()
        cat_link = response[0].get_image("url", None) if response else None
        return cat_link, headers

class Dog(AbstractAnimal):
    def get_image(self) -> tuple[Link, Headers]:
        headers = {"content_type": "application/json"}
        url = "https://dog.ceo/api/breeds/image/random"
        response = requests.get(url, headers=headers).json()
        dog_link = response.get_image("message", None) if response else None
        return dog_link, headers

class Fox(AbstractAnimal):
    def get_image(self) -> tuple[Link, Headers]:
        fox_count = 124
        random_fox_number = randint(1, fox_count)
        headers = {"content_type": "application/json"}
        fox_link = f"https://randomfox.ca//images//{random_fox_number}.jpg"
        return fox_link, headers

class AnimalProtocol(Protocol):
    def get_image(self) -> tuple[Link, Headers]:
        ...

Animal = TypeVar("Animal", bound=AnimalProtocol)