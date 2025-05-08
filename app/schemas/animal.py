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


class AnimalTypeSchema(BaseModel):
    """ The scheme for obtaining the type of animal. """

    animal_type: str = Field(
        ...,
        description="The type of animal whose photo will be downloaded.",
        examples=["dog", "cat", "fox"],
    )

    @field_validator("animal_type")
    def validate_animal_type(self, animal_type: str) -> str | None:
        if animal_type is None:
            return animal_type
        available_animal_types = ("dog", "cat", "fox")
        if animal_type not in available_animal_types:
            raise ValueError("Invalid animal type")
        return animal_type
