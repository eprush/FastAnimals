"""
A module defining image service
"""

from uuid import UUID
from PIL import Image, ImageFilter
import os

from app.core.config import (
    get_static_dir,
)


class AnimalImageService:
    @staticmethod
    def get_image_name(name: UUID) -> str:
        """ A method for getting the name of image. """
        return str(name) + ".jpg"

    @staticmethod
    def get_image_path(name: UUID) -> str:
        """ A method for getting the path of image. """
        return os.path.join(get_static_dir(), AnimalImageService.get_image_name(name))

    @staticmethod
    def save_image(data: bytes, *, name: UUID) -> str:
        """ A method for saving the image. """
        image_path = AnimalImageService.get_image_path(name)
        #image = Image.frombytes("L", (3, 2), data) # how to get image sizes tuple
        #image.save(filepath)
        with open(image_path, "wb") as file:
            file.write(data)
        return image_path

    @staticmethod
    def blur(path) -> None:
        """ A method for blurring photo with {path}. """
        with Image.open(path) as image:
            image.filter(filter=ImageFilter.BLUR)
        return

    @staticmethod
    def contour(path) -> None:
        """ A method for contouring photo with {path}. """
        with Image.open(path) as image:
            image.filter(filter=ImageFilter.CONTOUR)
        return
