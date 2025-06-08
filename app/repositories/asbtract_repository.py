from abc import ABC, abstractmethod
from uuid import UUID

from app.models.base import BaseModel

class AbstractRepository(ABC):
    Model = None

    @abstractmethod
    def add_by_name(self, name: str) -> BaseModel:
        ...

    @abstractmethod
    def get_by_uuid(self, uuid_code: UUID) -> BaseModel | None:
        ...

    @abstractmethod
    def get_all(self) -> tuple[BaseModel, ...]:
        ...