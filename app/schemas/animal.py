"""
A module describing animal schemas
"""

from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
import uuid
from datetime import datetime


class AnimalSchema(BaseModel):
    """ A scheme of animal. """

    animal_type: str = Field(
        ...,
        description="The type of animal whose photo will be downloaded.",
        examples=["dog", "cat", "fox"],
    )

    processed_image: uuid.UUID = Field(
        ...,
        examples=[uuid.uuid4()],
        description="The unique code assigned to the animal image.",
    )

    model_config = ConfigDict(from_attributes=True)

class AnimalDetailSchema(AnimalSchema):
    """ A scheme for showing animal fields. """

    id: int = Field(
        ...,
        description="The unique photo number",
        examples=[1],
    )

    created_at: datetime = Field(
        ...,
        examples=["2025-06-02 23:05:09.377698+03"],
        description="The time when the photo was added."
    )

    model_config = ConfigDict(from_attributes=True)

class AllAnimalsSchema(BaseModel):
    animals: tuple[AnimalDetailSchema, ...] = Field(
        ...,
        description="List of all requests.",
    )

class ImageSchema(BaseModel):
    image: bytes = Field(
        ...,
        description="Image in byte representation."
    )

class AnimalTypeSchema(str, Enum):
    dog = "dog"
    cat = "cat"
    fox = "fox"
