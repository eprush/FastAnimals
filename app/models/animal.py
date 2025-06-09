"""
A module describing animal model with ORM
"""

import uuid
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class Animal(BaseModel):
    """Animal model."""

    __tablename__ = "animal"

    id: Mapped[int] = mapped_column(primary_key=True)
    animal_type: Mapped[str] = mapped_column(nullable=False)
    processed_image: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, unique=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    def __repr__(self):
        return (f"Animal with ( \nid={self.id}, \nanimal_type={self.animal_type},"
                f" \nprocessed_image={self.processed_image} \n)")
