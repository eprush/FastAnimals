from typing import NotRequired, TypedDict
from abc import ABC, abstractmethod


Link = str

class Headers(TypedDict):
    api_key: NotRequired[str]
    content_type: str

class AbstractAnimal(ABC):

    @abstractmethod
    def get_image(self) -> tuple[Link, Headers]:
        """Returns the link to download the photo and needed headers"""
