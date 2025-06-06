"""
A module describing animal model with ORM
"""

import uuid
from sqlalchemy import Integer, Column, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID

from app.core.config import Settings, get_app_settings
from app.models.base import Base

app_settings: Settings = get_app_settings()

class Animal(Base):
    """Animal model."""

    __tablename__ = "animal"

    id = Column(Integer, primary_key=True)
    animal_type = Column(String, nullable=False)
    processed_image = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return (f"Animal with ( \nid={self.id}, \nanimal_type={self.animal_type},"
                f" \nprocessed_image={self.processed_image}, \ncreated_at{self.created_at} \n)")
