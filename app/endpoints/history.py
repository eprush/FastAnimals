from fastapi import APIRouter, status, Depends
from fastapi.responses import FileResponse
from uuid import UUID

from app.services.animal import AnimalsService
from app.services.image import AnimalImage
from app.core.dependecies import (
    get_image_service,
    get_animals_service,
)
from app.schemas.problem import ProblemDetail

router = APIRouter(prefix="/history", tags=["Скачивание картинки указанного животного"])

@router.get(
    "/static/{uuid_code}",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "model": FileResponse,
            "description": "Приложение доступно и работает.",
            "content": {"image/jpg": {}},
        },
        500: {
            "model": ProblemDetail,
            "description": "Внутренняя ошибка сервера."},
    },
    response_class=FileResponse,
    description="""
    Эндпоинт, получающий фотографию животного по uuid.
    """
)
async def read_animal_by_uuid(
        uuid_code: UUID,
        animal_service: AnimalsService = Depends(get_animals_service),
        image_service: AnimalImage = Depends(get_image_service)
) -> FileResponse:
    """ Endpoint that receives a photo of an animal by uuid. """
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

@router.get(
    "",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "model": FileResponse,
            "description": "Приложение доступно и работает.",
            "content": {"application/msexcel": {}},
        },
        500: {
            "model": ProblemDetail,
            "description": "Внутренняя ошибка сервера.",
        },
    },
    response_class=FileResponse,
    description="""
    Эндпоинт, получающий историю всех запросов.
    """
)
async def read_all_animals(
        animal_service: AnimalsService = Depends(get_animals_service)
) -> FileResponse:
    """ The endpoint that gets the history of all requests. """
    animals_path = await animal_service.get_all_animals()
    return FileResponse(
        path=animals_path,
        media_type="application/msexcel",
    )
