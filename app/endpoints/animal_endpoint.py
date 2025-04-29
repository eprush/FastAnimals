from fastapi import APIRouter, status, Depends
from app.services.animal_service.animals import AnimalsService
from app.schemas.animal_schema import (
    AnimalResponseSchema,
)
from app.core.dependecies import get_animals_service

router = APIRouter(prefix="/animal", tags=["Скачивание картинки указанного животного"])


@router.get(
    "/{animal_type}",
    status_code=status.HTTP_200_OK,
    responses={
        200: { "description": "Приложение доступно и работает."},
        500: {"description": "Внутренняя ошибка сервера."},
    }
)
async def read_animal_by(
        animal_type: str,
        animal_service: AnimalsService = Depends(get_animals_service)
) -> AnimalResponseSchema:
    animal = await animal_service.create_animal_by(animal_type= animal_type)
    image = animal_service.get_animal_image(animal_type)
    animal_service.save_image(image, name= animal.processed_image)
    return AnimalResponseSchema(animal_type= animal_type)
