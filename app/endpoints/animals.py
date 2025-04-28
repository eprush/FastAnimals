from fastapi import APIRouter, status
from app.services.animal_service.animals import animal_types
from app.schemas.animal import (
    AnimalResponseSchema,
)

router = APIRouter(prefix="/animal", tags=["Скачивание картинки указанного животного"])


@router.get(
    "/{animal_type}",
    status_code=status.HTTP_200_OK,
    responses={
        200: { "description": "Приложение доступно и работает."},
        500: {"description": "Внутренняя ошибка сервера."},
    }
)
def read_animal_by(animal_type: str) -> AnimalResponseSchema:
    func = animal_types[animal_type]
    link, headers = func()
    return AnimalResponseSchema(animal_type=animal_type, download_link=link)
