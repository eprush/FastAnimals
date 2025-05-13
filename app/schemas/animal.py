from pydantic import BaseModel, Field, ConfigDict, field_validator
from uuid import UUID
from datetime import datetime

class AnimalSchema(BaseModel):
    """ A scheme of animal. """

    animal_type: str = Field(
        ...,
        description="The type of animal whose photo will be downloaded.",
        examples=["dog", "cat", "fox"],
    )

    processed_image: UUID = Field(
        ...,
        description="The unique code assigned to the animal image.",
    )

    model_config = ConfigDict(from_attributes=True)


class AnimalDetailSchema(BaseModel):
    """ A scheme for showing animal fields. """

    id: int = Field(
        ...,
        description="The unique photo number",
        examples=[1],
    )

    animal_type: str = Field(
        ...,
        description="The type of animal whose photo will be downloaded.",
        examples=["dog", "cat", "fox"],
    )

    processed_image: UUID = Field(
        ...,
        description="The unique code assigned to the animal image.",
    )

    created_at: datetime = Field(
        ...,
        description="The time when the photo was added."
    )

    model_config = ConfigDict(from_attributes=True)

class AllAnimalsSchema(BaseModel):
    animals: tuple[AnimalDetailSchema, ...] = Field(
        ...,
        description="List of all requests.",
    )

class ImageSchema(BaseModel):
    image = bytes = Field(
        ...,
        description="Image in byte representation."
    )

class AnimalTypeSchema(BaseModel):
    """ The scheme for obtaining the type of animal. """

    animal_type: str = Field(
        ...,
        description="The type of animal whose photo will be downloaded.",
        examples=["dog", "cat", "fox"],
    )

    model_config = ConfigDict(from_attributes=True)
