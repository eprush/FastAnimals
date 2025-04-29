from fastapi import APIRouter
from app.endpoints import animal

routers = APIRouter()

routers.include_router(animal.router)
