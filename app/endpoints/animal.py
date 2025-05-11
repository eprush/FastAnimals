from fastapi import APIRouter, status, Depends
from app.services.animal import AnimalsService
from app.services.image import AnimalImage
from app.schemas.animal import (
    AnimalSchema,
    AnimalTypeSchema,
)
from app.schemas.problem import ProblemDetail
from app.core.dependecies import (
    get_animals_service,
    get_image_service,
)

router = APIRouter(prefix="/animal", tags=["Скачивание картинки."])


@router.get(
    "/{animal_type}",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "model": AnimalSchema,
            "description": "Приложение доступно и работает."
        },
        500: {
            "model": ProblemDetail,
            "description": "Внутренняя ошибка сервера.",
        },
    },
    response_model=AnimalSchema,
    description="""
        Эндпоинт, загружающий случайную фотографию указанного типа животного.
        На фото накладывается фильтр.
        Данные о фото сохраняются в бд.
    """,
)
async def read_animal_by_type(
        type_to_read: AnimalTypeSchema,
        animal_service: AnimalsService = Depends(get_animals_service),
        image_service: AnimalImage = Depends(get_image_service)
) -> AnimalSchema:
    """ An endpoint that uploads a random photo of the specified type of animal. """
    image = animal_service.request_animal_image(type_to_read.animal_type)
    animal = await animal_service.create_animal(animal_type= type_to_read.animal_type)
    image_path = image_service.save_image(image, name= animal.processed_image)
    image_service.contour(image_path)
    return AnimalSchema(
        animal_type= type_to_read,
        processed_image= animal.processed_image,
    )
