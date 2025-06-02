"""
A module that creates routers with all endpoints
"""

from fastapi import APIRouter
from app.endpoints import animal, history

routers = APIRouter()

routers.include_router(animal.router)
routers.include_router(history.router)
