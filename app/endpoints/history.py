"""
A module that implements endpoints of the type /history and /history/static/{uuid_code}
"""

from fastapi import APIRouter, status, HTTPException
from fastapi.responses import FileResponse
from uuid import UUID

from app.core.dependecies import (
    AnimalServiceDependence,
    ImageServiceDependence,
)
from app.schemas.problem import ProblemDetail
from app.schemas.animal import AllAnimalsSchema

router = APIRouter(prefix="/history", tags=["Показ истории запросов."])


@router.get(
    "/static/{uuid_code}",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "model": AllAnimalsSchema,
            "description": "Приложение доступно и работает.",
            "content": {"image/jpg": {}},
        },
        404: {
            "model": ProblemDetail,
            "description": "Неверный uuid-код.",
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
        animal_service: AnimalServiceDependence,
        image_service: ImageServiceDependence
) -> FileResponse:
    """ Endpoint that receives a photo of an animal by uuid. """
    animal = await animal_service.get_animal_by_uuid(uuid_code)
    if animal is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Введен несуществующий uuid-код.")

    image_path = image_service.get_image_path(animal.processed_image)
    image_name = image_service.get_image_name(animal.processed_image)
    response = FileResponse(
        path=image_path,
        media_type="image/jpg",
        filename=image_name
    )
    response.headers["animal_type"] = animal.animal_type
    return response


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "Приложение доступно и работает.",
            "content": {"application/json": {}},
        },
        500: {
            "model": ProblemDetail,
            "description": "Внутренняя ошибка сервера.",
        },
    },
    response_model=AllAnimalsSchema,
    description="""
    Эндпоинт, получающий историю всех запросов.
    """
)
async def read_all_animals(
        animal_service: AnimalServiceDependence
) -> AllAnimalsSchema:
    """ The endpoint that gets the history of all requests. """
    animals = await animal_service.get_all_animals()
    return animals
