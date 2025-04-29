from fastapi import APIRouter
from app.endpoints import animal_endpoint

routers = APIRouter()

routers.include_router(animal_endpoint.router)
