from PIL import Image, ImageFilter

class AnimalImage:
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
