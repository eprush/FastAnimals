from fastapi import APIRouter
from endpoints import animal, history

routers = APIRouter()

routers.include_router(animal.router)
routers.include_router(history.router)
