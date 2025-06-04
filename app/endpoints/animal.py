"""
A module that implements endpoints of the type /{animal_type}
"""


from fastapi import APIRouter, status, Depends, HTTPException

from app.core.dependecies import (
    AnimalServiceDependence,
    ImageServiceDependence,
)
from app.schemas.animal import (
    AnimalSchema,
    AnimalTypeSchema,
)
from app.schemas.problem import ProblemDetail


router = APIRouter(prefix="/animal", tags=["Скачивание фотографии животного определенного типа."])


@router.get(
    "/{animal_type}",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "model": AnimalSchema,
            "description": "Приложение доступно и работает.",
        },
        404: {
            "model": ProblemDetail,
            "description": "Недоступный тип животного.",
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
        animal_type: AnimalTypeSchema,
        animal_service: AnimalServiceDependence,
        image_service: ImageServiceDependence
) -> AnimalSchema:
    """ An endpoint that uploads a random photo of the specified type of animal. """
    animal_image = animal_service.request_animal_image(animal_type= animal_type)
    if animal_image is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Указан неподдерживаемый тип животного.")

    animal = await animal_service.create_animal(animal_type= animal_type)
    image_path = image_service.save_image(animal_image.image, name= animal.processed_image)
    image_service.contour(image_path)
    return AnimalSchema(
        animal_type= animal.animal_type,
        processed_image= animal.processed_image,
    )
