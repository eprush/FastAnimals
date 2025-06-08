"""
A module describing animal model with ORM
"""

import uuid
from sqlalchemy import Integer, Column, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID

from app.models.base import BaseModel


class Animal(BaseModel):
    """Animal model."""

    __tablename__ = "animal"

    id = Column(Integer, primary_key=True)
    animal_type = Column(String, nullable=False)
    processed_image = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return (f"Animal with ( \nid={self.id}, \nanimal_type={self.animal_type},"
                f" \nprocessed_image={self.processed_image} \n)")
