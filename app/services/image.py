from uuid import UUID
from PIL import Image, ImageFilter
import os

from app.core.config import (
    get_static_dir,
)


class AnimalImage:
    @staticmethod
    def get_image_name(name: UUID) -> str:
        return str(name) + ".jpg"

    @staticmethod
    def get_image_path(name: UUID) -> str:
        return os.path.join(get_static_dir(), AnimalImage.get_image_name(name))

    @staticmethod
    def save_image(data: bytes, *, name: UUID) -> str:
        image_path = AnimalImage.get_image_path(name)
        #image = Image.frombytes("L", (3, 2), data) # how to get image sizes tuple
        #image.save(filepath)
        with open(image_path, "wb") as file:
            file.write(data)
        return image_path

    @staticmethod
    def blur(path) -> None:
        with Image.open(path) as image:
            image.filter(filter=ImageFilter.BLUR)
        return

    @staticmethod
    def contour(path) -> None:
        with Image.open(path) as image:
            image.filter(filter=ImageFilter.CONTOUR)
        return
