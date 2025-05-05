from fastapi import APIRouter, status, Depends
from fastapi.responses import FileResponse
from uuid import UUID

from app.services.animal import AnimalsService
from app.services.image import AnimalImage
from app.core.dependecies import (
    get_image_service,
    get_animals_service,
)

router = APIRouter(prefix="/history/static", tags=["Скачивание картинки указанного животного"])

@router.get(
    "/{uuid_code}",
    status_code=status.HTTP_200_OK,
    responses={
        200: { "description": "Приложение доступно и работает.",
               "content": {"image/jpg": {}},
        },
        500: {"description": "Внутренняя ошибка сервера."},
    },
    response_class=FileResponse
)
async def get_animal_by_uuid(
        uuid_code: UUID,
        animal_service: AnimalsService = Depends(get_animals_service),
        image_service: AnimalImage = Depends(get_image_service)
) -> FileResponse:
    animal = await animal_service.get_animal_by_uuid(uuid_code)
    #if animal is None:
        #return #raise SomeError
    image_path = image_service.get_image_path(animal.processed_image)
    image_name = image_service.get_image_name(animal.processed_image)
    return FileResponse(
        path=image_path,
        media_type="image/jpg",
        filename=image_name
    )
