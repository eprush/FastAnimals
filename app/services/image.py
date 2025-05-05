from uuid import UUID
from PIL import Image, ImageFilter
import os

from app.core.config import (
    get_static_dir,
)


def get_image_path(filename: str) -> str:
    return os.path.join(get_static_dir(), filename + ".jpg")

class AnimalImage:
    @staticmethod
    def get_image(name: UUID) -> bytes:
        image_path = get_image_path(str(name))
        return Image.open(image_path).tobytes()

    @staticmethod
    def save_image(data: bytes, *, name: UUID) -> str:
        filepath = get_image_path(str(name))
        #image = Image.frombytes("L", (3, 2), data) # how to get image sizes tuple
        #image.save(filepath)
        with open(filepath, "wb") as file:
            file.write(data)
        return filepath

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
