from fastapi import APIRouter, status, Depends
from app.services.animal import AnimalsService
from app.services.image import AnimalImage
from app.schemas.animal import (
    AnimalResponseSchema,
)
from app.core.dependecies import (
    get_animals_service,
    get_image_service,
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
async def read_animal_by(
        animal_type: str,
        animal_service: AnimalsService = Depends(get_animals_service),
        image_service: AnimalImage = Depends(get_image_service)
) -> AnimalResponseSchema:
    image = animal_service.request_animal_image(animal_type)
    animal = await animal_service.create_animal(animal_type= animal_type)
    image_path = image_service.save_image(image, name= animal.processed_image)
    image_service.contour(image_path)
    return AnimalResponseSchema(animal_type= animal_type)
