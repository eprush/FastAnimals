from fastapi import APIRouter
from app.endpoints import animals

routers = APIRouter()

routers.include_router(animals.router)
